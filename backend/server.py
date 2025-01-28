from typing import Union
import time
import threading
import random
import uvicorn
from slowapi import Limiter
from slowapi.util import get_remote_address
from datetime import datetime
from openai import OpenAI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import os
from pydantic import BaseModel
from pymongo import MongoClient
from pymongo import DESCENDING
from fastapi.middleware.cors import CORSMiddleware
import sensors



def convert_message_to_api_format(response_role, response_content):
    
    formatted_message = { "role": response_role,  "content": response_content  }
    
    
    return formatted_message


load_dotenv()  
api_key = os.getenv("OPENAI_API_KEY")


app = FastAPI()




client = OpenAI()

Mongoclient = MongoClient("mongodb://localhost:27017/")  

db = Mongoclient["IoT_Quarium_Monitoring"]

limiter = Limiter(key_func=get_remote_address)


app.add_middleware(
    CORSMiddleware,
    allow_origins="https://iotquarium.info",
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers="*",
)

class Request(BaseModel):
    role: str
    content: str  
   







context= [{"role": "system", "content": "You are a helpful pet shop aquarium assistant, You are a part of an IoT system where Raspberry Pi collects aquarium data using sensors and sends it to you. You need to analyze the data and provide the status when asked to, or just assist with general questions. Each time u will get list of messages as a history of conversation/data, and u need to assist based on the data history and saved knowledge. Additionaly, when u're told about aquarium environment statistics, such as temperature or pH, u should not answer anything, but memorize it as current status of the aquarium and then give values plus evaluation when asked about the status. The sensor values are sent from _system_, automatically, so u don't have to answer this. Also bit about the data sent to you: application collects environment data each hour, after 24 hours calculates average, and sends to you when user opens the web page. For example, AverageTemp is a daily average which was calculated and recorded at the time mentioned in the Date: and time: fields. Another data that can be sent to you is at the moment when user opens the web page: at this point of time the whole conversation context will be sent to you and the last message would be the sensor data of the most recent data recording (not average, hourly data)"}]

messages= [{"role": "system", "content": "You are a helpful pet shop aquarium assistant, You are a part of an IoT system where Raspberry Pi collects aquarium data using sensors and sends it to you. You need to analyze the data and provide the status when asked to, or just assist with general questions. Each time u will get list of messages as a history of conversation/data, and u need to assist based on the data history and saved knowledge. Additionaly, when u're told about aquarium environment statistics, such as temperature or pH, u should not answer anything, but memorize it as current status of the aquarium and then give values plus evaluation when asked about the status. The sensor values are sent from _system_, automatically, so u don't have to answer this. Also bit about the data sent to you: application collects environment data each hour, after 24 hours calculates average, and sends to you when user opens the web page. For example, AverageTemp is a daily average which was calculated and recorded at the time mentioned in the Date: and time: fields. Another data that can be sent to you is at the moment when user opens the web page: at this point of time the whole conversation context will be sent to you and the last message would be the sensor data of the most recent data recording (not average, hourly data)"}]

Light_counter= 0

Current_light_status= "OFF"

message_history = db["Message_history"]

data_table = db["Aquarium_Data"]

daily_data_table= db["Aquarium_data_daily_average"]

input_thread = None
daily_thread = None



def save_msg(i):
    
    message_history.insert_one(i)

    processed_response= convert_message_to_api_format(i["role"], i["content"])

    return processed_response


def input_data():

    global Current_light_status

    global Light_counter

    

   

    attempt= 0


    while True:

        try:

            attempt+=1

            if attempt==10:
                break


            sensor_data_list= sensors.main()


            sensor_data = {
            "Temp": sensor_data_list[0],                             #round(23.0 + random.uniform(0.0, 1.0), 1),  # 23.0 to 24.0
            "pH": sensor_data_list[2],                               #round(7.0 + random.uniform(0.0, 0.6), 1),    # 7.0 to 7.6
            "TDS":  sensor_data_list[3],                            #round(50 + random.uniform(0.0, 450.0), 1), 
            "LightNow": sensor_data_list[1],                       #"ON" if random.choice([True, False]) else "OFF", 
            "WaterLevel": sensor_data_list[4],                    #random.choice(["Sufficient", "Low", "Critical"]),
            "WaterFlow": sensor_data_list[5],                     #random.choice(["Normal", "Weak", "Strong"]),
            "timestamp": datetime.now().isoformat()
            
            }
            
            data_table.insert_one(sensor_data)

            attempt=0

            if sensor_data_list[1]== "ON":

                Light_counter+=1

            Current_light_status= sensor_data_list[1]


            time.sleep(300)


        except Exception as e:
            print(f"Error in input_data thread: {e}")
            time.sleep(15)
            continue
            


        continue

    return True



