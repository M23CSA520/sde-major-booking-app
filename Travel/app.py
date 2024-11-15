from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/travel', methods=['GET'])
def get_travel_options():
    return jsonify({"travel_options": ["Flight", "Train", "Bus"]})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)

