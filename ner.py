#import the named entity recognition tool from Hugging Face
from transformers import pipeline

#intialize the NER pipeline with BERT model
ner = pipeline('ner')

#provide the text to analyze for named entities
text = "Barack Obama was born in Hawaii and became the 44th President of the United States."

#run NER to detect named entities
entities = ner(text)

#print the detected entities
for entity in entities:
    print(f"Entity: {entity['word']}, label: {entity['entity']}, score: {entity['score']: .2f}")