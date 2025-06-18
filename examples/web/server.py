from flask import Flask, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def serve_index():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'index.html')

if __name__ == '__main__':
    print("Starting frontend server on http://localhost:3000")
    print("Make sure the Snake game API is running on http://localhost:4000")
    app.run(host='0.0.0.0', port=3000) 