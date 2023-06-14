# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#讀取檔案
products = []
with open('products.txt','r', encoding='utf-8') as f:
    for line in f:
        if '商品,價格' in line:
            continue
        name, price = line.strip('\n').split(',')
        products.append([name, price])

# products = []
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
with open('products.txt', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')