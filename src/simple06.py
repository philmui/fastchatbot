import openai

chatlog = []

while True:
    
    query = input("Your query : ")
    if query.casefold() == "exit": break
    
    chatlog.append({'role': 'user', 'content': query})
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chatlog,
        temperature=0.5
    )
    reply = response.choices[0].message.content
    chatlog.append({'role': 'bot', 'content': reply})
    print(reply)