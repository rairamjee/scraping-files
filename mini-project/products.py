import requests
import pandas as pd
 
url = 'https://uk.misumi-ec.com/api_cms/en/navigation.json?_=1724907092424'
 
 
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
 
def fetch_response():
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        body = response.json()
        products = body.get("navigation", [])[0]  # Get the first item from 'navigation'
        items = products.get("items", [])  # Get items, which should be a list
 
        # List to store extracted data
        data = []
 
        # Iterate through items
        for item in items:
            try:
                category = item.get("label")
                sub_categories = item.get("items", [])
               
                # Iterate through subcategories
                for sub_category in sub_categories:
                    sub_cat_label = sub_category.get("label")
                    sub_cat_items = sub_category.get("items", [])
                    print(len(sub_cat_items))
                   
                    # Iterate through subcategory items
                    for sub_cat_item in sub_cat_items:
                        item_name = sub_cat_item.get("label")
                        item_id=sub_cat_item.get("href").split('/')
                        print(item_id)
                        data.append([category,item_id[3], sub_cat_label, item_name,item_id[4]])


                        url_sub=f'https://api.us.misumi-ec.com/api/v1/series/search?lang=ENG&suppressResponseCode=true&applicationId=72c49146-6b86-4155-a63c-499b00972294&_=1724920070194&sessionId=undefined&field=%40search%2CseriesList.templateType&categoryCode={item[4]}&sort=1&allSpecFlag=0&page=1&brandModeFlag=1&pageSize=45'
        
                        try:
                            response=requests.get(url_sub, headers=headers)
                            # print(response)
                            response.raise_for_status()
                            body = response.json()
                            print(body.get("seriesList",[]))
                    
                        except:
                            print("error")       
            except KeyError:
                continue
 
   
        df = pd.DataFrame(data, columns=['Category', 'CategoryId','Subcategory', 'Item Name','SubcategoryId'])
       
 
        df.to_csv('categories_subcategories_items.csv', index=False)
        print("Data saved to 'categories_subcategories_items.csv'")
 
    except requests.exceptions.RequestException as e:
       
        print(f"Request failed: {e}")
 
 
fetch_response()
