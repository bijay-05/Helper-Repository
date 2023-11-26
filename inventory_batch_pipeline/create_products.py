from faker import Faker
import random
import pandas as pd


def create_products(brands_list):
    fake = Faker()
    product_category = ['A','B','C','D','E','F','G','H','I']
    product_subcategory = ['AAA','BBB','CCC','DDD','EEE','FFF','GGG','HHH']
    product_list = []
    for brand in brands_list:
        for product_cat in product_category:
            for product_subcat in product_subcategory:
                product_row = {
                  "product_id":random.randint(100,1000),
                  "product_name":fake.word() + str(random.randint(1,100)),
                  "unit_cost": round(random.uniform(10,1000),2),
                  "product_category":product_cat,
                  "product_subcategory":product_subcat,
                  "product_brand":brand
                }
                product_list.append(product_row)

    return product_list

def products_df(products_list):
    products_dataframe = pd.DataFrame.from_dict(products_list, orient='columns')
    products_dataframe.to_csv("products.csv", header=True, index=False, encoding='utf-8')
    return "Products File Creation Successful !!!"


if __name__=='__main__':
    brands_list = ["SAMSUNG","APPLE"]
    product_list = create_products(brands_list)
    print(products_df(product_list))
