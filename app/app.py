# backend/app.py
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Api working!'

# Configure MySQL connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_DATABASE')
        )
        if connection.is_connected():
            print("Connection to MySQL database established successfully.")
        return connection
    except Error as e:
        print(f'Error: {e}')
        return none

# API configuration
@app.route('/execute-sql', methods=['POST'])
def execute_sql():
    data = request.get_json()  # Expecting JSON data
    sql_query = data.get('query')  # Get the SQL query from the JSON data

    if not sql_query:
        return jsonify({'error': 'No SQL query provided'}), 400

    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({'result': result})
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
