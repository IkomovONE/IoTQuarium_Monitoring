from typing import Union
import time
import threading
import random
import uvicorn
from datetime import datetime
from openai import OpenAI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from pymongo import DESCENDING
from fastapi.middleware.cors import CORSMiddleware


def convert_message_to_api_format(response_role, response_content):
    
    formatted_message = { "role": response_role,  "content": response_content  }
    
    
    return formatted_message


load_dotenv()  
api_key = os.getenv("OPENAI_API_KEY")


app = FastAPI()




client = OpenAI()

Mongoclient = MongoClient("mongodb://localhost:27017/")  # Local MongoDB instance

db = Mongoclient["IoT_Quarium_Monitoring"]


app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:8080",
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers="*",
)



#{"role": "system", "content": "You are a helpful pet shop aquarium assistant, You are a part of an IoT system where Raspberry Pi collects aquarium data using sensors and sends it to you. You need to analyze the data and provide the status whe asked to, or just assist with general questions. Each time u will get list of messages as a history of conversation/data, and u need to assist based on the data history and saved knowledge. Additionaly, when u're told about aquarium environment statistics, such as temperature or pH, u should not answer anything, but memorize it as current ststus of the aquarium and then give values plus evaluation when asked about the status"}






context= [{"role": "system", "content": "You are a helpful pet shop aquarium assistant, You are a part of an IoT system where Raspberry Pi collects aquarium data using sensors and sends it to you. You need to analyze the data and provide the status when asked to, or just assist with general questions. Each time u will get list of messages as a history of conversation/data, and u need to assist based on the data history and saved knowledge. Additionaly, when u're told about aquarium environment statistics, such as temperature or pH, u should not answer anything, but memorize it as current status of the aquarium and then give values plus evaluation when asked about the status. The sensor values are sent from _system_, automatically, so u don't have to answer this. Also bit about the data sent to you: application collects environment data each hour, after 24 hours calculates average, and sends to you when user opens the web page. For example, AverageTemp is a daily average which was calculated and recorded at the time mentioned in the Date: and time: fields. Another data that can be sent to you is at the moment when user opens the web page: at this point of time the whole conversation context will be sent to you and the last message would be the sensor data of the most recent data recording (not average, hourly data)"}]



context_table = db["Assistant_context"]

data_table = db["Aquarium_Data"]

daily_data_table= db["Aquarium_data_daily_average"]










def input_data():

    #Make database entry

    #Append to the context list

    #Send context to openAI


    #So, let's say I don't open the frontend application for a long time. 
    # Sensors record the data for a couple of days, calculate the average temperature/pH/etc every 12h, 
    # convert the data to a gpt message {role: system, content: Temp: 23, pH: 7.5} and 
    # save the message to the collection of messages for the context. Also data is saved separately to DB.
    # Then, when I open the app and check the dashboard the whole context list is 
    # fetched from the database and only 1 request is sent to show the status, 
    # and GPT sees the data through the whole long period and the most recent one.



    while True:
        sensor_data = {
        "Temp": round(23.0 + random.uniform(0.0, 1.0), 1),  # 23.0 to 24.0
        "pH": round(7.0 + random.uniform(0.0, 0.6), 1),    # 7.0 to 7.6
        "TDS": round(50 + random.uniform(0.0, 450.0), 1),
        "LightNow": "ON" if random.choice([True, False]) else "OFF",  # Random ON/OFF
        "WaterLevel": random.choice(["Sufficient", "Low", "Critical"]),
        "WaterFlow": random.choice(["Normal", "Weak", "Strong"]),
        "timestamp": datetime.now().isoformat()
        
    }
        
        data_table.insert_one(sensor_data)





        time.sleep(3600)


        continue

    return True



