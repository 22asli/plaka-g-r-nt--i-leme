from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def index():
    return ("lfshlfhdf")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)