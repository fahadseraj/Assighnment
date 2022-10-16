mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.6 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110  USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350  USD', 'made': 'Malaysia'}
    ]
    # 'exchnage_rate': 103.25
}

get_data = mobile_data.get('data')
get_item = get_data[3]
get_mobile_name = get_item.get('name')
get_price = get_item.get('price')
get_origin = get_item.get('made')
get_price_rate = get_price[0:4]
get_price_usd = get_price[4:]
get_bdt_str = get_price_usd.replace("USD","BDT")
get_price_bdt = float(get_price_rate) * 103.25
get_price_bdt_round = round(get_price_bdt)
template = f'You Can Choose {get_mobile_name}. Which Price IS {get_price} \nAnd In BD Price Will be {get_price_bdt_round}{get_bdt_str}' \
           f'\nAND Country Of Origin {get_origin} '

print(template)