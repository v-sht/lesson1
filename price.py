def format_price(price):
    price = int(price)
    return 'Цена: ' + str(price) + ' руб.'

result = format_price(56.24)

print(result)