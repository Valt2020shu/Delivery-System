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
                print(data_input.customer_input(customer_name,products))
                
            elif choice == '2':
                print("Fetching orders....")
                time.sleep(2)
                cursor.execute(f'select * from orders where Customer_Name = "{customer_name}"')
                record = cursor.fetchall()
                print(customer_name)
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
                print("Number 1 selected")
            
            elif choice == '2':
                print("Number 2 selected")

            elif choice == '3':
                print("Number 3 selected")

            elif choice == '4':
                print("Number 4 selected")

            elif choice == '5':
                print("Number 5 selected")
                

            elif choice == '6':
                print("Number 6 selected")
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

