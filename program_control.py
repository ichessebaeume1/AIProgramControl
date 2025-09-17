from openai import OpenAI
from pydantic import BaseModel, Field
import json
import subprocess

task = input("Command: ")

client = OpenAI(
    api_key="API_KEY",
)

class ApplicationName(BaseModel):
    a: list[str] = Field(..., description='The names of the applications mentioned by the user which he wants to open.')

messages = [
    {
        'role': 'user',
        'content': f'What application does the User want to open with this request: {task}.'
    }
]

response = client.chat.completions.parse(
    messages=messages,
    model="gpt-5",
    response_format=ApplicationName,
    timeout=10
)

apps = json.loads(response.choices[0].message.content)['a']   # {'a': ['explorer']}

for app in apps:
    print(f"Trying to open {app.lower()}...")
    command = f"start {app.lower()}"

    try:
        subprocess.run(command, shell=True)
    except FileNotFoundError:
        print(f"Windows could not find {app}.")
    except Exception as e:
        print(f"Unknown Error: {e}")
