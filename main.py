import json
import re
from flask import Flask, jsonify, request
from flask_cors import CORS
import bl as bl

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)


@app.route('/')
def root():
    return "This is the root server route and does nothing."


@app.route('/heath_check')
def health_check():
    return jsonify({'code': 200, 'msg': 'Server running!'}, 200)


@app.route('/things')
def get_things():
    result = bl.get_things()
    return jsonify(result), result['code']


@app.route('/things/<thing_id>/services')
def get_services(thing_id):
    result = bl.get_services(thing_id)
    return jsonify(result), result['code']


@app.route('/relationships')
def get_relationships():
    result = bl.get_relationships()
    return jsonify(result), result['code']


@app.route('/things', methods=['POST'])
def create_thing():
    if not request.is_json:
        return jsonify({'code': 400, 'msg': 'No data provided'}), 400

    data = request.json
    result = bl.create_thing(data)
    return jsonify(result), result['code']


@app.route('/services', methods=['POST'])
def create_service():
    if not request.is_json:
        return jsonify({'code': 400, 'msg': 'No data provided'}), 400
    data = request.json
    result = bl.create_service(data)
    return jsonify(result), result['code']


@app.route('/app/<app_id>/run', methods=['POST'])
def run_app(app_id):
    result = bl.run_app(app_id)
    return jsonify(result), result['code']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2080)
