#impoet the sentiment analysis pipeline from hugging face transformers lib
from transformers import pipeline

#intializing the sentiment analysis pipeline
sentiment = pipeline("sentiment-analysis")

#defining a sample movie review text
review = "This movie was absolutely mind blowing! The plot twists were amazing."

#running sentiment analysis on the input text
result = sentiment(review)

#extracting and printing the sentiment label and confidence score
print(f"The sentiment is: {result[0]['label']}, Confidence: {result[0]['score']: .2f}")
