%%writefile products.py
import random
import pandas as pd


def create_products_in_subcategory(brands_list, product_category, product_subcategory):
    
    product_list = []
    for brand in brands_list:
        product_row = {
            "product_id": random.randint(100,1000),
            "product_name": brand + " " + product_subcategory,
            "unit_cost": round(random.uniform(10,1000),2),
            "product_category": product_category,
            "product_subcategory": product_subcategory,
            "product_brand": brand
        }
        product_list.append(product_row)

    return product_list

def convert_list_to_csv(product_list):
    """
    outputs CSV file for each product_subcategory
    """
    products_df = pd.DataFrame.from_dict(product_list, orient='columns')
    filename = "products" + str(random.randint(1,40)) + ".csv"
    products_df.to_csv(filename, header=True, index=False, encoding='utf-8')
     return filename

def create_products_in_category(product_category, product_subcategory, brands_2Darray):
    # first create products for each subcategory using above function
    # for each product subcategory we have unique list of brands, so different
    # brands_list must be passed for each product_subcategory

    filename_list = []

    for brand_index, product_subcat in enumerate(product_subcategory):
        print(f"Time for some info {brand_index} : {product_subcat}")
        brands_list = brands_2Darray[brand_index]
        product_list = create_products_in_subcategory(brands_list=brands_list, product_category=product_category, product_subcategory=product_subcat)

        # convert into CSV
        file_name = convert_list_to_csv(product_list)
        filename_list.append(file_name)
        print(f"{brand_index + 1} ROUND SUCCESSFUL !!!")
    
    print("Check out files in Pandas !!!")
    return filename_list


def main():
    # for drinks and beverages
    brands_array = [["tuborg","Gorkha","Nepal Ice","Budweiser","Arna","LondonIce"],
    ["oldmonk","Bacardi","Khukuri"],
    ["JD","OD","Signature","Golden OAK","Black OAK","Black Label"],
    ["Big Master"],
    ["Real"]]

    product_subcategory = ["BEERS","RUM","WHISKEY","WINE","FRUIT JUICE"]

    filename_list = create_products_in_category("Drinks and beverages", product_subcategory, brands_array)

    # for beauty and hygience
    brands_array2 = [["nivea", "vaseline", "himalaya","dove","boroplus","patanjali"],
    ["battas", "plum", "OSHEA", "Lakme", "himalaya"]
    ["nivea", "vaseline", "himalaya","dove","boroplus","patanjali"],
    ["hair& shoulders", "sunsilk", "dove", "patanjali","pantene"],
    ["ugen", "reyon", "laryez", "gyudd"],
    ["pepsodent", "patanjali", "close up", "colgate", "sensodyne"],
    ["rin", "surf excel", "tide", "lifebuoy", "dettol", "lux", "dove"]]

    product_subcategory2 = ["Body Lotion","Sun guards and cream", "face wash", "shampoo", "tissue paper", "tooth paste", "soaps & detergents"]

    filename_list2 = create_products_in_category("Beauty and hygiene", product_subcategory2, brands_array2)

    # for dry fruits & snacks
    brands_array3 = [["haldirams aloo", "haldirams mix", "haldirams moong dal", "haldirams sweet", "bikano aloo", "bikano mix"],
    ["Lays", "Spicy Potato", "Kurkure", "popcorn", "pringles"],
    ["beno dry", "almani", "beeyo", "dini"],
    ["beno dry", "almani", "beeyo", "dini"],
    ["beno dry", "almani", "beeyo", "dini"],
    ["Korean Ramen","Chinsoo", "Current Spicy", "2PM Spicy", "Hot Pot"],
    ["Good day", "Monaco", "Britania", "Marie Gold", "Sugar Free digestive", "BourBourn"]]

    product_subcategory3 = ["Namkeen", "Chips", "Cashews", "Raisins", "Walnut", "Instant Noodles", "Biscuits & Cookies"]

    filename_list3 = create_products_in_category("Dry fruits and snacks", product_subcategory3, brands_array3)

    # for daily groceries
    brands_array4 = [["Hulas","Basmati", "Marsee", "india gate"],
    ["Gyan Chakki", "Bhumi", "Healthy One"],
    ["Monio", "Forever Healthy", "Dhara", "Patanjali"],
    ["Pena","Gyanu","Sanu Chana", "Palm"],
    ["Everest Chilly", "Everest Veggy", "Everest Chicken", "Century Momo", "Century chilly", "Century Chaat"],
    ["Good vinegar", "Garlic Paste"]]

    product_subcategory4 = ["Rice", "Flour", "Olive Oil", "lentils", "Spices", "seasoners"]

    filename_list4 = create_products_in_category("Daily Groceries", product_subcategory4, brands_array4)

    return filename_list + filename_list2 + filename_list3 + filename_list4



def create_single_file(file_name_list):
    #create dataframe for each CSV file and concat all dataframes
    #and finally into single CSV file
    





if __name__=='__main__':
    main()
