from pprint import pprint
# Открываю файл
with open('cookbook.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        recipe = line.strip()
        ingredient_count = int(file.readline())
        ingredients = []
        for _ in range(ingredient_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredients.append(
                {
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            }
            )
        file.readline()
        cook_book[recipe] = ingredients


print('cook-book - ')
pprint(cook_book, sort_dicts=False)
print('----------------------------------------------')
# Задача2
def get_shoplist_for_persons(list_dishes, person_count):
    shoplist = {}
    for recipe, ingredients in cook_book.items():
        if recipe in list_dishes:
            for ingredient in ingredients:
                name = ingredient['ingredient_name']
                quantity = int(ingredient['quantity'])
                measure = ingredient['measure']
                if name not in shoplist.keys():
                    shoplist[name] = {
                        'measure': measure,
                        'quantity': int(quantity) * person_count
                    }
                else:
                    shoplist[name]['quantity'] += quantity
    return shoplist

pprint(get_shoplist_for_persons(['Омлет', 'Запеченный картофель'], 2))
