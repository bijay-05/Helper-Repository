from configparser import ConfigParser
import pandas as pd
import psycopg2

def get_connection_object():
    parser = ConfigParser()
    parser.read("config.ini")

    db_keys = {}

    if "postgres" in parser.sections():
      params = parser.items("postgres")
      for param in params:
          db_keys[param[0]] = param[1]

    try:
        print("Let's see what happens with database connection")
        connection_to_db = psycopg2.connect(
          database=db_keys["database"],
          host=db_keys["host"],
          user=db_keys["user"],
          password=db_keys["password"],
          port=db_keys["port"]
        )

        return connection_to_db
    except Exception as ex:
        print("Unfortunately Database connection could not be formed.")
        print(ex)


def insert_records(connection_object: psycopg2.extensions.connection):
    print("Time to set the cursor")
    with connection_object.cursor() as cursar:
        try:
            products_df = pd.read_csv('products.csv')
            products_list = products_df.itertuples(index=False, name=None)

            print("Starting insertion into products table")
            for product in products_list:
                #cursar.execute("INSERT INTO products(product_name,unit_cost,product_category,product_subcategory,product_brand) VALUES (%s,%s,%s,%s,%s)", product)
                #cursar.execute("COMMIT")
            cursar.execute("SELECT COUNT(*) FROM products")
            result = cursar.fetchall()
            print(f"Total records inserted in products table: {result}")

            warehouse_df = pd.read_csv("warehouses.csv")
            warehouse_list = warehouse_df.itertuples(index=False, name=None)

            print("Starting insertion into warehouse table")
            for warehouse in warehouse_list:
                cursar.execute("INSERT INTO warehouse(warehouse_id,address_state,address_city,address_street) VALUES (%s,%s,%s,%s)", warehouse)
                cursar.execute("COMMIT")
            cursar.execute("SELECT COUNT(*) FROM warehouse;")
            result_w = cursar.fetchone()
            print(f"Total records inserted into warehouse table: {result_w}")

            supplier_df = pd.read_csv("suppliers.csv")
            supplier_list = supplier_df.itertuples(index=False, name=None)

            print("Starting insertion into supplier table")
            for supplier in supplier_list:
                cursar.execute("INSERT INTO supplier(supplier_name,address,contact,supplier_since) VALUES (%s,%s,%s,%s)", supplier)
                cursar.execute("COMMIT")
            cursar.execute("SELECT COUNT(*) FROM supplier;")
            result_s = cursar.fetchone()
            print(f"Total records inserted into supplier table: {result_s}")  

            return "Check on PSQL"  
            
        except Exception as er:
            print(er)
            return er
    

if __name__=='__main__':
    connection_object = get_connection_object()   
    status = insert_records(connection_object=connection_object)
    print(status)
