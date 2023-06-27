from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/contacts')
def contacts():
    return 'Bunty: 8019036609'

@app.route('/about')
def about():
    return 'This is bunty this my flask 1st project thank you.....:)'

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)