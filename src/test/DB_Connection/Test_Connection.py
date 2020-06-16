import Dummy_Database
import request

CURD = ['GET', 'POST', 'PUT', 'DELETE']


def connect(self, host, db, user, passwd):
    try:
        db = Dummy_Database.connect(host="localhost:8080", db="BigPayDB", user="bigpay", passwd="12345")

        if CURD == 'GET':
            # Create a Cursor object
            cur = db.cursor()

            # Create a query string. It can contain variables
            query_string = "SELECT * FROM USER_TABLE"

            # Execute the query
            cur.execute(query_string)

            # Get all the rows present the database
            for each_row in cur.fetchall():
                print(each_row)

            # Close the connection
            db.close()

        elif CURD == 'POST':
            # Create a Cursor object
            cur = db.cursor()

            # Create a query string. It can contain variables
            query_string = "CREATE USER = 'BIGPAY_ONE' WITH PASSWD = 67890"

            # Execute the query
            cur.execute(query_string)

            # Get all the rows present the database
            for each_row in cur.fetchall():
                print(each_row)

            # Close the connection
            db.close()

        elif CURD == 'PUT':
            # Create a Cursor object
            cur = db.cursor()

            # Create a query string. It can contain variables
            query_string = "UPDATE USER_TABLE SET ID=1002 WHERE ID= 55"

            # Execute the query
            cur.execute(query_string)

            # Get all the rows present the database
            for each_row in cur.fetchall():
                print(each_row)

            # Close the connection
            db.close()

        elif CURD == 'DELETE':
            # Create a Cursor object
            cur = db.cursor()

            # Create a query string. It can contain variables
            query_string = "DELETE FROM USER_TABLE WHERE ID=55"

            # Execute the query
            cur.execute(query_string)

            # Get all the rows present the database
            for each_row in cur.fetchall():
                print(each_row)

            # Close the connection
            db.close()

    except Exception as e:
        print('Error ', e)


class Test_Connection:
    pass
