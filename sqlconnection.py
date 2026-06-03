import mysql.connector as connector
from mysql.connector import Error


def automatic_connection():        # Tries to connect automatically
    try:
        connection = connector.connect(
            host='localhost',
            user='root',    
            password='O)W%=[-(pEA-D6VFaz`_6',     #Password needs to be adjusted according to the device
            database='Delivery'

        )

    except Error:
        print(f"Error connecting to MySQL: {Error}")
        print("Please manually enter the following:")
        host = input("Host: ")
        user = input("User: ")
        password = input("Password: ")
        database = input("Database: ")
        connection = manual_connection(host,user,password,database)
    
    return connection
    
    


def manual_connection(host,user,password,database):  #Manual connection if the default fails
    try: 
        connection = connector.connect(
        host=host,
        user=user,    
        password=password,     
        database=database

    )

    except Error:
        print(f"Error connecting to MySQL: {Error}")
        print("Please enter the correct details: ")
        host = input("Host: ")
        user = input("User: ")
        password = input("Password: ")
        database = input("Database: ")
        manual_connection(host,user,password,database)

    return connection








def sql_data_fetch(cursor):  # Gets the data from all tables in the database
    
    cursor.execute("select * from products order by Product_ID;")
    products = cursor.fetchall()

    # cursor.execute("select * from delivery_in_charge order by IC_ID;")
    # delivery_in_charge = cursor.fetchall()

    # cursor.execute("select * from delivery_centres order by C_ID;")
    # delivery_centres = cursor.fetchall()

    # cursor.execute("select * from zone_allocation order by zone_no;")
    # zone_allocation = cursor.fetchall()  

    # cursor.execute("select * from zone_priority order by zone_no;")
    # zone_priority = cursor.fetchall()

    # cursor.execute("select * from orders order by order_id;")
    # orders = cursor.fetchall()

    return products #,delivery_centres,delivery_in_charge,zone_allocation,zone_priority,orders 
