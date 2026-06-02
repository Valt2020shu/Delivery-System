import tabulate
import routing

class Validation_Error(Exception):
    def __init__ (self,message):
        self.message = message

def create_table(data, headers='keys', tablefmt ='grid'):
    table = tabulate.tabulate(data,headers=headers, tablefmt=tablefmt)
    return table

customer_name = input("Enter your name: ")

while customer_name == "ADMIN":
    password = input("Enter password: ")
    if password == "ADMIN":
        user = "ADMIN"
        print("Welcome Admin")
        break

    else:
        print("Invalid Password")
        print("If you are an admin please enter the correct name and password")
        print("If you are a customer, enter your name")
        customer_name = input("Enter your name: ")

def customer_order_processing(products,orders,zone_priority,zone_allocation,delivery_centres,delivery_in_charge,prod_id,city,address,customer_name):
    for row in products:
        if row["Product_ID"] == prod_id:
            break
        else:
            raise Validation_Error("Invalid Product ID")
        
    order_size = row["Size"]
    order_id = orders[-1]["Order_ID"] + 1
    order_price = row["Price"]

    zone_no, assigned_in_charge, centre_location = routing.allocation(zone_allocation,zone_priority,order_size,city,delivery_centres,delivery_in_charge)

    return(f'insert into orders values({order_id},{prod_id},{order_size},{customer_name},{address},{zone_no}, {assigned_in_charge},{order_price},{centre_location} )')
   

def customer_input(products,zone_priority='temp',zone_allocation='temp',delivery_centres='temp',delivery_in_charge='temp',orders='temp'):
    while True:
        try:

            print(create_table(products))
            print("Select product to purchase")
            prod_id = input("Enter the Product ID: ")
            city = input("Enter the city you live in: ")
            address = input("Enter your address: ")

            customer_order_processing(products,orders,zone_priority,zone_allocation,delivery_centres,delivery_in_charge,prod_id,city,address,customer_name) 

            break

        except Validation_Error as e:
            print(e.message)
            continue
