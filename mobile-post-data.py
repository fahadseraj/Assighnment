import random
mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'}
    ]
    # 'exchnage_rate': 103.25
}

#  Your Code Starts from here
get_data = mobile_data.get('data')
template2 =[]
# f'It will be Cost for {prices}',
#         # f'Country Of origin is {country_origin}'
for i in get_data:
    mobile_names = i.get('name')
    prices = i.get('price')
     #prices_bd = int(prices) * 103.25
    country_origin = i.get('made')
    template = f'{mobile_names} Price is',f'{prices} In BDT'
    template2.append(template)
    print(prices)


# print(random.choice(template2))