def daily_data_input():

    global Current_light_status

    global Light_counter


    avg_data = {
                "timestamp": datetime.now().isoformat(),
                "AverageTemp": 0,
                "AveragepH": 0,
                "AverageTDS": 0,
                "LightDuration": 0,
            }
            
            
    daily_data_table.insert_one(avg_data)


    request= str(avg_data)

    role= "system"


    converted_input= convert_message_to_api_format(role, request)

    
    

    context.append(converted_input)

    time.sleep(60)

    while True:
        if Current_light_status == "ON":

            print("Light is on, waiting until the light turns off to start the daily averages timer...")

            time.sleep(1200)

            continue

        elif Current_light_status == "OFF":

            Light_counter= 0

            break


    while True:


        time.sleep(86430) # 24 hours
       

        Light_on_duration= Light_counter * 5

        Light_on_duration= Light_on_duration/60

        Light_on_duration= round(Light_on_duration, 1)


        recent_data = list(data_table.find().sort("timestamp", DESCENDING).limit(288))


       

    

        
        
        if len(recent_data) == 288:
           
            avg_temp = sum(d['Temp'] for d in recent_data) / 288
            avg_ph = sum(d['pH'] for d in recent_data) / 288
            avg_tds = sum(d['TDS'] for d in recent_data) / 288
            
           
            avg_data = {
                "timestamp": datetime.now().isoformat(),
                "AverageTemp": round(avg_temp, 1),
                "AveragepH": round(avg_ph, 1),
                "AverageTDS": round(avg_tds, 1),
                "LightDuration": Light_on_duration,
            }
            
           
            daily_data_table.insert_one(avg_data)


            request= str(avg_data)
        
            role= "system"


            converted_input= convert_message_to_api_format(role, request)

            
            

            context.append(converted_input)

            if len(context) > 25:

                context = context[:1] + context[-15:]


            print(f"Daily averages saved: {avg_data}")

            Light_counter = 0
        
       
        

######



@app.on_event("startup")
def start_data_generation():
    global input_thread, daily_thread
    input_thread = threading.Thread(target=input_data, daemon=True)
    daily_thread = threading.Thread(target=daily_data_input, daemon=True)
    input_thread.start()
    daily_thread.start()
    


#####


entries= daily_data_table.find()


for i in entries:


    context_history_msg= convert_message_to_api_format("system", str(i))

    
    context.append(context_history_msg)


if len(context) > 10:

    context = context[:1] + context[-5:]

    









@app.get("/message-gpt")
def message_gpt():


    global messages

    messages= messages[:1]


    recent_data = data_table.find().sort("timestamp", DESCENDING).limit(1)
    recent_daily_data = daily_data_table.find().sort("timestamp", DESCENDING).limit(1)

    data = recent_data[0]

    daily_data= recent_daily_data[0]


    recent_data_message = convert_message_to_api_format("system", str(data))

    daily_data_message = convert_message_to_api_format("system", str(daily_data))

    
    



    gpt_prompt= []





    for i in context:

       

        gpt_prompt.append(i)

     
    gpt_prompt.append(recent_data_message)


  

    gpt_prompt.append({"role": "system", "content": "Chat with AI view: tell the status of the aquarium, including daily av evaluation and most recent recording. Limit: 100 words, Example format: Good conditions! Temperature is appropriate, liquid level is sufficient, pH is balanced, water TDS is normal.<(U can add more detailed status report)> What would you like to ask?"})
    

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages= gpt_prompt
)
    

    response= completion.choices[0].message

    

    response_role= response.role

    response_content= response.content


    processed_response= convert_message_to_api_format(response_role, response_content)


    

    

   

    

    processed= save_msg(processed_response)

    messages.append(processed)




    return messages


@app.get("/message-history")
def get_message_history():

    message_history_list= message_history.find()

    returnable_list=[]


   


    for i in message_history_list:


        context_history_msg= convert_message_to_api_format(i["role"], i["content"])

        returnable_list.append(context_history_msg)



        


    return returnable_list





@app.post("/ask-gpt")
def ask_gpt(request: Request):

    global messages



    body = request

    request_message= {'role': body.role, 'content': body.content}

   
    messages.append(request_message)

    converted_input= convert_message_to_api_format(body.role, body.content)

   

   

    save_msg(converted_input)

    

    

    converted_input= convert_message_to_api_format(body.role, body.content)


    

   
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages= messages
)
    

    response= completion.choices[0].message

    

    response_role= response.role

    response_content= response.content



   

    


    processed_response= convert_message_to_api_format(response_role, response_content)

    


    

    
    processed= save_msg(processed_response)

    messages.append(processed)


    processed_response= convert_message_to_api_format(response_role, response_content)

   

    
    

    


    return processed_response





@app.get("/dashboard/")
def read_root():


    dashboard_context= []

    dashboard_context.append(context[0])
   


    recent_data = data_table.find().sort("timestamp", DESCENDING).limit(1)
    recent_daily_data = daily_data_table.find().sort("timestamp", DESCENDING).limit(1)



    data = recent_data[0]

    daily_data= recent_daily_data[0]


    api_response= []





    recent_data_message = convert_message_to_api_format("system", str(data))

    daily_data_message = convert_message_to_api_format("system", str(daily_data))

    
    dashboard_context.append(daily_data_message)
    
    dashboard_context.append(recent_data_message)

    


    api_response.append(recent_data_message)

    

    dashboard_context.append({"role": "system", "content": "DASHBOARD VIEW: tell the status of the aquarium, including daily av evaluation and most recent recording. Limit: 33-35 words, Example format: Good conditions! Temperature is appropriate, liquid level is sufficient, pH is balanced, water TDS is normal. You can press 'Ask GPT' to ask me anything!"})
    



    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages= dashboard_context
)
    

    response= completion.choices[0].message

    

    response_role= response.role

    response_content= response.content


    processed_response= convert_message_to_api_format(response_role, response_content)


    

    

    api_response.append(processed_response)

    api_response.append(daily_data_message)

    




    return api_response














