import os

from flask import Flask, request, jsonify
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

def get_user(username: str, password: str) -> User:
    connection = get_db_connection()
    cursor = connection.cursor()
    sql = 'SELECT * FROM users WHERE UserName = %s AND Password = %s'
    val = (username, password)
    cursor.execute(sql, val)
    row = cursor.fetchone()
    return User.load(*row)


# Authentication decorator
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        username = request.args.get('USERNAME')
        password = request.args.get('PASSWORD')
        user = get_user(username, password)
        if not user:
            return jsonify({'error': 'Unauthorized access'}), 401
        return f(*args, **kwargs)

    return decorated

def requires_write(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        username = request.args.get('USERNAME')
        password = request.args.get('PASSWORD')
        user = get_user(username, password)
        if not user or not user.CanWrite:
            return jsonify({'error' : 'Unauthorized access'}), 401
        return f(*args, **kwargs)
    return decorated

def requires_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        username = request.args.get('USERNAME')
        password = request.args.get('PASSWORD')
        user = get_user(username, password)
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
def get_fahrzeug(objekt_id):
    connection = get_db_connection()
    objekt = MietObjekt.read(connection, objekt_id)
    connection.close()
    if objekt:
        return jsonify(objekt.__dict__)
    else:
        return jsonify({'error': 'Fahrzeug not found'}), 404


@app.route('/mietvertraege', methods=['GET'])
@requires_auth
def get_all_mietvertraege():
    connection = get_db_connection()
    mietvertraege = MietVorgang.get_all(connection)
    connection.close()
    return jsonify([m.__dict__ for m in mietvertraege])


@app.route('/mietvertraege/<int:mietvertrag_id>', methods=['GET'])
@requires_auth
def get_mietvertrag(mietvertrag_id):
    connection = get_db_connection()
    mietvertrag = MietVorgang.read(connection, mietvertrag_id)
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
    app.run(debug=True, use_reloader=False)
