catalog = []
product = {}
count = 1
continuous = True
while continuous:
    product['name'] = input('Input name:')
    product['price'] = float(input('Input price:'))
    product['quantity'] = int(input('Input quantity:'))
    product['unit'] = input('Input unit type:')
    usr_input = input("Enough?( yes or no)")
    if usr_input == 'yes':
        prod_info = (count, product.copy())
        catalog.append(prod_info)
        continuous = False
    elif usr_input == "no":
        prod_info = (count, product.copy())
        catalog.append(prod_info)
        count += 1
        print("Next item")
print(catalog, '\n\n')
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
for i, n in catalog:
    for key, value in n.items():
        analytics[key].append(value)
print("Catalog information:")
print(analytics)
