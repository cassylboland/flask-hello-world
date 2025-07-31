from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return 'Hello World from Cassandra Boland in 3308'

@app.route('/db_test')
def db_test():
    try:
        conn = psycopg2.connect("your_db_url_here") 
        conn.close()
        return "Database connection successful!"
    except Exception as e:
        return f"Database connection failed: {str(e)}"
