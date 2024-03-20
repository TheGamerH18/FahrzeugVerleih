from flask import Flask, request, jsonify
from fahrzeug import Fahrzeug
from inspektion import Inspektion
from mietvertrag import Mietvertrag
from mitarbeiter import Mitarbeiter
import mysql.connector

app = Flask(__name__)

# Define your API key
API_KEY = 'your_api_key_here'

# MySQL connection parameters
db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database'
}


def get_db_connection():
    return mysql.connector.connect(**db_config)


# Authentication decorator
def requires_auth(f):
    def decorated(*args, **kwargs):
        api_key = request.headers.get('X-API-KEY')
        if not api_key or api_key != API_KEY:
            return jsonify({'error': 'Unauthorized access'}), 401
        return f(*args, **kwargs)

    return decorated


@app.route('/fahrzeuge', methods=['GET'])
@requires_auth
def get_all_fahrzeuge():
    connection = get_db_connection()
    fahrzeuge = Fahrzeug.get_all(connection)
    connection.close()
    return jsonify([f.__dict__ for f in fahrzeuge])


@app.route('/fahrzeuge/<int:fahrzeug_id>', methods=['GET'])
@requires_auth
def get_fahrzeug(fahrzeug_id):
    connection = get_db_connection()
    fahrzeug = Fahrzeug.read(connection, fahrzeug_id)
    connection.close()
    if fahrzeug:
        return jsonify(fahrzeug.__dict__)
    else:
        return jsonify({'error': 'Fahrzeug not found'}), 404


@app.route('/inspektionen', methods=['GET'])
@requires_auth
def get_all_inspektionen():
    connection = get_db_connection()
    inspektionen = Inspektion.get_all(connection)
    connection.close()
    return jsonify([i.__dict__ for i in inspektionen])


@app.route('/inspektionen/<int:inspektion_id>', methods=['GET'])
@requires_auth
def get_inspektion(inspektion_id):
    connection = get_db_connection()
    inspektion = Inspektion.read(connection, inspektion_id)
    connection.close()
    if inspektion:
        return jsonify(inspektion.__dict__)
    else:
        return jsonify({'error': 'Inspektion not found'}), 404


@app.route('/mietvertraege', methods=['GET'])
@requires_auth
def get_all_mietvertraege():
    connection = get_db_connection()
    mietvertraege = Mietvertrag.get_all(connection)
    connection.close()
    return jsonify([m.__dict__ for m in mietvertraege])


@app.route('/mietvertraege/<int:mietvertrag_id>', methods=['GET'])
@requires_auth
def get_mietvertrag(mietvertrag_id):
    connection = get_db_connection()
    mietvertrag = Mietvertrag.read(connection, mietvertrag_id)
    connection.close()
    if mietvertrag:
        return jsonify(mietvertrag.__dict__)
    else:
        return jsonify({'error': 'Mietvertrag not found'}), 404


@app.route('/mitarbeiter', methods=['GET'])
@requires_auth
def get_all_mitarbeiter():
    connection = get_db_connection()
    mitarbeiter = Mitarbeiter.get_all(connection)
    connection.close()
    return jsonify([m.__dict__ for m in mitarbeiter])


@app.route('/mitarbeiter/<int:mitarbeiter_id>', methods=['GET'])
@requires_auth
def get_mitarbeiter(mitarbeiter_id):
    connection = get_db_connection()
    mitarbeiter = Mitarbeiter.read(connection, mitarbeiter_id)
    connection.close()
    if mitarbeiter:
        return jsonify(mitarbeiter.__dict__)
    else:
        return jsonify({'error': 'Mitarbeiter not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
