import ollama

response = ollama.chat(model="gemma:2b", messages=[{"role": "user", "content": "Hello"}])
print(response)
