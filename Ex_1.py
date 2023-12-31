# import os
# import time

cook_book = {}

with open('cook_book.txt', 'rt', encoding='utf-8') as file:
    for f in file:
        name = f.strip()
        dicting = []
        listing = {}
        emplocount = file.readline()
        for i in range(int(emplocount)):
            exdat = file.readline()
            ingredient_name, quantity, measure = exdat.strip().split(' | ')
            dicting.append({'ingredient_name': ingredient_name,
                            'quantity': quantity,
                            'measure': measure})
            nam = {name: dicting}
        blank_line = file.readline()
        cook_book.update(nam)
print(f'cook_book = {cook_book}')
