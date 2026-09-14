'''
==========================================================================================================================================================
MODULE: routing.py
PURPOSE: Responsible for assigning delivery incharge and delivery centre based on the location of the customer
==========================================================================================================================================================
'''



def allocation(zone_allocation,zone_priority,order_size,city,delivery_centres,delivery_in_charge):
    if order_size == "Large":   # Assigns the capacity required by each product
        size = 3
    elif order_size == 'Medium':
        size = 2
    else:
        size = 1

    for i in zone_allocation:  # Checks for zone number required for priority list
        if i['Location'] == city:
            zone_no = i['Zone_No']

    for i in zone_priority:
        if i['Zone_No'] == zone_no:  
            priority_1 = i['Priority_1']
            priority_2 = i['Priority_2']
            priority_3 = i['Priority_3']

    for i in delivery_in_charge:   # Provides information about assigned incharge
        if i['C_ID'] == priority_1:
            availability, assigned_in_charge, centre_id, current_orders = priority_check(i,priority_1,zone_no,size)
            priority_no = 1
            break

        elif i['C_ID'] == priority_2:
           availability, assigned_in_charge, centre_id, current_orders = priority_check(i,priority_2,zone_no,size)
           priority_no = 2
           break
               
        elif i['C_ID'] == priority_3:
           availability, assigned_in_charge, centre_id, current_orders = priority_check(i,priority_3,zone_no,size)
           priority_no = 3
           break

        else:
            continue

    else:
        raise Exception
        
    for i in delivery_centres:  # Provides the location from which product is shipped
        if centre_id == i["C_ID"]:
            centre_location = i["Centre_Location"]

    additional_query = "update deliveryincharges set current_orders = %s + %s, availability = %s where name = %s"    #To update the availability of a given incharge
    additional_values = (current_orders,size,availability,assigned_in_charge)

    return zone_no, assigned_in_charge, centre_location, additional_query, additional_values, priority_no

def priority_check(delivery_in_charge,priority,zone_no,size):
    # To assign an incharge based on zone

    if delivery_in_charge['Zone_Delivered'] == zone_no and delivery_in_charge['Maximum_Orders'] - delivery_in_charge["Current_Orders"] >= size:  # Checks if a given incharge is valid for the order
        current_orders = delivery_in_charge['Current_Orders']
        if current_orders+size == delivery_in_charge['Maximum_Orders']:
            availability = 0
        else:
            availability = 1
        assigned_in_charge = delivery_in_charge['Name']
        centre_id = priority
    return availability,assigned_in_charge,centre_id,current_orders

