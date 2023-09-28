import openai

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[{
        'role': 'system',
        'content': 'You are a helpful assistant'
    }, {
        'role': 'user',
        'content': 'Who won the World Series in 2004?'
    }],
    
)

print(response)