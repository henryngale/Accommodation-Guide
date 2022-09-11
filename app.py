from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route('/', methods=['POST', 'GET'])
def home():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
