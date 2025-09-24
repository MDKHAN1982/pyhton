from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')

def index():
    return '<H1> Jaffar khan in Flask frame work python devloper </H1>'


if __name__ == "__main__":
    app.run(debug=True)