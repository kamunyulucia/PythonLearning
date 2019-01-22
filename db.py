import mysql.connector
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
 
 
def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='school',
                                       user='root',
                                       password='lucia2019')
        if conn.is_connected():
            print('Connected to MySQL Persons')
 
    except Error as e:
        print(e)
 
    finally:
        #conn.close()

def query_with_fetchone():
    try:
        #dbconfig = read_db_config()
        #conn = MySQLConnection(**dbconfig)
        connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Persons")
 
        row = cursor.fetchone()
 
        while row is not None:
            print(row)
            row = cursor.fetchone()
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()

 
 
if __name__ == '__main__':
    connect()
    query_with_fetchone()