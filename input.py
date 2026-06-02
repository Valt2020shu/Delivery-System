import tabulate

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
        
def table_creation(cursor):
        cursor.execute("select * from products;")
        records = cursor.fetchall()
        table = create_table(records)
        print(table)

def customer_input():
    while True:
        print("Select product to purchase")
        prod_id = input("Enter product id: ")
        break
        for row in records:
            if str(row['Product_ID']) == prod_id:
                price =  row['Price']
                size = row['Size']
                break
        else:
            print("Invalid product")
            print("Please try again")
            continue 
        break
