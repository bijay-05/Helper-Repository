import random
import pandas as pd

def get_inventory_in_each_warehouse(warehouseID):
    """
    this function creates fake inventory records for each warehouse
    """
    product_df = pd.read_csv("products.csv")

    # get product id's for each product category and place measure unit accordingly
    inventory_warehouse_list = []
    ## drinks and beverages
    product_list_db = product_df[product_df.product_category == "Drinks and beverages"]["product_id"]
    for product in product_list_db:
        inventory_rec_a = {
          "inventory_id": random.randint(3333,3999),
          "available_quantity": random.randint(111,222),
          "measure_unit": "caret",
          "min_stock": random.randint(30,45),
          "max_stock": random.randint(230,300),
          "reorder_point": random.randint(10,20),
          "warehouse_id": warehouseID,
          "product_id": product
        }
        inventory_warehouse_list.append(inventory_rec_a)

    ## beauty and hygiene
    product_list_hg = product_df[product_df.product_category == "Beauty and hygiene"]["product_id"]
    for product in product_list_hg:
        inventory_rec_b = {
          "inventory_id": random.randint(4333,4999),
          "available_quantity": random.randint(100,200),
          "measure_unit": "cartoon",
          "min_stock": random.randint(22,45),
          "max_stock": random.randint(130,200),
          "reorder_point": random.randint(10,20),
          "warehouse_id": warehouseID,
          "product_id": product
        }
        inventory_warehouse_list.append(inventory_rec_b)


    ## dry fruits and snacks
    product_list_dfs = product_df[product_df.product_category == "Dry fruits and snacks"]["product_id"]
    for product in product_list_dfs:
        inventory_rec_d = {
          "inventory_id": random.randint(5333,5999),
          "available_quantity": random.randint(50,122),
          "measure_unit": "packs",
          "min_stock": random.randint(30,45),
          "max_stock": random.randint(130,200),
          "reorder_point": random.randint(10,20),
          "warehouse_id": warehouseID,
          "product_id": product
        }
        inventory_warehouse_list.append(inventory_rec_d)


    ## daily groceries
    product_list_dg = product_df[product_df.product_category == "Daily Groceries"]["product_id"]
    for product in product_list_dg:
        inventory_rec_e = {
          "inventory_id": random.randint(6333,6999),
          "available_quantity": random.randint(211,322),
          "measure_unit": "KG",
          "min_stock": random.randint(130,145),
          "max_stock": random.randint(330,400),
          "reorder_point": random.randint(50,100),
          "warehouse_id": warehouseID,
          "product_id": product
        }
        inventory_warehouse_list.append(inventory_rec_e)

    inventory_df = pd.DataFrame.from_dict(inventory_warehouse_list, orient="columns")

    inventory_df.to_csv("inventory.csv", mode="a", index=False, header=True, encoding='utf-8')

    return "$$  SUCCESS  $$"


def main():
    """
    this function creates entire inventory data
    """
    warehouse_df = pd.read_csv("warehouse.csv")
    warehouse_id_list = list(warehouse_df.warehouse_id)
    for i,id in enumerate(warehouse_id_list):
        status = get_inventory_in_each_warehouse(warehouseID=id)
        print(f"ROUND {i + 1}  ====>>  {status}")

    return "ALL SUCCESS"

if __name__=='__main__':
    status = main()
    print(status)


