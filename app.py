from flask import Flask, render_template, request, redirect
from news import news_bp
app = Flask(__name__)

app.register_blueprint(news_bp)# , url_prefix='/news')

@app.route("/", methods=['GET','POST'])
def login():
   if request.method == 'POST':
      print('post called ****')
      name = request.form.get('username')
      pwd = request.form.get('pwd')
      print(f'*** user:{name} passwrod:{pwd} ****')
      return redirect('/news')
      
   else:
      print('get called ****')
      return render_template('login.html')
   # return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)