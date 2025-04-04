import os
from llama_stack_client import LlamaStackClient

# Get the model ID from the environment variable
INFERENCE_MODEL = os.environ.get("INFERENCE_MODEL")

# Check if the environment variable is se
if INFERENCE_MODEL is None:
    raise ValueError("The environment variable 'INFERENCE_MODEL' is not set.")

# Initialize the client
client = LlamaStackClient(base_url="http://localhost:8321")

# Create a chat completion reques
response = client.inference.chat_completion(
    messages=[
        {"role": "system", "content": "You are a friendly assistant."},
        {"role": "user", "content": "Write a two-sentence poem about llama."},
    ],
    model_id=INFERENCE_MODEL,
)

# Print the response
print(response.completion_message.content)