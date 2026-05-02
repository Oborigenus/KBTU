import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "dbname": "postgres",
    "user": "postgres",
    "password": "Sardar228",
    "port": 5432
}

def connect():
    return psycopg2.connect(**DB_CONFIG)