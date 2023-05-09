from flask import Flask
from news import news_bp
app = Flask(__name__)

app.register_blueprint(news_bp)# , url_prefix='/news')

@app.route("/")
def hello_world():
   return "<p>Hello, World!</p>"

@app.route("/news")
def news():
   return "<p>This is the NEWS section!</p>"

@app.route("/sports")
def sport():
   return "<p>This is the SPORT section!</p>"

if __name__ == '__main__':
    app.run(debug=True)