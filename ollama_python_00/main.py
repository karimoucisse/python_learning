# from openai import OpenAI

# client = OpenAI(
#     base_url="http://localhost:11434/v1",  # Ollama en local
#     api_key="ollama",                       # ignorée mais requise
# )

# response = client.chat.completions.create(
#     model="llama3.2",
#     messages=[
#         {"role": "user", "content": "What is the name of the fastest man in the world?"}
#     ],
# )

# print(response.choices[0].message.content)

from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'Pourquoi le ciel est-il bleu?',
  },
])
print(response['message']['content'])
