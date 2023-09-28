import openai
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4, width=76)

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[{
        'role': 'system',
        'content': 'Respond in Shakespearean sonnet style.'
    }, {
        'role': 'user',
        'content': 'How should I relax?'
    }],
    
)

pp.pprint(response.choices[0].message.content)