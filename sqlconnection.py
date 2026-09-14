import mysql.connector as connector
from mysql.connector import Error
import json


def automatic_connection():        # Tries to connect automatically
    with open('config.json', 'r') as config:
        data = json.load(config)
    # print(data['host'],data['user'],data['password'],data['database'])
    try:
        print("Connecting to MySQL server....")
        connection = connector.connect(
            host = str(data['host']).strip(),
            user = str(data['user']).strip(),    
            password = str(data['password']).strip(),     #Password needs to be adjusted according to the device
            database = str(data['database']).strip()

        )

    except connector.Error as e:
        print(f"Error connecting to MySQL: {e.errno}\n")
        print(f"Error connecting to MySQL: {e.msg}\n")
        print("Please manually enter the following:")
        host = input("Host: ")
        user = input("User: ")
        password = input("Password: ")
        database = input("Database: ")
        connection = manual_connection(host,user,password,database)

    if connection == None:
        return
    else:
        return connection
    
    


def manual_connection(host,user,password,database):  #Manual connection if the default fails
    try: 
        print("Connecting to MySQL server....")
        connection = connector.connect(
            host=host,
            user=user,    
            password=password,     
            database=database

    )
        with open('config.json','w') as config:
            data = {'host':host,'user':user,'password':password,'database':database}
            json.dump(data,config,indent=3)
        

    except Error:
        print(f"Error connecting to MySQL: {Error}")
        print("Connection has failed again\n")

        while True:
            choice = input("Do you wish to retry (Y/N): ").strip().lower()

            if choice == "y" or choice == 'yes':
                print("Please enter the correct details: ")
                host = input("Host: ")
                user = input("User: ")
                password = input("Password: ")
                database = input("Database: ")
     
                connection = manual_connection(host,user,password,database)
                break

            elif choice == 'n' or choice == 'no':
                print('Exiting')
                print('Goodbye....')
                return

            else:
                print("Please enter a valid option\n")

    return connection








def sql_data_fetch(cursor):  # Gets the data from all tables in the database
    
    cursor.execute("select * from products order by Product_ID;")
    products = cursor.fetchall()

    cursor.execute("select * from deliveryincharges order by IC_ID;")
    delivery_in_charge = cursor.fetchall()

    cursor.execute("select * from deliverycentres order by C_ID;")
    delivery_centres = cursor.fetchall()

    cursor.execute("select * from zoneallocation order by zone_no;")
    zone_allocation = cursor.fetchall()  

    cursor.execute("select * from zoneprioritylist order by zone_no;")
    zone_priority = cursor.fetchall()

    cursor.execute("select * from orders order by order_id;")
    orders = cursor.fetchall()

    return products, delivery_centres, delivery_in_charge, zone_allocation, zone_priority, orders 
