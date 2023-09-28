###########################################################
#
#  dalle02.py
#
#  This server uses the OpenAI API to
#  generate images based on user queries. 
#
#  Usage: > uvicorn dalle02:api --reload
#
###########################################################

import openai
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated
from mangum import Mangum

api = FastAPI()
handler = Mangum(api)

templates = Jinja2Templates(directory="templates")

chatlog = [{'role': 'system', 
            'content': 'You are a Shakespearean poet who replies in sonnet style.'
            }]
chat_responses = []

@api.get("/", response_class=HTMLResponse)
async def chat_html(request: Request):
    return templates.TemplateResponse("home02.html", {"request": request})

@api.post("/", response_class=HTMLResponse)
async def chat(request: Request, query: Annotated[str, Form()]):

    chatlog.append({'role': 'user', 'content': query})
    chat_responses.append(query)
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chatlog,
        temperature=0.5
    )
    bot_response = response.choices[0].message.content
    chatlog.append({'role': 'assistant', 'content': bot_response})
    chat_responses.append(bot_response)
    return templates.TemplateResponse("home02.html", {"request": request, "chat_responses": chat_responses})

@api.get("/image", response_class=HTMLResponse)
async def image_html(request: Request):
    return templates.TemplateResponse("image.html", {"request": request})

@api.post("/image", response_class=HTMLResponse)
async def create_image(request: Request, query: Annotated[str, Form()]):

    response = openai.Image.create(
        prompt=query,
        n=1,
        size="512x512"
    )
    image_url = response.data[0].url
    return templates.TemplateResponse("image.html", {"request": request, "image_url": image_url})