import json

#Loading Userinput and get distinct colors
user_clothes_json = '{"Jacket":{"color":["black"]},"Pants":{"color":["white"]}}'#,"Shoes":{"color":["black"]}}'
shop_clothes_json = '{"001":{"type":"Jacket","colors":["black","white","blue"]},"002":{"type":"Pants","colors":["black","blue"]},"003":{"type":"Shirt","colors":["black","white","yellow"]},"004":{"type":"Shoes","colors":["black","brown"]}}'
#requested_cloths_json = '[{"name": "Shirt"}]'

rules_json = '{"Jacket":{"mustMatch":["Shirt","Pants"]},"Shirt":{"mustMatch":["Jacket","Pants"]},"Pants":{"mustMatch":["Jacket","Shirt"]},"Shoes":{"mustMatch":["Pants"]},"Tie":{"mustMatch":["Shirt","Shoes"]}}'

shop_clothes = json.loads(shop_clothes_json)
user_clothes = json.loads(user_clothes_json)
rules = json.loads(rules_json)

requested_cloths = ["Shirt", "Shoes"]

in_shop_available_cloths = []

def get_products_ids_from_type(requested_type):
    product_ids = []
    for product_id in shop_clothes:
        if shop_clothes[product_id]['type'] == requested_type:
            product_ids.append(product_id)
    
    return product_ids;

def get_must_match_items(product_type):
    return rules[product_type]['mustMatch'] #example: ['Jacket', 'Pants']

def get_colors_from_user_clothes():
    colors = set()
    for cloth in user_clothes:
        colors.update(user_clothes[cloth]['color'])
    
    return colors

def get_products_in_type_and_color(item_type, must_match_colors):
    product_ids = []
    for product in shop_clothes:
        if shop_clothes[product]['type'] == item_type:
            if set(shop_clothes[product]['colors']).intersection(must_match_colors):
                product_ids.append(product)

    return product_ids;
##Examlpe: User needs a matching shirt for his nice suite!


for requested_item in requested_cloths:

    #Get all the product types which have to match with the requested item
    must_match_items = get_must_match_items(requested_item)
    print("must_match_items: " + str(must_match_items))

    #Define all Colors from user_clothes
    must_match_colors = get_colors_from_user_clothes() 
    print('must_match_colors: ' + str(must_match_colors))

    available_products_in_type_and_color = get_products_in_type_and_color(requested_item, must_match_colors)
    print("available_products_in_type_and_color: " + str(available_products_in_type_and_color))