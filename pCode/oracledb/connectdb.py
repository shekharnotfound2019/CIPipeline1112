#/usr/bin/env python3
import getpass
import sys
syspath = '/home/harsh/pCode/venv/lib/python3.10/site-packages'


sys.path.append(syspath)
import oracledb

pw = getpass.getpass("Enter password: ")

connection = oracledb.connect(
    user="shekhar",
    password=pw,
    dsn="oradb1.demo.com/freepdb1")

print("Successfully connected to Oracle Database")

cursor = connection.cursor()

sqlcmd = "select file_name from dba_data_files"
cursor.execute(sqlcmd)
all_db_files = cursor.fetchall()

# print all db files
for dbfile in all_db_files:
    print(f'{dbfile}')
print(all_db_files)

connection.close()