from flask import Blueprint, request, make_response, jsonify
import os

# utils
import joblib
from .utils import processTeks


from ...utilities import *

blueprint_facebook_sentiment = Blueprint('blueprint_facebook_sentiment', __name__)

models_path = os.path.abspath(os.path.join(__file__, "../model/")) + "/"

model = joblib.load(os.path.join(models_path, "fb_sentiment.pkl"))


@blueprint_facebook_sentiment.route("/api/sentiment/facebook", methods=["GET"])
def FacebookSentiment():
    try:
        data = request.json
        
        prediction = model.predict([processTeks(data['text'])])
        
        hasil_prediksi = ""
        if prediction == 0:
            hasil_prediksi = "negative"
        elif prediction == 1:
            hasil_prediksi = "positive"
            
        return make_response(jsonify({'status_code': '200', 'prediksi': hasil_prediksi}))
    except Exception as e:
        return bad_request(e)
    
