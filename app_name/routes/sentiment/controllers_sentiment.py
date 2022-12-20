from flask import Blueprint, request
import os

# utils
import joblib
from ...utilities import bad_request, success, processTeks

blueprint_sentiment = Blueprint('blueprint_sentiment', __name__)

facebook_models_path = os.path.abspath(os.path.join(__file__, "../model/")) + "/"

facebook_model = joblib.load(os.path.join(facebook_models_path, "fb_sentiment_svm.pkl"))


@blueprint_sentiment.route("/api/sentiment/facebook", methods=["POST"])
def FacebookSentiment():
    """Indonesia facebook caption post sentiment analysis
    
    Input:
        {
            "text": *args
        }
        params:
            args (str): facebook caption text in indonesia language

    Returns:
        json: sentiment result (negative/positive)
    """
    try:
        data = request.json
        
        prediction = facebook_model.predict([processTeks(data['text'])])
        
        hasil_prediksi = ""
        if prediction == 0:
            hasil_prediksi = "negative"
        elif prediction == 1:
            hasil_prediksi = "positive"
            
        return success(hasil_prediksi)
    except Exception as e:
        return bad_request(e)
    
news_models_path = os.path.abspath(os.path.join(__file__, "../model/")) + "/"

news_model = joblib.load(os.path.join(news_models_path, "news_sentiment_svm.pkl"))

@blueprint_sentiment.route("/api/sentiment/news", methods=["POST"])
def NewsSentiment():
    """Indonesia news content and title sentiment analysis
    
    Input:
        {
            "text": *args
        }
        params:
            args (str): news content text in indonesia language

    Returns:
        json: sentiment result (negative/positive/netral)
    """
    try:
        data = request.json
        
        prediction = news_model.predict([processTeks(data['text'])])
        
        hasil_prediksi = ""
        if prediction == 0:
            hasil_prediksi = "negative"
        elif prediction == 1:
            hasil_prediksi = "netral"
        elif prediction == 2:
            hasil_prediksi = "positive"
            
        return success(hasil_prediksi)
    except Exception as e:
        return bad_request(e)
