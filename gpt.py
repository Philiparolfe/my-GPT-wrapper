from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()


client = OpenAI(
  api_key=os.environ.get("AIAPIKEY"),
)

class GPT:
    def __init__(self) -> None:
        self.client = OpenAI(api_key=os.environ.get("AIAPIKEY"))
    def chat_completion(self, user_content):
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{user_content}"}
        ]
        )
        return f"{response.choices[0].message.content}"
    
    def custom_GPT(self, sys_prompt, user_content):
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"{sys_prompt}"},
            {"role": "user", "content": f"{user_content}"}
        ]
        )
        return f"{response.choices[0].message.content}"

# Test    
GPT_instance = GPT()
print(GPT_instance.chat_completion(user_content="hello"))