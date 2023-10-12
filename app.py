from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy import create_engine, text

load_dotenv()  # Load environment variables from .env file

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
#DB_PORT = int(os.getenv("DB_PORT", 3306))
#DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
connect_args={'ssl':{'fake_flag_to_enable_tls': True}}

connection_string = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}'

engine = create_engine(
        connection_string,
        connect_args=connect_args,

)

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('base.html')

@app.route('/doctors')
def doctors():
    # Establish a database connection
    with engine.connect() as connection:
        # Execute an SQL query to fetch data (replace this with your query)
        query1 = text('SELECT * FROM doctors')

        result1 = connection.execute(query1)

        # Fetch all rows of data
        db_data1 = result1.fetchall()

    return render_template('doctors.html', data1=db_data1)

@app.route('/patients')
def patients():
    # Establish a database connection
    with engine.connect() as connection:
        # Execute an SQL query to fetch data (replace this with your query)
        query2 = text('SELECT * FROM patients')

        result2 = connection.execute(query2)

        # Fetch all rows of data
        db_data2 = result2.fetchall()

    return render_template('patients.html', data2=db_data2)

@app.route('/laboratorytests')
def laboratorytests():
    # Establish a database connection
    with engine.connect() as connection:
        # Execute an SQL query to fetch data (replace this with your query)
        query3 = text('SELECT * FROM laboratorytests')

        result3 = connection.execute(query3)

        # Fetch all rows of data
        db_data3 = result3.fetchall()

    return render_template('laboratorytests.html', data3=db_data3)

if __name__ == '__main__':
    app.run(debug=True)