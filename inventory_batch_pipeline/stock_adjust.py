import pandas as pd
import random
from datetime import datetime

# adjustment id, warehouse id, product id,adjust date, adjust type, quantity adjusted

def get_adjust_records_in_warehouse(warehouse_number, record_list):
    lower_range = random.randint(0,10)
    upper_range = random.randint(20,100)
    adjust_type_list = ["Restocked", "Sold Out", "Damaged", "Expired & Returned"]
    for product in product_list[lower_range:upper_range]:
        type_id = random.randint(0,3)
        adjust_record = {
          "adjustment_id": random.randint(100000,200000),
          "warehouse_id": warehouse_number,
          "product_id": product,
          "adjust_date": datetime.now(),
          "adjust_type": adjust_type_list[type_id]
          "quantity_adjusted": random.randint(10,300),
        }
        record_list.append(adjust_record)
    
    return record_list

def get_adjust_records(lower_range=0, upper_range):
    """
    takes input as lower range and upper range for warehouse list to
    only create stock adjust records for those warehouses and to create 
    different adjust records in different warehouses each day
    """
    warehouse_df = pd.read_csv("warehouse.csv")
    warehouse_list = list(warehouse_df.warehouse_id)
    for warehouse_number in warehouse_list[lower_range:upper_range]:
        record_list = get_adjust_records_in_warehouse(warehouse_number=warehouse_number, record_list=[])
        print(f"Adding Stock Adjust records for warehouse number {warehouse_number} to file.")

        print("\n**********************\n")
        print("***********************")

        record_df = pd.DataFrame.from_dict(record_list, orient="columns")
        record_df.to_csv("stock_adjust.csv", mode='a', index=False, header=True, encoding='utf-8')

        print("Writing to file completed\n")
        print("*************************")

    return

if __name__=='__main__':
    get_adjust_records(upper_range=6)
    get_adjust_records(lower_range=15, upper_range=23)
    get_adjust_records()
