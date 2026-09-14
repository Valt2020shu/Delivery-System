'''
==========================================================================================================================================================
MODULE: interface.py
PURPOSE: Responsible for providing the interface between the user and the program allowing them to communicate
==========================================================================================================================================================
'''




import data_input
import sqlconnection
import time


def main_menu():  #The main CLI for the entire program
    if customer_name != "ADMIN":
        while True:
            print("What do you want to do: ")
            print("\t\t(1) Place new order")
            print("\t\t(2) View my order history")
            print("\t\t(3) Exit")
            choice = input("\nEnter option number: ").strip()
            print("\n")
            if choice == '1':
                print("Creating new order session....\n\n")
                time.sleep(2)
                data = data_input.customer_input(customer_name,products,zone_priority,zone_allocation,delivery_centres,delivery_in_charge,orders)

                if type(data) == tuple:
                    query,values,additional_query,additional_values = data
                else:
                    print("Order Cancelled")
                    query = None

                if query != None:    # If the order is placed, stores it in the system
                    cursor.execute(query,values)
                    cursor.execute(additional_query,additional_values)
                    connection.commit()
                    print("Order Placed")
                
                    
   
            elif choice == '2':
                print("Fetching orders....")
                time.sleep(2)
                cursor.execute('select * from orders where Customer_Name = %s',(customer_name,))
                record = cursor.fetchall()
                if len(record) == 0:
                    print("No placed orders")
                table = data_input.create_table(record)
                print(table)
                

            elif choice == '3':
                print("Goodbye")
                print("Exiting....")
                time.sleep(2)
                return

            else:
                print("Please select a valid option")

    else:
        while True:   # Need to finish
            print("What do you want to do: ")
            print("\t\t(1) Edit Orders")
            print("\t\t(2) Edit Delivery Centres")
            print("\t\t(3) Edit Zone Numbers and Allocation ")
            print("\t\t(4) Edit Products ")
            print("\t\t(5) Edit Delivery In Charges ")
            print("\t\t(6) Exit")
            choice = input("\nEnter option number: ").strip()
            print("\n")            

            if choice == '1':
                print("Fetching orders....")
                time.sleep(2)
                cursor.execute(f'select * from orders')
                record = cursor.fetchall()
                table = data_input.create_table(record)
                print(table)              
            
            elif choice == '2':
                print("Fetching delivery centres....")
                time.sleep(2)
                cursor.execute(f'select * from deliverycentres')
                record = cursor.fetchall()
                table = data_input.create_table(record)
                print(table)  

            elif choice == '3':
                print("Fetching zone numbers and allocation....")
                time.sleep(2)
                cursor.execute(f'select * from zoneallocation, zoneprioritylist where zoneallocation.zone_no = zoneprioritylist.zone_no')
                record = cursor.fetchall()
                table = data_input.create_table(record)
                print(table)  

            elif choice == '4':
                print("Fetching products....")
                time.sleep(2)
                cursor.execute(f'select * from products')
                record = cursor.fetchall()
                table = data_input.create_table(record)
                print(table)  

            elif choice == '5':
                print("Fetching delivery incharges....")
                time.sleep(2)
                cursor.execute(f'select * from deliveryincharges')
                record = cursor.fetchall()
                table = data_input.create_table(record)
                print(table)  
                

            elif choice == '6':
                print("Goodbye")
                print("Exiting....")
                time.sleep(2)
                return

            else:
                print("Please select a valid option")




if __name__ == "__main__":
    connection = sqlconnection.automatic_connection()  # Connects to the database
    if connection is not None:
        if connection.is_connected():
            print("Connected Successfully")
            print("\n")
            cursor = connection.cursor(dictionary=True)
            products, delivery_centres, delivery_in_charge, zone_allocation, zone_priority, orders  = sqlconnection.sql_data_fetch(cursor)    
            customer_name = data_input.user_name()
            main_menu()
