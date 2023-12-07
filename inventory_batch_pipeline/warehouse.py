
import random
import pandas as pd
from faker import Faker


from random import randrange

# columns = warehouse id,state, city, street

def get_warehouse():
    """
    this function creates fake warehouse data
    """
    warehouse_list = []
    fakey = Faker()
    states = ['CA','TX','OH','FL','AZ','NJ']
    for i in range(24):
        state_num = random.randint(0,5)
        warehouse_id = random.randint(777,888)
        state = states[state_num]
        city = fakey.word() + " city"
        street = fakey.word() + " " + f"{random.randint(10,89)}"

        warehouse_rec = {
          "warehouse_id": warehouse_id,
          "address_state": state,
          "address_city": city,
          "address_street": street
        }
        warehouse_list.append(warehouse_rec)

    warehouse_df = pd.DataFrame.from_dict(warehouse_list, orient="columns")

    warehouse_df.to_csv("warehouse.csv", mode='w', index=False, header=True, encoding='utf-8')

    return "$$ SUCCESS $$"

if __name__=='__main__':

    status = get_warehouse()
    print(status)
