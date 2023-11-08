from flask import Flask
from waitress import serve
from concurrent.futures import thread

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello there from Pritesh!! "

if __name__ == "__main__":
     serve(app, host='0.0.0.0',port=50100, threads=2, url_prefix="/my-app") 