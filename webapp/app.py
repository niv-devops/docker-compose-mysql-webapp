import os
from flask import Flask, render_template, abort
import mysql.connector

app = Flask(__name__)

def db_connection():
    required_env_vars = ['MYSQL_HOST', 'MYSQL_DATABASE', 'MYSQL_USER', 'MYSQL_PASSWORD']
    missing_env_vars = [var for var in required_env_vars if not os.getenv(var)]
    if missing_env_vars:
        error_message = f"Missing environment variables: {', '.join(missing_env_vars)}"
        print(error_message)
        abort(500, description=error_message)
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            database=os.getenv('MYSQL_DATABASE'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD')
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None

@app.route('/')
def index():
    db = db_connection()
    if db is None:
        return "Connection to the database has failed.", 500
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template('index.html', employees=employees)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
