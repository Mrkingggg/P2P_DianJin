# generate database, tables
# pip install mysql-connector-python mysql-connector

import mysql.connector

conn = mysql.connector.connect(user = 'root', password = 'root1234', host = '127.0.0.1')
cursor = conn.cursor()

create_db = "CREATE DATABASE p2p"

cursor.execute(create_db)

cursor.close()
conn.close()