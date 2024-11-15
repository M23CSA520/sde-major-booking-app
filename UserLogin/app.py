from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # For GET request, return a welcome message or basic info
        return jsonify({"message": "Welcome to the User Login service. Please POST your credentials."}), 200

    if request.method == 'POST':
        # For POST request, check the credentials
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if username == 'admin' and password == 'password':
            return jsonify({"message": "Login successful", "status": "OK"}), 200
        return jsonify({"message": "Invalid credentials", "status": "ERROR"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
