import data_input
import sqlconnection


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
                print("Number 1 selected")
                print(data_input.customer_input(customer_name,products))
                
            elif choice == '2':
                print("Number 2 selected")
                pass
                # record = cursor.execute(f'select * from orders where customer_name is {data_input.customer_name}')
                # table = data_input.create_table(record)
                # print(table)

            elif choice == '3':
                print("Number 3 selected")
                return

            else:
                print("Please select a valid option")

    else:
        while True:
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
    if connection.is_connected():
        print("Connected Successfully")
        print("\n")
        cursor = connection.cursor(dictionary=True)

        
    products = sqlconnection.sql_data_fetch(cursor)    
    customer_name = data_input.user_name()
    main_menu()

