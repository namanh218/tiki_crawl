from flask import Flask, render_template
import json
app = Flask(__name__)


@app.route('/')


def index():
    with open('div.json', 'r') as file:
         div = json.load(file)
    return render_template('index.html', div = div)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
 