''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Create a Flask app instance
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    '''Analyze the emotions in a given text.

    Retrieves text from the request arguments and uses the `emotion_detector`
    function to analyze it. Returns the analysis as a formatted string.

    Returns:
        str: A message with the emotion scores and the dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    # Extract emotion scores and the dominant emotion
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with the emotion analysis
    output = (f"For the given statement, the system response is 'anger': {anger}, "
              f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
              f"The dominant emotion is {dominant_emotion}.")
    return output


@app.route("/")
def render_index_page():
    '''Render the index page.

    Returns:
        HTML: The content of the index page.
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
