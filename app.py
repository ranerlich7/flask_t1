from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
   return "<p>Hello, World!</p>"

@app.route("/news")
def hello_world():
   return "<p>This is the NEWS section!</p>"

@app.route("/news")
def hello_sport():
   return "<p>This is the SPORT section!</p>"

if __name__ == '__main__':
    app.run(debug=True)