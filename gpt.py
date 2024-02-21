from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()


client = OpenAI(
  api_key=os.environ.get("AIAPIKEY"),
)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)

content = response.choices[0].message.content
print(content)