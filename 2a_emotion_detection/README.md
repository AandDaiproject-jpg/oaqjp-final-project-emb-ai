# Emotion Detector

An AI-based web application that detects emotions from text using Watson NLP API.

## Features

- Real-time emotion detection from user input
- Analyzes five emotions: anger, disgust, fear, joy, sadness
- Identifies the dominant emotion with confidence scores
- Web-based interface built with Flask
- Error handling for invalid inputs

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd 2a_emotion_detection
```

2. Create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Flask application:
```bash
python server.py
```

Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
2a_emotion_detection/
├── EmotionDetection/
│   ├── __init__.py           # Package initialization
│   └── emotion_detection.py  # Emotion detection logic
├── templates/
│   └── index.html           # Web interface
├── static/
│   └── mywebscript.js       # Frontend JavaScript
├── test_emotion_detection.py # Unit tests
├── server.py                 # Flask application
└── requirements.txt          # Dependencies
```

## API

### Endpoint: `/emotionDetector`

Query Parameters:
- `textToAnalyze` (string): The text to analyze

Response:
- Returns emotion scores and dominant emotion
- Returns HTTP 400 for invalid input

## Testing

Run unit tests:
```bash
python -m unittest test_emotion_detection.py
```

## Static Code Analysis

Run pylint for code quality check:
```bash
pylint server.py
```
