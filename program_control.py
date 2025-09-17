from openai import OpenAI
from pydantic import BaseModel, Field
import json

task = input("")

client = OpenAI(
    api_key="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",
)

class ApplicationName(BaseModel):
    a: list[str] = Field(..., description='The names of the applications or files mentioned by the user which he want to open.')

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
)

app = json.loads(response.choices[0].message.content)["a"].lower()
print(app)
