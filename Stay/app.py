from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/stay', methods=['GET'])
def get_stay_options():
    return jsonify({"stay_options": ["Hotel", "Hostel", "Airbnb"]})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)

