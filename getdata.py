
from mysql.connector import MySQLConnection, Error
#from python_mysql_dbconfig import read_db_config
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

def query_with_fetchall():
    try:
        """
        conn = mysql.connector.connect(host='localhost',
                                       database='school',
                                       user='root',
                                       password='lucia2019')
        #conn = MySQLConnection(**dbconfig)
        #cursor = conn.cursor() """
        connect()
        cursor.execute("SELECT * FROM Persons")
        rows = cursor.fetchall()
 
        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
 
 
if __name__ == '__main__':
    query_with_fetchall()