def daily_data_input():
    while True:

        time.sleep(86430)  # 86400 seconds = 24 hours
        #time.sleep(20)
        # Get the last 24 entries from the data_table

        recent_data = list(data_table.find().sort("timestamp", DESCENDING).limit(24))


        print(recent_data)

    

        
        
        if len(recent_data) == 24:
            # Calculate averages
            avg_temp = sum(d['Temp'] for d in recent_data) / 24
            avg_ph = sum(d['pH'] for d in recent_data) / 24
            avg_tds = sum(d['TDS'] for d in recent_data) / 24
            
            # Prepare the averaged data document
            avg_data = {
                "timestamp": datetime.now().isoformat(),
                "AverageTemp": round(avg_temp, 1),
                "AveragepH": round(avg_ph, 1),
                "AverageTDS": round(avg_tds, 1)
            }
            
            # Insert the average data into the Daily_Average_Data collection
            daily_data_table.insert_one(avg_data)


            request= str(avg_data)
        
            role= "system"


            converted_input= convert_message_to_api_format(role, request)

            context_table.insert_one(converted_input)

            converted_input= convert_message_to_api_format(role, request)
            

            context.append(converted_input)


            print(f"Daily averages saved: {avg_data}")
        
        # Sleep for 1 day (24 hours) before running again
        

######

@app.on_event("startup")
def start_data_generation():
    threading.Thread(target=input_data, daemon=True).start()
    threading.Thread(target=daily_data_input, daemon=True).start()


#####


entries= context_table.find()


for i in entries:


    context_history_msg= convert_message_to_api_format(i["role"], i["content"])

    
    context.append(context_history_msg)









@app.get("/message-gpt")
def message_gpt():

    request= input("Enter request:")

    role= "system"


    converted_input= convert_message_to_api_format(role, request)

    context_table.insert_one(converted_input)

    converted_input= convert_message_to_api_format(role, request)
    

    context.append(converted_input)





    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages= context
)
    




    response= completion.choices[0].message

    

    response_role= response.role

    response_content= response.content


    processed_response= convert_message_to_api_format(response_role, response_content)


    context_table.insert_one(processed_response)

    processed_response= convert_message_to_api_format(response_role, response_content)

    context.append(processed_response)




    processed_chat= []


    for i in context:

        

        formatted_message = f'{{"ROLE": "{i["role"]}", "CONTENT": "{i["content"]}"}}'
        processed_chat.append(formatted_message)

    formatted_output = "<br><br><br><br><br><br><br><br>".join(processed_chat)


    

    return HTMLResponse(content=f"<pre>{formatted_output}</pre>")







@app.get("/dashboard/")
def read_root():

    print(context)


    recent_data = data_table.find().sort("timestamp", DESCENDING).limit(1)

    print(recent_data)

    recent_daily_data = daily_data_table.find().sort("timestamp", DESCENDING).limit(1)

    data = recent_data[0]

    daily_data= recent_daily_data[0]


    api_response= []


    

    

    



    #data = recent_data[0] if recent_data.count() > 0 else None


    
    print(data)

    #print(daily_data)


    recent_data_message = convert_message_to_api_format("system", str(data))

    daily_data_message = convert_message_to_api_format("system", str(daily_data))

    
    
    
    context.append(recent_data_message)


    api_response.append(recent_data_message)

    

    context.append({"role": "system", "content": "DASHBOARD VIEW: tell the status of the aquarium, including daily av evaluation and most recent recording. Limit: 33-35 words, Example format: Good conditions! Temperature is appropriate, liquid level is sufficient, pH is balanced, water TDS is normal. You can press 'Ask GPT' to ask me anything!"})
    



    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages= context
)
    

    response= completion.choices[0].message

    

    response_role= response.role

    response_content= response.content


    processed_response= convert_message_to_api_format(response_role, response_content)


    

    

    api_response.append(processed_response)

    api_response.append(daily_data_message)

    context.pop()




    processed_chat= []


    for i in context:

        

        formatted_message = f'{{"ROLE": "{i["role"]}", "CONTENT": "{i["content"]}"}}'
        processed_chat.append(formatted_message)

    formatted_output = "<br><br><br><br><br><br><br><br>".join(processed_chat)

    #api_response.append(processed_chat)


    


    

    #return HTMLResponse(content=f"<pre>{formatted_output}</pre>")

    return api_response














