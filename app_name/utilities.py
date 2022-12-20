from flask import jsonify, make_response

import re 
import emoji 
import string
from string import punctuation
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# bad request
def bad_request(description=""):
	return make_response(jsonify({'description':f"{description}",'error': 'Bad Request','status_code':400}), 400)

def success(message, status_code=200):
    return make_response(jsonify({'status_code': status_code, 'message': message}), status_code)

def processTeks(teks):
    def text_cleaning(teks):
        teks = emoji.demojize(teks)
        teks = teks.replace('·', '')
        teks = teks.replace('Lihat Terjemahan', '')
        teks = teks.replace('Beri Nilai Terjemahan', '')
        teks = re.sub(r'\&\w*;', '', teks)
        teks = re.sub('@[^\s]+','',teks)
        teks = re.sub(r'\$\w*', '', teks)
        teks = teks.lower()
        teks = re.sub(r'https?:\/\/.*\/\w*', '', teks)
        teks = re.sub(r'#\w*', '', teks)
        teks = re.sub(r'[' + punctuation.replace('@', '') + ']+', ' ', teks)
        teks = re.sub(r'\b\w{1,2}\b', '', teks)
        teks = re.sub(r'\s\s+', ' ', teks)
        teks = re.sub(r'2022', ' ', teks)
        teks = re.sub(r'2021', ' ', teks)
        teks = re.sub(r'2020', ' ', teks)
        teks = re.sub(r'000', ' ', teks)
        teks = re.sub(r'0', ' ', teks)
        teks = re.sub(r'1', ' ', teks)
        teks = re.sub(r'2', ' ', teks)
        teks = re.sub(r'3', ' ', teks)
        teks = re.sub(r'4', ' ', teks)
        teks = re.sub(r'5', ' ', teks)
        teks = re.sub(r'6', ' ', teks)
        teks = re.sub(r'7', ' ', teks)
        teks = re.sub(r'8', ' ', teks)
        teks = re.sub(r'9', ' ', teks)
        teks = teks.lstrip(' ') 
        teks = ''.join(c for c in teks if c <= '\uFFFF') 
        return teks
    
    def stopword_removal(raw_text):
        list_stop_words = StopWordRemoverFactory().get_stop_words()
        # Check characters to see if they are in punctuation
        nopunc = [char for char in list(raw_text) if char not in string.punctuation]
        # Join the characters again to form the string.
        nopunc = ''.join(nopunc)
        # Now just remove any stopwords
        remove_stopword = [word for word in nopunc.lower().split() if word.lower() not in list_stop_words]
        join_teks = " ".join(remove_stopword)
        return join_teks
    
    bersih_teks = text_cleaning(teks)
    remove_stopword = stopword_removal(bersih_teks)
    return remove_stopword