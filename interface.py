import input
import sqlconnection

if sqlconnection.connection.is_connected():
    print("Connected Successfully")
    cursor = sqlconnection.connection.cursor(dictionary=True)


input.customer_input("Order",cursor)