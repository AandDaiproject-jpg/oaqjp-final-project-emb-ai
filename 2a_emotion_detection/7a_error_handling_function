import json
import requests


def emotion_detector(text_to_analyse):
    """
    Analyzes the emotion of the given text using Watson NLP API.

    Args:
        text_to_analyse (str): The text to analyze for emotions

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:
        return None
    elif response.status_code == 500:
        return None

    formatted_response = json.loads(response.text)
    emotion_predictions = formatted_response["emotionPredictions"][0]["emotion"]

    dominant_emotion = max(emotion_predictions, key=emotion_predictions.get)
    emotion_predictions["dominant_emotion"] = dominant_emotion

    return emotion_predictions
