import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    formatted_response = json.loads(response.text)


    # If the response status code is 200, extract the response
    if response.status_code == 200:
        # Access the first element of the 'emotionPredictions' list
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        # Extract each emotion value
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']
        # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
    # If the response status code is 400, set to None
    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        # Find the dominant emotion
        dominant_emotion = None

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }  # Return the response text from the API