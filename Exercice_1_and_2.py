from pprint import pprint


def converter():
    cook_book = {}
    with open('cook_book.txt', 'rt', encoding='utf-8') as file:
        for f in file:
            name = f.strip()
            dicting = []
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

    def get_shop_list_by_dishes(dishes, person_count):
        result = {}
        for dish in dishes:
            recipes = cook_book[dish]
            for ingridient in recipes:
                key = ingridient['ingredient_name']
                if key not in result:
                    shoplist = {
                        'measure': ingridient['measure'],
                        'quantity': int(ingridient['quantity']) * person_count

                    }
                    result[key] = shoplist
                else:
                    result[key]['quantity'] += int(ingridient['quantity']) * person_count

        pprint(result)

    get_shop_list_by_dishes(['Фахитос', 'Запеченный картофель', 'Омлет'], 5)


converter()


