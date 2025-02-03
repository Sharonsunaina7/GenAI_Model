Welcome to my collection of projects from the **Gen AI Workshop**! This repository showcases various applications of Generative AI, developed over a two-day workshop.

## **Day 1: Introduction to Generative AI & Basics**

### 1. **AI-Generated Poems**
**Description:** This Python script generates creative poems using predefined templates. The user is prompted to enter a fun word, which is then inserted into a randomly selected template to create a unique poem.

- **Concepts Covered:** Random selection, string formatting, user input handling.
- **Project Link:** [poem.py](https://github.com/Sharonsunaina7/GenAI_Model/blob/main/poem.py)

**How It Works:**
1. The script defines a list of poem templates with placeholders.
2. It prompts the user to input a fun word (e.g., "robot," "star," "AI").
3. A random template is selected from the list.
4. The user's word is inserted into the template using string formatting.
5. The final poem is displayed to the user.

*Example Output:*
```
Enter a fun word (e.g., robot, star, AI): star

AI-generated poem:

Twinkle twinkle little star,
AI helps in ways so bright!
```

### 2. **AI-Generated Jokes**
**Description:** This Python script creates humorous jokes based on user input. The user provides a fun word, which is inserted into a randomly chosen joke template, resulting in a personalized joke.

- **Concepts Covered:** Random selection, string formatting, interactive user experience.
- **Project Link:** [joke.py](https://github.com/Sharonsunaina7/GenAI_Model/blob/main/joke.py)

**How It Works:**
1. The script defines a list of joke templates with placeholders.
2. It prompts the user to input a fun word (e.g., "banana," "light bulb," "AI").
3. A random template is selected from the list.
4. The user's word is inserted into the template using string formatting.
5. The final joke is displayed to the user.

*Example Output:*
```
Enter a fun word (e.g., banana, light bulb, AI): banana

AI-generated joke:

Why did the banana go to school? Because it wanted to be a little brighter!
```

### 3. **AI-Generated Stories**
**Description:** This Python script crafts short stories by incorporating user-provided words into predefined story templates, resulting in engaging and personalized narratives.

- **Concepts Covered:** Random selection, string formatting, user input handling.
- **Project Link:** [story.py](https://github.com/Sharonsunaina7/GenAI_Model/blob/main/story.py)

**How It Works:**
1. The script defines a list of story templates with placeholders.
2. It prompts the user to input a fun word (e.g., "dragon," "spaceship," "AI").
3. A random template is selected from the list.
4. The user's word is inserted into the template using string formatting.
5. The final story is displayed to the user.

*Example Output:*
```
Enter a fun word (e.g., dragon, spaceship, AI): dragon

AI-generated story:

Once upon a time, in a land far away, a dragon discovered the magic of AI and transformed the world forever.
```

## **Day 2: Advanced Applications of Generative AI**

### 4. **AI-Powered Text Generation**
**Description:** This Python script utilizes the GPT-2 model to generate coherent text based on a user-provided prompt.

- **Concepts Covered:** Natural Language Processing (NLP), text generation using pre-trained models.
- **Project Link:** [text_generation.py](https://github.com/Sharonsunaina7/GenAI_Model/blob/main/text_generation.py)

**How It Works:**
1. The script initializes a text generation pipeline using the GPT-2 model from Hugging Face's Transformers library.
2. It prompts the user to input a starting sentence or prompt.
3. The model generates text continuation based on the provided prompt.
4. The generated text is displayed to the user.

*Example Output:*
```
Enter a starting sentence: Once upon a time, in a land far away

Generated text: Once upon a time, in a land far away, there lived a wise old king who ruled his kingdom with kindness and justice. One day, he decided to...
```

### 5. **Sentiment Analysis of Reviews**
**Description:** This Python script analyzes the sentiment of multiple user-provided reviews, determining whether each review is positive, negative, or neutral.

- **Concepts Covered:** Sentiment analysis, batch processing of text data.
- **Project Link:** [review_analysis.py](https://github.com/Sharonsunaina7/GenAI_Model/blob/main/review_analysis.py)

**How It Works:**
1. The script initializes a sentiment analysis pipeline using a pre-trained model.
2. It defines a list of reviews to be analyzed.
3. The model processes each review and outputs the sentiment label (e.g., positive, negative) and confidence score.
4. The results are displayed to the user.

*Example Output:*
```
Review 1: I absolutely loved this film!
Sentiment: POSITIVE, Confidence: 0.99

Review 2: It was a waste of time.
Sentiment: NEGATIVE, Confidence: 0.98

Review 3: Not bad, but could have been better.
Sentiment: NEUTRAL, Confidence: 0.75
```

### 6. **Named Entity Recognition (NER)**
**Description:** This Python script extracts named entities (such as people, locations, organizations, and more) from user-provided text using a pre-trained NLP model.

- **Concepts Covered:** Named Entity Recognition (NER), NLP fundamentals, text processing.
- **Project Link:** [ner.py](https://github.com/Sharonsunaina7/GenAI_Model/blob/main/ner.py)

**How It Works:**
1. The script initializes a Named Entity Recognition (NER) pipeline using a pre-trained model.
2. It prompts the user to input a sentence or paragraph.
3. The model identifies named entities in the text and classifies them (e.g., PERSON, LOCATION, ORGANIZATION).
4. The extracted entities are displayed along with their categories.

*Example Output:*
```
Enter a sentence: Elon Musk founded SpaceX in California.

Extracted Entities:
- Elon Musk (PERSON)
- SpaceX (ORGANIZATION)
- California (LOCATION)
```

### 7. **AI-Based Sentiment Analysis**
**Description:** This Python script determines the sentiment (positive, negative, or neutral) of user-provided text using a pre-trained deep learning model.

- **Concepts Covered:** Sentiment classification, NLP pipeline usage.
- **Project Link:** [sentiment_analysis.py](https://github.com/Sharonsunaina7/GenAI_Model/blob/main/sentiment_analysis.py)

**How It Works:**
1. The script initializes a sentiment analysis model using Hugging Face's Transformers library.
2. It prompts the user to enter a sentence.
3. The model processes the sentence and outputs the sentiment label along with a confidence score.
4. The result is displayed to the user.

*Example Output:*
```
Enter a sentence: The product quality is amazing!

Sentiment: POSITIVE, Confidence: 0.98
```

---

These projects demonstrate various applications of Generative AI, from text generation to sentiment analysis and Named Entity Recognition. Feel free to explore, modify, and experiment with these scripts to create your own AI-powered applications. Happy coding! 
