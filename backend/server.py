from typing import Union
from openai import OpenAI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import os


load_dotenv()  # Load environment variables from .env file

api_key = os.getenv("OPENAI_API_KEY")


app = FastAPI()

client = OpenAI()

context= [{"role": "system", "content": "You are a helpful pet shop aquarium assistant, You are a part of an IoT system where Raspberry Pi collects aquarium data using sensors and sends it to you. You need to analyze the data and provide the status whe asked to, or just assist with general questions. Each time u will get list of messages as a history of conversation/data, and u need to assist based on the data history and saved knowledge."}]





    




@app.get("/")
def read_root():
    
    
    request= input("Enter request:")

    role= "user"


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

    

    context.append(processed_response)




    processed_chat= []


    for i in context:

        

        formatted_message = f'{{"ROLE": "{i["role"]}", "CONTENT": "{i["content"]}"}}'
        processed_chat.append(formatted_message)

    formatted_output = "<br><br><br><br><br><br><br><br>".join(processed_chat)


    


    

    return HTMLResponse(content=f"<pre>{formatted_output}</pre>")















def convert_message_to_api_format(response_role, response_content):
    
    formatted_message = { "role": response_role,  "content": response_content  }
    
    
    return formatted_message