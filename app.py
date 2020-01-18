from flask import Flask


app = Flask(__name__)
# ba dastore pip freeze > requirements.txt
@app.route('/')
def index():
    return "homepage"