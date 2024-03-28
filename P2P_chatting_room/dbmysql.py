# generate database, tables
# pip install mysql-connector-python mysql-connector

import mysql.connector

conn = mysql.connector.connect(user = 'root', password = 'root1234', host = 'localhost', database='p2p')
cur = conn.cursor()

create_db = "CREATE DATABASE p2p"

cur.execute(create_db)

sql_ip_table = """
CREATE table IPs(
    ipid int AUTO_INCREMENT primary key,
    ip varchar(255) not null unique
)
cur.execute(sql_ip_table)
"""

sql_insert = "insert into IPs (ip) values ('%s') " % ("192.158.1.38")

# sql =" select * from IPs"
try:
    cur.execute(sql_insert)
    conn.commit()
    print("Success")
except:
    conn.rollback()
    print("Failed")

sql_select = "Select * from IPs"
cur.execute(sql_select)
res = cur.fetchall()
print(res)
cur.close()
conn.close()