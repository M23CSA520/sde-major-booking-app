from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/conveyance', methods=['GET'])
def get_conveyance_options():
    return jsonify({"conveyance_options": ["Taxi", "Bike", "Bus"]})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)

