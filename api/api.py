import os
from typing import Tuple

from flask import Flask, request, jsonify, wrappers, Response
from functools import wraps

from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from MietObjekt import MietObjekt
from MietVorgang import MietVorgang
from Mitarbeiter import Mitarbeiter
from User import User
import mysql.connector
from dotenv import load_dotenv
import json

app = Flask(__name__)
load_dotenv()
# Define your API key
API_KEY = os.getenv('API_KEY')

# MySQL connection parameters
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS'),
    'database': os.getenv('DB_DATABASE'),
}


def get_db_connection() -> PooledMySQLConnection | MySQLConnectionAbstract:
    return mysql.connector.connect(**db_config)


# Authentication decorator
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user = User.get(get_db_connection(), request.args.get('USERNAME'), request.args.get('PASSWORD'))
        if not user:
            return jsonify({'error': 'Unauthorized access'}), 401
        return f(*args, **kwargs)

    return decorated

def requires_write(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user = User.get(get_db_connection(), request.args.get('USERNAME'), request.args.get('PASSWORD'))
        if not user or not user.CanWrite:
            return jsonify({'error' : 'Unauthorized access'}), 401
        return f(*args, **kwargs)
    return decorated

def requires_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user = User.get(get_db_connection(), request.args.get('USERNAME'), request.args.get('PASSWORD'))
        if not user or not user.IsAdmin:
            return jsonify({'error' : 'Unauthorized access'}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/objekte', methods=['GET'])
@requires_auth
def get_all_fahrzeuge():
    connection = get_db_connection()
    objekte = MietObjekt.get_all(connection)
    connection.close()
    return jsonify([i.get_dict() for i in objekte])


@app.route('/objekte/<int:objekt_id>', methods=['GET'])
@requires_auth
def get_fahrzeug(objekt_id: int) -> Response | tuple[Response, int] :
    connection = get_db_connection()
    objekt = MietObjekt.get(connection, objekt_id)
    connection.close()
    if objekt:
        return jsonify(objekt.get_dict())
    else:
        return jsonify({'error': 'Fahrzeug not found'}), 404


@app.route('/mietvertraege', methods=['GET'])
@requires_auth
def get_all_mietvertraege():
    connection = get_db_connection()
    mietvertraege = MietVorgang.get_all(connection)
    connection.close()
    return jsonify([m.get_dict() for m in mietvertraege])


@app.route('/mietvertraege/<int:mietvertrag_id>', methods=['GET'])
@requires_auth
def get_mietvertrag(mietvertrag_id):
    connection = get_db_connection()
    mietvertrag = MietVorgang.read(connection, mietvertrag_id)
    connection.close()
    if mietvertrag:
        return jsonify(mietvertrag.get_dict())
    else:
        return jsonify({'error': 'Mietvertrag not found'}), 404


@app.route('/mitarbeiter', methods=['GET'])
@requires_auth
def get_all_mitarbeiter():
    connection = get_db_connection()
    mitarbeiter = Mitarbeiter.get_all(connection)
    connection.close()
    return jsonify([m.get_dict() for m in mitarbeiter])


@app.route('/mitarbeiter/<int:mitarbeiter_id>', methods=['GET'])
@requires_auth
def get_mitarbeiter(mitarbeiter_id):
    connection = get_db_connection()
    mitarbeiter = Mitarbeiter.read(connection, mitarbeiter_id)
    connection.close()
    if mitarbeiter:
        return jsonify(mitarbeiter.get_dict())
    else:
        return jsonify({'error': 'Mitarbeiter not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
