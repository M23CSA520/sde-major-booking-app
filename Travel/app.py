from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/travel', methods=['GET', 'POST'])
def travel_options():
    if request.method == 'GET':
        # For GET request, show available travel options
        return jsonify({"travel_options": ["Flight", "Train", "Bus"]})

    if request.method == 'POST':
        # For POST request, accept user input for travel booking
        data = request.json
        destination = data.get('destination')
        travel_type = data.get('travel_type')

        # Perform logic to create a travel booking
        return jsonify({
            "message": f"Booking for {destination} with {travel_type} has been created."
        }), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
