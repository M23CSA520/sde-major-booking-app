from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/stay', methods=['GET', 'POST'])
def stay_options():
    if request.method == 'GET':
        # For GET request, show available stays (hotels)
        return jsonify({"stay_options": ["Hotel A", "Hotel B", "Hotel C"]})

    if request.method == 'POST':
        # For POST request, accept user input for stay booking
        data = request.json
        hotel = data.get('hotel')
        check_in = data.get('check_in')
        check_out = data.get('check_out')

        # Perform logic to create a stay booking
        return jsonify({
            "message": f"Booking at {hotel} from {check_in} to {check_out} has been created."
        }), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
