from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/localconveyance', methods=['GET', 'POST'])
def local_conveyance():
    if request.method == 'GET':
        # For GET request, show available local conveyance options
        return jsonify({"local_conveyance_options": ["Taxi", "Car Rental", "Bus"]})

    if request.method == 'POST':
        # For POST request, accept user input for local conveyance booking
        data = request.json
        conveyance_type = data.get('conveyance_type')
        destination = data.get('destination')

        # Perform logic to create a local conveyance booking
        return jsonify({
            "message": f"Booking a {conveyance_type} to {destination} has been created."
        }), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)
