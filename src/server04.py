###########################################################
#
#  server03.py
#
#  This server uses the OpenAI API to
#  generate replies to user queries.  This staged
#  server file also implements a chat query page with
#  real simple html form inputs.
#
#  Usage: > uvicorn server03:api --reload
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
chat_responses = []

@api.get("/", response_class=HTMLResponse)
async def chat_html(request: Request):
    return templates.TemplateResponse("home02.html", {"request": request, "chat_response": chat_responses})

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