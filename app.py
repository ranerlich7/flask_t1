from flask import Flask, render_template
from news import news_bp
app = Flask(__name__)

app.register_blueprint(news_bp)# , url_prefix='/news')

@app.route("/")
def hello_world():
   return render_template('hello.html')
   # return "<p>Hello, World!</p>"

@app.route("/sports")
def sport():
   return "<p>This is the SPORT section!</p>"

if __name__ == '__main__':
    app.run(debug=True)