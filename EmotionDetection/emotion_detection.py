import requests
import json

def emotion_detector(text_to_analyse): 
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = input_json, headers=Headers)
    formatted_response = response.json()
    emotion_predictions = formatted_response['emotionPredictions']
    emotions = emotion_predictions[0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    result = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
                            'sadness': emotions.get('sadness', 0),
            'dominant_emotion': dominant_emotion
                }
    return result

    