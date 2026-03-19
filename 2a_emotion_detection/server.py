"""
Flask web application for emotion detection using Watson NLP API.
Provides a web interface for users to analyze emotions in text.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_analyzer():
    """
    This code receives the text from the HTML interface and
    runs emotion analysis over it using emotion_detector()
    function. The output returned shows the label and its confidence
    score for the provided text.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Invalid text input. Please try again.", 400

    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text input. Please try again.", 400

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]

    dominant_emotion = max(response, key=response.get)

    return (
        f"For the given statement, the system response is {dominant_emotion}. "
        f"Your anger score is {anger}, disgust score is {disgust}, "
        f"fear score is {fear}, joy score is {joy}, and sadness score is {sadness}."
    )


@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
