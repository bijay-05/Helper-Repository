
import random
import pandas as pd
from faker import Faker


from random import randrange
from datetime import timedelta, datetime


def random_date(start, end):

    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = delta.days + 88
    random_days = randrange(int_delta)
    return start + timedelta(days=random_days)



def supplier(date_list,state_name):
    supplier_list = []
    fakey = Faker()
    for i in range(23):
        supplier_id = random.randint(22222, 25555)
        supplier_name = fakey.word() + " & CO"
        address = state_name + " " + fakey.word() + f" street {random.randint(1,40)}"
        contact = f"{random.randint(100,400)}" + "-" + f"{random.randint(200,500)}"
        since = random_date(start=date_list[0],end=date_list[1])
        supplier_record = {
          "supplier_id": supplier_id,
          "supplier_name": supplier_name,
          "address": address,
          "contact": contact,
          "supplier_since": since
        }

        supplier_list.append(supplier_record)

    supplier_df = pd.DataFrame.from_dict(supplier_list, orient="columns")

    supplier_df.to_csv("supplier.csv", mode='a', header=True, index=False, encoding='utf-8')

    return " $$  SUCCESS  $$"


if __name__=="__main__":
    date_de = [datetime.strptime("2008-01-10", "%Y-%m-%d"), datetime.strptime("2018-01-10", "%Y-%m-%d")]
    states_list = ['CA','TX','OH','FL','AZ','NJ']
    for state in states_list:
        status = supplier(date_list=date_de, state_name=state)
        print(status)



