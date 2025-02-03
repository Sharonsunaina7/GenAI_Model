import random
#list of possible storyline
stories = [
    "Once upon a time, in a magical forest, a {} found a mysterious talking tree",
    "Deep in the ocean, a {} discovered a hidden treasure guarded by a friendly octopus.",
    "One day, a {} built a robot that could talk and dance!",
    "In a faraway space station, a {} met an alien who loved eating chocolates."
]

#ask the kid for a character
character = input("Enter a character (e.g., princess, astronaut, robot, cat):")

#generate a random story
story = random.choice(stories).format(character)

#print the storyline
print("\nHere's your AI-generated story:\n")
print(story)