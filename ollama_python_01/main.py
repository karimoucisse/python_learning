from ollama import chat

messages = [
	{
		'role': 'system',
		'content': '''
			give shot response, use exemple in each response
		'''
	},
	{
		'role': 'user',
		'content': '''
			why is the skye blue?
		'''
	}
]

response_1 = chat(model='llama3.2', messages= messages)

messages.append(
	{
		'role': response_1.message.role,
		'content': response_1.message.content
	}
)

messages.append(
	{
		'role': 'user',
		'content': '''
			Can you explain in slightly more detail??
		'''
	}
)

response_2 = chat(model='llama3.2', messages= messages)

print(f"Role1: {response_1['message']['role']}")
print(f"Content1: {response_1['message']['content']}\n")
print(f"{'----' * 50 + '\n'} ")
print(f"Role2: {response_2['message']['role']}")
print(f"Content2: {response_2['message']['content']}")
