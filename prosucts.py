# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入價格: ')
# =============================================================================
#     p = []
#     p.append(name)
#     p.append(price)
#     products.append(p)
# =============================================================================
    products.append([name, price])

for p in products:
    print(p[0], '的價格是', p[1])