def read_cook_book():
    cook_book = {}

    with open('list_of_recipes.txt', 'rt', encoding='utf-8') as file:
        key = ''
        ingredients_total = 0
        ingredients_processed = 0
        all_ingredients_list = []

        for line in file:
            if line[0] != '#' and line[0] != '\n':
                line = line.strip('\n').lower()
                if key == '':
                    key = line
                elif ingredients_total == 0:
                    ingredients_total = int(line)
                elif ingredients_processed != ingredients_total:
                    ingredients_processed += 1
                    current_ingredient_list = line.split('|')
                    all_ingredients_list.append({
                        'ingredient_name' : current_ingredient_list[0],
                        'quantity' : current_ingredient_list[1],
                        'measure' : current_ingredient_list[2]
                    })

                    if ingredients_processed == ingredients_total:
                        cook_book[key] = all_ingredients_list
                        key = ''
                        ingredients_total = 0
                        ingredients_processed = 0
                        all_ingredients_list = []

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = read_cook_book()

    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


if __name__ == '__main__':
    create_shop_list()