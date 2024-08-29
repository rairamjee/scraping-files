import requests
import pandas as pd

url = 'https://uk.misumi-ec.com/api_cms/en/navigation.json?_=1724907092424' 
# https://uk.misumi-ec.com/api_cms/en/navigation.json?_=1724913780669
headers = {'User-Agent': 'Mozilla/5.0'}
 
def fetch_response():
    # try:
        response = requests.get(url, headers=headers)
       
 
        response.raise_for_status()
       
 
        body = response.json()
        products = body.get("navigation", [])[0]  # Get the first item from 'navigation'
        # print(products)

        items = products.get("items", [])  # Get items, which should be a list
        # print(items)

        # List to store extracted data
        data = []
 
    #     # Iterate through items
        for item in items:
                # print(item)
             
    #         try:
                category = item.get("label")
                sub_categories = item.get("items", [])
                # print(sub_categories)

               
    #             # Iterate through subcategories
                for sub_category in sub_categories:
                    sub_cat_label = sub_category.get("label")
                    sub_cat_items = sub_category.get("items", [])
                    print(sub_cat_items)
                   
                    # Iterate through subcategory items
                    for sub_cat_item in sub_cat_items:
                        item_name = sub_cat_item.get("label")
                        # data.append([category, sub_cat_label, item_name])
                        print(sub_cat_item)
                    break
           
    #         except KeyError:
    #             continue
 
   
    #     df = pd.DataFrame(data, columns=['Category', 'Subcategory', 'Item Name'])
       
 
    #     df.to_csv('categories_subcategories_items.csv', index=False)
    #     print("Data saved to 'categories_subcategories_items.csv'")
 
    # except requests.exceptions.RequestException as e:
       
    #     print(f"Request failed: {e}")
 
 
fetch_response()