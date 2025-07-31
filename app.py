from flask import Flask
import psycopg2

app = Flask(__name__)

DB_URL = "postgresql://lab10db_zlln_user:gdT9nltdzKYenjEv1hukDtX0I4WrsLvT@dpg-d25f89nfte5s7384bmpg-a/lab10db_zlln"

@app.route('/')
def index():
    return 'Hello World from Cassandra Boland in 3308'

@app.route('/db_test')
def db_test():
    try:
        conn = psycopg2.connect(DB_URL)
        conn.close()
        return "Database connection successful!"
    except Exception as e:
        return f"Database connection failed: {str(e)}"

@app.route('/db_create')
def db_create():
    try:
        conn = psycopg2.connect(DB_URL)
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS Basketball (
                First varchar(255),
                Last varchar(255),
                City varchar(255),
                Name varchar(255),
                Number int
            );
        ''')
        conn.commit()
        conn.close()
        return "Basketball Table Created"
    except Exception as e:
        return f"Error creating table: {str(e)}"

@app.route('/db_insert')
def db_insert():
    try:
        conn = psycopg2.connect(DB_URL)
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO Basketball (First, Last, City, Name, Number)
            VALUES
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
            ('Jack', 'Boland', 'CU Boulder', 'Buffs', 3308);
        ''')
        conn.commit()
        conn.close()
        return "Basketball Table Populated"
    except Exception as e:
        return f"Error inserting data: {str(e)}"

@app.route('/db_select')
def db_select():
    try:
        conn = psycopg2.connect(DB_URL)
        cur = conn.cursor()
        cur.execute('SELECT * FROM Basketball;')
        records = cur.fetchall()
        conn.close()

        # Create HTML table
        html = "<table border='1'><tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"
        for row in records:
            html += "<tr>"
            for col in row:
                html += f"<td>{col}</td>"
            html += "</tr>"
        html += "</table>"
        return html
    except Exception as e:
        return f"Error selecting data: {str(e)}"

@app.route('/db_drop')
def db_drop():
    try:
        conn = psycopg2.connect(DB_URL)
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS Basketball;')
        conn.commit()
        conn.close()
        return "Basketball Table Dropped"
    except Exception as e:
        return f"Error dropping table: {str(e)}"
