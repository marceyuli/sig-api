from flask import Flask, make_response,jsonify, request
from flask_mysqldb import MySQL
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)

#Creating a connection cursor#
# cursor = mysql.connection.cursor()

api = Api(app)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/getlineas', methods = ['GET'])
def getlineas():
    if request.method == 'GET':
        lineas = []
        cursor = mysql.connection.cursor();
        cursor.execute("SELECT id, code, direccion, telefono, mail, foto, descripcion FROM linea")
        lineas = cursor.fetchall()
        cursor.close()
        response = make_response(jsonify(lineas),200)
        return response


if __name__ == '__main__':
    app.run(debug=True)