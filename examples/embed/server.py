from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    print("Starting embed example server on http://localhost:8080")
    print("Make sure the Snake game server is running on http://localhost:4000")
    app.run(host='0.0.0.0', port=8080) 