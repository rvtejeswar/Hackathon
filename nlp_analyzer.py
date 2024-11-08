import nltk
from transformers import pipeline
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download necessary NLTK data (run this only once)
nltk.download('vader_lexicon')

# Initialize NLP models
sentiment_analyzer = SentimentIntensityAnalyzer()
emotion_analyzer = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

def analyze_conversation(text):
    """
    Analyze the text of a conversation to evaluate social engagement and mood.
    Parameters:
        text (str): The conversation or message content.
    Returns:
        dict: Analysis results including sentiment and emotions.
    """
    # Sentiment Analysis
    sentiment_score = sentiment_analyzer.polarity_scores(text)
    
    # Emotion Detection
    emotion = emotion_analyzer(text)[0][0]
    
    return {
        "sentiment": sentiment_score,
        "emotion": emotion['label'],
        "emotion_score": emotion['score']
    }
