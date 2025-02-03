from transformers import pipeline
#intializing the sentiment analysis pipeline
sentiment = pipeline("sentiment-analysis")

#list of multiple reviews analyse
reviews = [
    "I absolutely loved this film!",
    "It was a waste of time.",
    "Not bad, but could have been better."
]
#running sentiment analysis on all reviews
results = sentiment(reviews)

#extracting and printing the sentiment label and confidence score
for i, res in enumerate(results):
    print(f"Review {i+1}: {reviews[i]}")
    print(f"Sentiment: {res['label']}, Confidence: {res['score']: .2f}\n")