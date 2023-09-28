###########################################################
#
#  server02.py
#
#  This server uses the OpenAI API to
#  generate replies to user queries.  This staged
#  server file also implements a chat response that
#  is a simple text html page.
#
#  Usage: > uvicorn server02:api --reload
#
###########################################################

import openai
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated

api = FastAPI()
templates = Jinja2Templates(directory="templates")

chatlog = [{'role': 'system', 
            'content': 'You are a Shakespearean poet who replies in sonnet style.'
            }]

@api.get("/", response_class=HTMLResponse)
async def chat_html(request: Request):
    return templates.TemplateResponse("layout01.html", {"request": request})

@api.post("/")
async def chat(query: Annotated[str, Form()]):

    chatlog.append({'role': 'user', 'content': query})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chatlog,
        temperature=0.5
    )
    reply = response.choices[0].message.content
    chatlog.append({'role': 'bot', 'content': reply})
    return reply