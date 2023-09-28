import openai

response = openai.Image.create(
    prompt="Chipmunk with a cowboy hat wearing a t-shirt and a baseball cap",
    n=1,
    size="1024x1024"
)

print(response)