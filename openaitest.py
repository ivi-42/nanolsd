import openai

# Apply for an API key from OpenAI
openai.api_key = "YOUR_API_KEY"

# Preprocess your data
with open('input.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
data = [x.strip() for x in data]

#data = [
    #"This is a sample text.",
    #"Here's another sample text.",
    #"And here's one more sample text."
#]

# Define your prompt or task
prompt = "Please generate a story over this text."

# Use the API to fine-tune the model on your data
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
    #context=data
)

# Print the generated text
generated_text = response["choices"][0]["text"]
print(generated_text)
