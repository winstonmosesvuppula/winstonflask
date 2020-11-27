from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/test1")
def test1():
    return render_template('test1.html')

@app.route("/dashboard")
def dashboard():
    return render_template('/dashboard/index.html')

if __name__ == '__main__':
    app.run()
