import random

#import poem templates
poems = [
    "Roses are red, violets are blue,\n{} is awesome, and so are you!",
    "Twinkle twinkle little {}, \nAI helps in ways so bright!",
    "{} is learning, coding away, \nMaking new things every day!"
]
#ask for a word/phrase
word = input("Enter a fun word(e.g., robot, star, AI:)")

#generate a random poem
poem = random.choice(poems).format(word)

#print the poem lines
print("\nAI-generated poem:\n")
print(poem)