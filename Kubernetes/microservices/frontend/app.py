from flask import Flask, render_template
import os
import requests


app = Flask(__name__)

PORT = os.environ.get('PORT', 9000)

BACKEND_URL = os.environ.get('BACKEND_URL', 'http://localhost:8000')



@app.route('/')
def index():
    
    response = requests.get(f'{BACKEND_URL}/api/names')

    data = response.json()

    env = dict(os.environ)

    return render_template('index.html', env = env, data = data['data'])



if __name__ == '__main__':
    app.run(debug=True, port=PORT, host='0.0.0.0')