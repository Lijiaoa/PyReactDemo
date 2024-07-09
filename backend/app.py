import os
from flask import Flask, send_from_directory, jsonify
from flask_static_digest import FlaskStaticDigest
from flask_cors import CORS

app = Flask(__name__, static_folder=os.path.join('client', 'build/static'))
flask_static_digest = FlaskStaticDigest(app)
CORS(app)

@app.route('/')
def serve_react_app():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "Hello from the backend!"}
    return jsonify(data)

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
