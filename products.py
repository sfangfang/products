# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os

products = []
if os.path.isfile('products.csv'):
    print('yeh')
    #讀取檔案
    with open('products.csv','r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip('\n').split(',')
            products.append([name, price])
else:
    print('No')

while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入價格: ')
    products.append([name, price])

for p in products:
    print(p[0], '的價格是', p[1])
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')