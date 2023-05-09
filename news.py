
from flask import Flask, Blueprint, jsonify
print(f"my __name__ is:{__name__}")
news_bp = Blueprint('news', __name__)


@news_bp.route("/news")
def news():
   return "<p>This is the NEWS section!</p>"

@news_bp.route("/news/world")
def world():
   return "<p>This is the WORLD NEWS section!</p>"

from flask import Flask, Blueprint, jsonify

app = Flask(__name__)
api_bp = Blueprint('api', __name__)

@api_bp.route('/hello')
def hello():
    return jsonify({'message': 'Hello, World!'})

