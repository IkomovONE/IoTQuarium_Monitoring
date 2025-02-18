from typing import Union
import time
import threading
import random
from datetime import datetime
from openai import OpenAI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse                                  #Importing necessary libraries.
from dotenv import load_dotenv
import os
from pydantic import BaseModel
from pymongo import MongoClient
from pymongo import DESCENDING
from fastapi.middleware.cors import CORSMiddleware
import sensors




load_dotenv()                                    #Loading .env file.
api_key = os.getenv("OPENAI_API_KEY")            #Getting OpenAI api key.


app = FastAPI()                                    #initializing FastAPI app.

client = OpenAI()                                   #Initializing OpenAI client

Mongoclient = MongoClient("mongodb://localhost:27017/")         #Initializing MongoDB connection. 

db = Mongoclient["IoT_Quarium_Monitoring"]              #Initializing the database.




app.add_middleware(                                 #CORS middleware for request filtering. Alowing requests only from domain
    CORSMiddleware,
    allow_origins="https://iotquarium.info",
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers="*",
)

class Request(BaseModel):           #Request class for messaging
    role: str
    content: str  
   

#Initializing "context" and "messages" global changeable variables, initially containing GPT guidance text.

context= [{"role": "system", "content": "You are a helpful pet shop aquarium assistant, You are a part of an IoT system where Raspberry Pi collects aquarium data using sensors and sends it to you. You need to analyze the data and provide the status when asked to, or just assist with general questions. Each time u will get list of messages as a history of conversation/data, and u need to assist based on the data history and saved knowledge. Additionaly, when u're told about aquarium environment statistics, such as temperature or pH, u should not answer anything, but memorize it as current status of the aquarium and then give values plus evaluation when asked about the status. The sensor values are sent from _system_, automatically, so u don't have to answer this. Also bit about the data sent to you: application collects environment data each hour, after 24 hours calculates average, and sends to you when user opens the web page. For example, AverageTemp is a daily average which was calculated and recorded at the time mentioned in the Date: and time: fields. Another data that can be sent to you is at the moment when user opens the web page: at this point of time the whole conversation context will be sent to you and the last message would be the sensor data of the most recent data recording (not average, hourly data)"}]


messages= [{"role": "system", "content": "You are a helpful pet shop aquarium assistant, You are a part of an IoT system where Raspberry Pi collects aquarium data using sensors and sends it to you. You need to analyze the data and provide the status when asked to, or just assist with general questions. Each time u will get list of messages as a history of conversation/data, and u need to assist based on the data history and saved knowledge. Additionaly, when u're told about aquarium environment statistics, such as temperature or pH, u should not answer anything, but memorize it as current status of the aquarium and then give values plus evaluation when asked about the status. The sensor values are sent from _system_, automatically, so u don't have to answer this. Also bit about the data sent to you: application collects environment data each hour, after 24 hours calculates average, and sends to you when user opens the web page. For example, AverageTemp is a daily average which was calculated and recorded at the time mentioned in the Date: and time: fields. Another data that can be sent to you is at the moment when user opens the web page: at this point of time the whole conversation context will be sent to you and the last message would be the sensor data of the most recent data recording (not average, hourly data)"}]

Light_counter= 0                        #Counter for light hours

Current_light_status= "OFF"             #Current light status

message_history = db["Message_history"]     #initializing message history database document

data_table = db["Aquarium_Data"]            #initializing aquarium data database document

daily_data_table= db["Aquarium_data_daily_average"]         #initializing daily average aquarium data database document

input_thread = None         #Initializing thread variables
daily_thread = None

#########################################################



############## METHODS START HERE ####################


def convert_message_to_api_format(response_role, response_content):
    formatted_message = {"role": response_role,  "content": response_content}           #Method for converting messages to OpenAI api format.
    return formatted_message


def save_msg(i):
    message_history.insert_one(i)                                      #Method for saving chat messages into database
    processed_response= convert_message_to_api_format(i["role"], i["content"])
    return processed_response


