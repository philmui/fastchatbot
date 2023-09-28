###########################################################
#
#  server01.py
#
#  This server uses the OpenAI API to
#  generate replies to user queries.
#
#  Usage: > uvicorn server01:api --reload
#
###########################################################

import openai
from fastapi import FastAPI, Form
from typing import Annotated

api = FastAPI()

chatlog = [{'role': 'system', 
            'content': 'You are a Shakespearean poet who replies in sonnet style.'
            }]

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