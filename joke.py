import random

# List of joke templates
jokes = [
    "Why did the {} go to school? Because it wanted to be a little brighter!",
    "What do you call a {} that sings? A rock star!",
    "Why don’t {} ever get lost? Because they always follow the path of least resistance!"
]

# Ask for a fun word/phrase
word = input("Enter a fun word (e.g., light bulb, banana, AI): ")

# Generate a random joke
joke = random.choice(jokes).format(word)

# Print the joke
print("\nAI-generated joke:")
print(joke)