def input_data():                       #Method for regular data gathering, uses sensor.py to initialize the measurements 
    global Current_light_status     #Mentioning global variables
    global Light_counter
    attempt= 0          #Attempt variable for error handling. Thread closes after several failed attempts.

    while True:
        try:

            attempt+=1

            if attempt==20:     #Close the thread if 20 failed attempts
                break

            sensor_data_list= sensors.main()          #Calling sensors.py main method to gather sensor data

            sensor_data = {             #Forming structured data json               #"Random" for testing purposes  
            "Temp": sensor_data_list[0],                                            #round(23.0 + random.uniform(0.0, 1.0), 1),  # 23.0 to 24.0
            "pH": sensor_data_list[2],                                              #round(7.0 + random.uniform(0.0, 0.6), 1),    # 7.0 to 7.6
            "TDS":  sensor_data_list[3],                                            #round(50 + random.uniform(0.0, 450.0), 1), 
            "LightNow": sensor_data_list[1],                                        #"ON" if random.choice([True, False]) else "OFF", 
            "WaterLevel": sensor_data_list[4],                                      #random.choice(["Sufficient", "Low", "Critical"]),
            "WaterFlow": sensor_data_list[5],                                       #random.choice(["Normal", "Weak", "Strong"]),
            "timestamp": datetime.now().isoformat()
            }
            
            data_table.insert_one(sensor_data)          #Inserting sensor data into the database

            attempt=0

            if sensor_data_list[1]== "ON":      #Counting light hours
                Light_counter+=1

            Current_light_status= sensor_data_list[1]       #updating global current light status for daily average method

            time.sleep(300)     #5 minute sleep

        except Exception as e:
            print(f"Error in input_data thread: {e}")          #Error handling
            time.sleep(15)
            continue
        
        continue

    return True


def daily_data_input():             #Method for recording daily average

    global Current_light_status
    global Light_counter            #Mentioning global variables
    global context


    avg_data = {
                "timestamp": datetime.now().isoformat(),        #Forming average data json, initial entry at program execution
                "AverageTemp": 0,
                "AveragepH": 0,
                "AverageTDS": 0,
                "LightDuration": 0,
            }
            
            
    daily_data_table.insert_one(avg_data)       #Adding initial entry

    request= str(avg_data)                      
    role= "system"                                                      #Adding initial entry to context for GPT
    converted_input= convert_message_to_api_format(role, request)
    context.append(converted_input)

    time.sleep(60)      #1 minute rest


    while True:
        if Current_light_status == "ON":            #For precise "light on" measurement, the measurement timer starts only after the light is OFF
            print("Light is on, waiting until the light turns off to start the daily averages timer...")
            time.sleep(1200)    #Waiting 20 minutes
            continue

        elif Current_light_status == "OFF":     #Breaking the loop if the light is OFF
            Light_counter= 0
            break


    while True:
        print("Starting daily average measurement process")
        time.sleep(86400)                                   #Waiting 24 hours

        Light_on_duration= Light_counter * 5
        Light_on_duration= Light_on_duration/60         #Calculating Light on hours
        Light_on_duration= round(Light_on_duration, 1)


        recent_data = list(data_table.find().sort("timestamp", DESCENDING).limit(288))      #Gathering all 24 hour measurements to form daily averages

        if len(recent_data) == 288:
            avg_temp = sum(d['Temp'] for d in recent_data) / 288            #calculating averages
            avg_ph = sum(d['pH'] for d in recent_data) / 288
            avg_tds = sum(d['TDS'] for d in recent_data) / 288
            
           
            avg_data = {
                "timestamp": datetime.now().isoformat(),
                "AverageTemp": round(avg_temp, 1),              #Forming average data json
                "AveragepH": round(avg_ph, 1),
                "AverageTDS": round(avg_tds, 1),
                "LightDuration": Light_on_duration,
            }
            
           
            daily_data_table.insert_one(avg_data)           #Inserting daily average to database


            request= str(avg_data)
            role= "system"
            converted_input= convert_message_to_api_format(role, request)       #Adding daily average to GPT's context
            context.append(converted_input)

            if len(context) > 25:           
                context = context[:1] + context[-15:]       #Trimming GPT's context in case it's too big (avoiding big OpenAI costs)


            print(f"Daily averages saved: {avg_data}")
            Light_counter = 0
        
       
        

########## STARTUP INITIALIZATION CONTINUES HERE #################



@app.on_event("startup")
def start_data_generation():
    global input_thread, daily_thread
    input_thread = threading.Thread(target=input_data, daemon=True)             #Starting data measurement and daily averages threads
    daily_thread = threading.Thread(target=daily_data_input, daemon=True)
    input_thread.start()
    daily_thread.start()
    

entries= daily_data_table.find()
for i in entries:
    context_history_msg= convert_message_to_api_format("system", str(i))        #Adding past daily averages to GPT's context
    context.append(context_history_msg)

if len(context) > 10:
    context = context[:1] + context[-5:]        #Trimming the GPT's context

    
