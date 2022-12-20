from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'welcome to backend flask api template'


# import blueprint
from .routes.sentiment.controllers_sentiment import blueprint_sentiment
app.register_blueprint(blueprint_sentiment)