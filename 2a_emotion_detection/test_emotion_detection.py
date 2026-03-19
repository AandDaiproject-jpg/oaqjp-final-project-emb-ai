import unittest
import json
from unittest.mock import Mock, patch
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_emotion_detector_success(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps(
            {
                "emotionPredictions": [
                    {
                        "emotion": {
                            "anger": 0.1,
                            "disgust": 0.05,
                            "fear": 0.05,
                            "joy": 0.6,
                            "sadness": 0.2,
                        }
                    }
                ]
            }
        )
        mock_post.return_value = mock_response

        result = emotion_detector("I love this day!")
        self.assertIsNotNone(result)
        self.assertEqual(result["anger"], 0.1)
        self.assertEqual(result["joy"], 0.6)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_emotion_detector_empty_text(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        result = emotion_detector("")
        self.assertIsNone(result)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_emotion_detector_server_error(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 500
        mock_post.return_value = mock_response

        result = emotion_detector("test")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
