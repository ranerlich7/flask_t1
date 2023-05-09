
from flask import Flask, Blueprint, render_template
print(f"my __name__ is:{__name__}")
news_bp = Blueprint('news', __name__,url_prefix='/news', template_folder='templates/news7')


@news_bp.route("/")
def news():
   return render_template('main_news.html')

@news_bp.route("/world")
def world():
   return render_template('world_news.html')

from flask import Flask, Blueprint, jsonify

app = Flask(__name__)
api_bp = Blueprint('api', __name__)