#############################################




############ APIs START HERE ############## 



@app.get("/message-gpt")            #API for messaging GPT (Getting initial GPT's status message when opening the chat page)
def message_gpt():
    global messages
    global context

    messages= messages[:1]      #Messages variable for storing messages


    recent_data = data_table.find().sort("timestamp", DESCENDING).limit(1)
    data = recent_data[0]                                                       #recent data for GPT prompt
    recent_data_message = convert_message_to_api_format("system", str(data))


    gpt_prompt= []      #GPT prompt

    for i in context:
        gpt_prompt.append(i)        #Adding context to GPT prompt

    gpt_prompt.append(recent_data_message)      #Adding recent data message


    #Adding extra guidance for GPT

    gpt_prompt.append({"role": "system", "content": "Chat with AI view: tell the status of the aquarium, including daily av evaluation and most recent recording. Limit: 100 words, Example format: Good conditions! Temperature is appropriate, liquid level is sufficient, pH is balanced, water TDS is normal.<(U can add more detailed status report)> What would you like to ask?"})
    

    completion = client.chat.completions.create(        #Creating OpenAI prompt request
    model="gpt-4o-mini",
    messages= gpt_prompt
    )
    

    response= completion.choices[0].message     #Getting response
    response_role= response.role
    response_content= response.content
    processed_response= convert_message_to_api_format(response_role, response_content)


    processed= save_msg(processed_response)         #Saving msg response
    messages.append(processed)

    return messages     #Returning messages


@app.get("/message-history")            #API for returning message history
def get_message_history():
    message_history_list= message_history.find()    #Gathering messages from database
    returnable_list=[]

    for i in message_history_list:


        context_history_msg= convert_message_to_api_format(i["role"], i["content"])             #Converting and returning the messages

        returnable_list.append(context_history_msg) 

    return returnable_list





@app.post("/ask-gpt")                   #API for sending GPT a message in the chat view
def ask_gpt(request: Request):
    global messages

    body = request
    request_message= {'role': body.role, 'content': body.content}       #Forming a message based on received body

    messages.append(request_message)    #Adding message to history

    converted_input= convert_message_to_api_format(body.role, body.content)
    save_msg(converted_input)                                                   #Saving the message to database
    converted_input= convert_message_to_api_format(body.role, body.content)



   
    completion = client.chat.completions.create(        #Creating completion to send to OpenAI
    model="gpt-4o-mini",
    messages= messages
)
    

    response= completion.choices[0].message
    response_role= response.role
    response_content= response.content                                                      #Processing response
    processed_response= convert_message_to_api_format(response_role, response_content)

    processed= save_msg(processed_response)     #Saving to database and to current chat history
    messages.append(processed)


    processed_response= convert_message_to_api_format(response_role, response_content)      #Converting and returning the response
    return processed_response





@app.get("/dashboard/")                 #API for dashboard information, including GPT's status update
def read_root():


    dashboard_context= []                   #Dashboard context with initial message
    dashboard_context.append(context[0])
   


    recent_data = data_table.find().sort("timestamp", DESCENDING).limit(1)              #Getting all the recent data from DB
    recent_daily_data = daily_data_table.find().sort("timestamp", DESCENDING).limit(1)
    data = recent_data[0]
    daily_data= recent_daily_data[0]

    api_response= []    #Initializing returnable

    recent_data_message = convert_message_to_api_format("system", str(data))        #converting all recent data to messages
    daily_data_message = convert_message_to_api_format("system", str(daily_data))

    
    dashboard_context.append(daily_data_message)
    dashboard_context.append(recent_data_message)       #Updating dashboard context for GPT request

    api_response.append(recent_data_message)        

    #Context guidance for GPT
    dashboard_context.append({"role": "system", "content": "DASHBOARD VIEW: tell the status of the aquarium, including daily av evaluation and most recent recording. Limit: 33-35 words, Example format: Good conditions! Temperature is appropriate, liquid level is sufficient, pH is balanced, water TDS is normal. You can press 'Ask GPT' to ask me anything!"})
    


    completion = client.chat.completions.create(        #Creating completion for OpenAI
    model="gpt-4o-mini",
    messages= dashboard_context
    )
    
    response= completion.choices[0].message
    response_role= response.role                                #Processing response
    response_content= response.content                      
    processed_response= convert_message_to_api_format(response_role, response_content)


    api_response.append(processed_response)         #Preparing api returnable
    api_response.append(daily_data_message)
    return api_response














