from flask import Flask, request, jsonify
from fahrzeug import Fahrzeug
from inspektion import Inspektion
from mietvertrag import Mietvertrag
from mitarbeiter import Mitarbeiter
import mysql.connector

app = Flask(__name__)

# MySQL connection parameters
db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/fahrzeuge', methods=['POST'])
def create_fahrzeug():
    data = request.get_json()
    connection = get_db_connection()
    fahrzeug_id = Fahrzeug.create(connection, **data)
    connection.close()
    return jsonify({'FahrzeugID': fahrzeug_id}), 201

@app.route('/fahrzeuge/<int:fahrzeug_id>', methods=['GET'])
def get_fahrzeug(fahrzeug_id):
    connection = get_db_connection()
    fahrzeug = Fahrzeug.read(connection, fahrzeug_id)
    connection.close()
    if fahrzeug:
        return jsonify(fahrzeug.__dict__)
    else:
        return jsonify({'error': 'Fahrzeug not found'}), 404

@app.route('/inspektionen', methods=['POST'])
def create_inspektion():
    data = request.get_json()
    connection = get_db_connection()
    inspektion_id = Inspektion.create(connection, **data)
    connection.close()
    return jsonify({'InspektionID': inspektion_id}), 201

@app.route('/inspektionen/<int:inspektion_id>', methods=['GET'])
def get_inspektion(inspektion_id):
    connection = get_db_connection()
    inspektion = Inspektion.read(connection, inspektion_id)
    connection.close()
    if inspektion:
        return jsonify(inspektion.__dict__)
    else:
        return jsonify({'error': 'Inspektion not found'}), 404

@app.route('/mietvertraege', methods=['POST'])
def create_mietvertrag():
    data = request.get_json()
    connection = get_db_connection()
    mietvertrag_id = Mietvertrag.create(connection, **data)
    connection.close()
    return jsonify({'MietvertragID': mietvertrag_id}), 201

@app.route('/mietvertraege/<int:mietvertrag_id>', methods=['GET'])
def get_mietvertrag(mietvertrag_id):
    connection = get_db_connection()
    mietvertrag = Mietvertrag.read(connection, mietvertrag_id)
    connection.close()
    if mietvertrag:
        return jsonify(mietvertrag.__dict__)
    else:
        return jsonify({'error': 'Mietvertrag not found'}), 404

@app.route('/mitarbeiter', methods=['POST'])
def create_mitarbeiter():
    data = request.get_json()
    connection = get_db_connection()
    mitarbeiter_id = Mitarbeiter.create(connection, **data)
    connection.close()
    return jsonify({'MitarbeiterID': mitarbeiter_id}), 201

@app.route('/mitarbeiter/<int:mitarbeiter_id>', methods=['GET'])
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