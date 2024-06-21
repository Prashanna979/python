# for x in range(1,11):
#     if x==5 or x==7:
#         continue
#     print(x)
#
# categoryData = [
#     {
#         'category_name': "laptop",
#         'products': [
#             {'id': 1, 'name': 'dell', 'price': 1000},
#             {'id': 2, 'name': 'hp', 'price': 2000},
#             {'id': 3, 'name': 'mac', 'price': 3000},
#             {'id': 4, 'name': 'toshiba', 'price': 5000},
#
#         ]
#     },
#     {
#         'category_name': "mobile",
#         'products': [
#             {'id': 1, 'name': 'samsung', 'price': 10000},
#             {'id': 2, 'name': 'nokia', 'price': 20000},
#             {'id': 3, 'name': 'iphone', 'price': 30000},
#         ]
#     },
#     {
#         'category_name': "tablet",
#         'products': [
#             {'id': 1, 'name': 'samsung', 'price': 1000},
#             {'id': 2, 'name': 'nokia', 'price': 2000},
#             {'id': 3, 'name': 'iphone', 'price': 3000},
#
#         ]
#     },
#
# ]

# for category in categoryData:
#     print(f"Category Name: {category['category_name']}")
#     for product in category['products']:
#         print(f"\t Product Name: {product['name']} Product Price: {product['price']}")
#     print()

# products=[
#     {'id':1,'name':'dell','price':1000},
#     {'id':2,'name':'hp','price':2000},
#     {'id':3,'name':'mac','price':3000},
#     {'id':4,'name':'toshiba','price':5000},
#     {'id':5,'name':'samsung','price':10000},
#     {'id':6,'name':'nokia','price':20000},
#     {'id':7,'name':'iphone','price':30000},
#     {'id':8,'name':'samsung','price':1000},
#     {'id':9,'name':'nokia','price':2000},
#     {'id':10,'name':'iphone','price':3000},
# ]
#
# search=input("enter product name")
# is_found=False
# for product in products:
#     if search== product['name']:
#         is_found=True
#         print(f"product price: {product['price']}")
#
# if not is_found:
#         print("not found")

users=[
    {"uid":1,"name":"ram","address":"ktm"},
    {"uid":2,"name":"sita","address":"ltp"},
]

category=[
    {"cid":1,"name":"laptop"},
    {"cid":2,"name":"mobile"},
    {"cid":3,"name":"tablet"},
]

products=[
    {"pid":1,"name":"dell","price":1000,"category_id":1},
    {"pid":2,"name":"hp","price":2000,"category_id":1},
    {"pid":3,"name":"mac","price":3000,"category_id":1},
    {"pid":4,"name":"toshiba","price":5000,"category_id":1},
    {"pid":5,"name":"samsung","price":10000,"category_id":2},
    {"pid":6,"name":"nokia","price":20000,"category_id":2},
    {"pid":7,"name":"iphone","price":30000,"category_id":2},
    {"pid":8,"name":"samsung","price":1000,"category_id":3},
    {"pid":9,"name":"nokia","price":2000,"category_id":3},
    {"pid":10,"name":"iphone","price":3000,"category_id":3},
]

orders=[
    {"oid":1,"user_id":1,"product_id":1,"quantity":2},
    {"oid":2,"user_id":1,"product_id":2,"quantity":1},
    {"oid":3,"user_id":2,"product_id":3,"quantity":3},
    {"oid":4,"user_id":2,"product_id":4,"quantity":2},
    {"oid":5,"user_id":1,"product_id":5,"quantity":1},
    {"oid":6,"user_id":1,"product_id":6,"quantity":1},
    {"oid":7,"user_id":2,"product_id":7,"quantity":3},
    {"oid":8,"user_id":2,"product_id":8,"quantity":2},
    {"oid":9,"user_id":1,"product_id":9,"quantity":1},
    {"oid":10,"user_id":1,"product_id":10,"quantity":1},
]

username=input("enter your name")
is_found=False

for user in users:
    if username== user['name']:
        is_found=True

