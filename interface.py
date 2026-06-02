import data_input
import sqlconnection

if sqlconnection.connection.is_connected():
    print("Connected Successfully")
    cursor = sqlconnection.connection.cursor(dictionary=True)

    
sqlconnection.sql_data_fetch(cursor)
data_input.customer_input(sqlconnection.products)