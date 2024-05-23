import os
from typing import Tuple

import flask
from flask import Flask, request, jsonify, wrappers, Response
from functools import wraps, partial

from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from MietObjekt import MietObjekt
from MietVorgang import MietVorgang
from Mitarbeiter import Mitarbeiter
from User import User
import mysql.connector
from dotenv import load_dotenv
import json
import base64

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
def requires_auth(f, argument):
    @wraps(f)
    def decorated(*args, **kwargs):
        usernamepass = base64.b64decode(request.headers.get('Authorization').replace('Basic ', '')).decode('utf-8')
        username,password = usernamepass.split(':')
        user = User.get(get_db_connection(), username)
        if not user or user.Password != password or user.Level > argument:
            return jsonify({'error': 'Unauthorized access'}), 401
        return f(*args, **kwargs)
    return decorated

#region objekte
@app.route('/objekte', methods=['GET'])
@partial(requires_auth, argument=1)
def get_all_fahrzeuge():
    connection = get_db_connection()
    objekte = MietObjekt.get_all(connection)
    connection.close()
    return jsonify([i.get_dict() for i in objekte])


@app.route('/objekte/<int:objekt_id>', methods=['GET'])
@partial(requires_auth, argument=1)
def get_fahrzeug(objekt_id: int) -> Response | tuple[Response, int] :
    connection = get_db_connection()
    objekt = MietObjekt.get(connection, objekt_id)
    connection.close()
    if objekt:
        return jsonify(objekt.get_dict())
    else:
        return jsonify({'error': 'Fahrzeug not found'}), 404
#endregion

#region vetraege
@app.route('/mietvertraege', methods=['GET'])
@partial(requires_auth, argument=1)
def get_all_mietvertraege():
    connection = get_db_connection()
    mietvertraege = MietVorgang.get_all(connection)
    connection.close()
    return jsonify([m.get_dict() for m in mietvertraege])


@app.route('/mietvertraege/<int:mietvertrag_id>', methods=['GET'])
@partial(requires_auth, argument=1)
def get_mietvertrag(mietvertrag_id):
    connection = get_db_connection()
    mietvertrag = MietVorgang.read(connection, mietvertrag_id)
    connection.close()
    if mietvertrag:
        return jsonify(mietvertrag.get_dict())
    else:
        return jsonify({'error': 'Mietvertrag not found'}), 404
#endregion

#region mitarbeiter
@app.route('/mitarbeiter', methods=['GET'])
@partial(requires_auth, argument=1)
def get_all_mitarbeiter():
    connection = get_db_connection()
    mitarbeiter = Mitarbeiter.get_all(connection)
    connection.close()
    return jsonify([m.get_dict() for m in mitarbeiter])


@app.route('/mitarbeiter/<int:mitarbeiter_id>', methods=['GET'])
@partial(requires_auth, argument=1)
def get_mitarbeiter(mitarbeiter_id):
    connection = get_db_connection()
    mitarbeiter = Mitarbeiter.read(connection, mitarbeiter_id)
    connection.close()
    if mitarbeiter:
        return jsonify(mitarbeiter.get_dict())
    else:
        return jsonify({'error': 'Mitarbeiter not found'}), 404
#endregion

#region user
@app.route('/user', methods=['GET'])
@partial(requires_auth, argument=0)
def get_users():
    connection = get_db_connection()
    users = User.get_all(connection)
    connection.close()
    return jsonify([user.get_dict() for user in users])


@app.route('/user/<user_id>', methods=['GET'])
@partial(requires_auth, argument=0)
def get_user(user_id):
    connection = get_db_connection()
    user = User.get(connection, user_id)
    connection.close()
    if user:
        return jsonify(user.get_dict())
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/user', methods=['PUT'])
def create_user():
    try:
        username = request.json.get('username')
        password = request.json.get('password')
        permissions = int(request.json.get('level'))
    except TypeError:
        return jsonify({'error': 'Invalid JSON'}), 400
    user = User(username, password, permissions)
    connection = get_db_connection()
    user.create(connection)
    connection.close()
    return jsonify(user.get_dict())

@app.route('/user', methods=['DELETE'])
def delete_user():
    try:
        username = str(request.json.get('username'))
    except TypeError:
        return jsonify({'error': 'Invalid JSON'}), 400
    connection = get_db_connection()
    user = User.get(connection, username)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    user.delete(connection)
    connection.close()
    return jsonify({"success": f'Deleted user {username}'})
#endregion

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
