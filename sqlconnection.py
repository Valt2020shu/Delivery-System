import mysql.connector as connector
from mysql.connector import Error

def manual_connection(host,user,password,database):  #Manual connection if the default fails
    try:
        global connection 
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
    manual_connection(host,user,password,database)