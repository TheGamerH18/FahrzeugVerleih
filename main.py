from flask import Flask, request, jsonify

app = Flask(__name__)

# Hardcoded API key for authentication
API_KEY = "token"

# Dummy data for demonstration
data = {"1": {"name": "John", "age": 30},
        "2": {"name": "Alice", "age": 25},
        "3": {"name": "Bob", "age": 35}}


# Authentication decorator
def require_api_key(view_function):
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get("Authorization")
        if api_key and api_key == f"Bearer {API_KEY}":
            return view_function(*args, **kwargs)
        else:
            return jsonify({"error": "Unauthorized"}), 401

    return decorated_function


# Route to get all data
@app.route('/data', methods=['GET'])
@require_api_key
def get_data():
    return jsonify(data)


# Route to get data by id
@app.route('/data/<id>', methods=['GET'])
@require_api_key
def get_data_by_id(id):
    if id in data:
        return jsonify(data[id])
    else:
        return jsonify({"error": "Not Found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
