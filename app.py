from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    print("Hi from main on git ")
    return "Hello from a Github pull request!!!!!!"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)
