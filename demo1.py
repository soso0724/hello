from flask import Flask

app=Flask(__name__)

@app.route("/")

def index1():
    return "Don't worry, everything gonna be ok ^_^"

if __name__ == "__main__":
    app.run(port=5002,debug=True)
