import openai

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[{
        'role': 'system',
        'content': 'You are a helpful assistant'
    }, {
        'role': 'user',
        'content': 'How should I relax?'
    }],
    
)

print(response)