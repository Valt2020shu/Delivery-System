import tabulate
import routing
import datetime

class Validation_Error(Exception):  # Class for custom error messages
    def __init__ (self,message):
        self.message = message

def create_table(data, headers='keys', tablefmt ='grid'):  # For pretty print of tables
    table = tabulate.tabulate(data,headers=headers, tablefmt=tablefmt)
    return table



def user_name():  # Takes the name of the user and keeps it as the customer name
    customer_name = input("Enter your name: ")  

    while customer_name == "ADMIN":  # Verification for admin which allows for database editing, weak verification for the sake of simplicity, not very relevant for the purpose of this project,might be updated later
        password = input("Enter password: ")
        if password == "ADMIN":
            print("Welcome Admin")
            break

        else:
            print("Invalid Password")
            print("If you are an admin please enter the correct name and password")
            print("If you are a customer, enter your name")
            customer_name = input("Enter your name: ")
        
    return customer_name



def customer_order_processing(products,orders,zone_priority,zone_allocation,delivery_centres,delivery_in_charge,prod_id,city,address,customer_name): # Returns query to add customers order to the database 
    for row in products:
        if str(row["Product_ID"]) == prod_id:
            prod_name = row["Product_Name"]
            break
    else:
        raise Validation_Error("Invalid Product ID")
        
    order_size = row["Size"]
    order_price = row["Price"]
    date_ordered = str(datetime.date.today())



    zone_no, assigned_in_charge, centre_location = routing.allocation(zone_allocation,zone_priority,order_size,city,delivery_centres,delivery_in_charge)

    return(f'insert into orders(Product_Name, Order_Size, Customer_Name, Customer_Address, Zone_No, Assigned_Incharge, Order_Price, Shipped_From, Date_Ordered) values({prod_name},{order_size},{customer_name},{address},{zone_no}, {assigned_in_charge},{order_price},{centre_location},{date_ordered} )')
   #  return f"{order_price},{order_size},{prod_id},{customer_name},{city},{address}" # (TEST ONLY)

def customer_input(customer_name,products,zone_priority='temp',zone_allocation='temp',delivery_centres='temp',delivery_in_charge='temp',orders='temp'): # Takes necessary information from the customer to place their order
    while True:
        try:

            print(create_table(products))
            print("Select product to purchase")
            prod_id = input("Enter the Product ID: ").strip()
            city = input("Enter the city you live in: ").strip()
            address = input("Enter your address: ").strip()

            return customer_order_processing(products,orders,zone_priority,zone_allocation,delivery_centres,delivery_in_charge,prod_id,city,address,customer_name) 

            break

        except Validation_Error as e:
            print(e.message)
            continue
