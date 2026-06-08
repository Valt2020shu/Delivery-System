# def deliveryincharge(priority,delivery_in_charge,zone_no,size):    WORK ON LATER
#     if delivery_in_charge['C_ID'] == priority:
#         if delivery_in_charge['Zone_Delivered'] == zone_no and delivery_in_charge['Maximum_Orders'] - delivery_in_charge["Current_Orders"] >= size:
#             current_orders = delivery_in_charge['Current_Orders']
#             if current_orders+size == delivery_in_charge['Maximum_Orders']:
#                 availability = 0
#             else:
#                 availability = 1
#             assigned_in_charge = delivery_in_charge['Name']
#             centre_id = priority
#             return assigned_in_charge,centre_id,availability,current_orders
#         return False


def allocation(zone_allocation,zone_priority,order_size,city,delivery_centres,delivery_in_charge):
    if order_size == "Large":
        size = 3
    elif order_size == 'Medium':
        size = 2
    else:
        size = 1

    for i in zone_allocation:
        if i['Location'] == city:
            zone_no = i['Zone_No']

    for i in zone_priority:
        if i['Zone_No'] == zone_no:
            priority_1 = i['Priority_1']
            priority_2 = i['Priority_2']
            priority_3 = i['Priority_3']

    for i in delivery_in_charge:   # Might change the condition repetition to a function
        if i['C_ID'] == priority_1:
           if i['Zone_Delivered'] == zone_no and i['Maximum_Orders'] - i["Current_Orders"] >= size:
                current_orders = i['Current_Orders']
                if current_orders+size == i['Maximum_Orders']:
                    availability = 0
                else:
                    availability = 1
                assigned_in_charge = i['Name']
                centre_id = priority_1
                break

        elif i['C_ID'] == priority_2:
           if i['Zone_Delivered'] == zone_no and i['Maximum_Orders'] - i["Current_Orders"] >= size:
                current_orders = i['Current_Orders']
                if current_orders+size == i['Maximum_Orders']:
                    availability = 0
                else:
                    availability = 1                
                assigned_in_charge = i['Name']
                centre_id = priority_2
                break
               
        elif i['C_ID'] == priority_3:
           if i['Zone_Delivered'] == zone_no and i['Maximum_Orders'] - i["Current_Orders"] >= size:
                if current_orders+size == i['Maximum_Orders']:
                    availability = 0
                else:
                    availability = 1
                current_orders = i['Current_Orders']
                assigned_in_charge = i['Name']
                centre_id = priority_3
                break
        else:
            continue

    else:
        raise Exception
        
    for i in delivery_centres:
        if centre_id == i["C_ID"]:
            centre_location = i["Centre_Location"]
            

    return zone_no, assigned_in_charge, centre_location, f"update deliveryincharges set current_orders = {current_orders} + {size}, availability = {availability}"