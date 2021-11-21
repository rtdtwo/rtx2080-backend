from flask import Flask, jsonify
import bl_mock as bl

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def root():
    return "This is the root server route and does nothing."

@app.route('/heath_check')
def health_check():
    return jsonify({'code': 200, 'msg': 'Server running!'}, 200)


@app.route('/things')
def get_things():
    result = bl.get_things();
    return jsonify(result), result['code']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2080)
