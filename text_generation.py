#import the gpt-2 text generation tool from hugging face
from transformers import pipeline

#intialise the next generation pipeline with gpt-2 model
generator = pipeline("text-generation", model="gpt2")  # Specify model explicitly

#provide a starting sentence or prompt
prompt = "Once upon a time, in a land far away"

#generate the text based on the prompt
generated_text = generator(prompt, max_length=50, num_return_sequences=1)

#print the generated text
print(f"Generated_text: {generated_text[0]['generated_text']}")
