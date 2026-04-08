import sys
import psycopg2

try:
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='Kinoo123',
        host='127.0.0.1',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute("SELECT datname FROM pg_database")
    rows = cur.fetchall()
    print("Databases:", rows, flush=True)
except Exception as e:
    print("Error:", e, flush=True)