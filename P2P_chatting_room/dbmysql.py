# generate database, tables
# pip install mysql-connector-python mysql-connector

import mysql.connector

conn = mysql.connector.connect(user = 'root', password = 'root1234', host = 'localhost', database='p2p')
cur = conn.cursor()

create_db = "CREATE DATABASE p2p"

# create table for store offline message
sql_table_offline_msg ="""

create table offline_msg(
    offid int AUTO_INCREMENT primary key,
    targetIP varchar(255) not null,
    msg varchar(255) not null
)
"""
# cur.execute(sql_table_offline_msg)


# create table for blocked users(ip address)
sql_table_block ="""
create table blocklist(
    blockId int auto_increment primary key,
    ip varchar(255) not null unique 
)
"""
# cur.execute(sql_table_block)



# cur.execute(create_db)

# sql_ip_table = """
# CREATE table IPs(
#     ipid int AUTO_INCREMENT primary key,
#     ip varchar(255) not null unique
# )
# cur.execute(sql_ip_table)
# """

# sql_insert = "insert into IPs (ip) values ('%s') " % ("192.158.1.38")

# sql =" select * from IPs"
# try:
#     cur.execute(sql_insert)
#     conn.commit()
#     print("Success")
# except:
#     conn.rollback()
#     print("Failed")

# sql_select = "Select * from IPs"
# cur.execute(sql_select)
# res = cur.fetchall()
# print(res)

# For user to ban someone. People banned cannot chat with the user
# sql_table_status = """
#     Create table usr_stat(
#         sid int AUTO_INCREMENT primary key,
#         opeID int not null,
#         bannedID int not null,
#         FOREIGN KEY (opeID) REFERENCES IPs(ipid),
#         FOREIGN KEY(bannedID) REFERENCES IPs(ipid)
#     )
# """
# cur.execute(sql_table_status)

cur.close()
conn.close()