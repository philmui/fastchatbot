import openai

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[{
        'role': 'system',
        'content': 'You are a helpful assistant'
    }, {
        'role': 'assistant',
        'content': 'The Boston Red Sox won the World Series in 2004',
    }, {
        'role': 'user',
        'content': 'Who was on the team?'
    }],
    
)

print(response)