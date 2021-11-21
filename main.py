from flask import Flask, jsonify

app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/heath_check')
def health_check():
    return jsonify({'code': 200, 'msg': 'Server running!'}, 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2080)
