import pprint


def get_shop_list_by_dishes(dishes, person_count):
	ingredients = {}
	for dish in dishes:
		for dish_name, ingredient_list in cook_book.items():
			if dish_name == dish:
				for ingredient in ingredient_list:
					if ingredient["ingredient_name"] in list(ingredients.keys()):
						ingredients[ingredient["ingredient_name"]]["quantity"] +=(
								int(ingredient["quantity"]) * person_count)
					else:
						ingredients[ingredient["ingredient_name"]] = \
							{"measure": ingredient["measure"], "quantity": int(ingredient["quantity"]) * person_count}
	return ingredients


with open('../recipes.txt', encoding='utf-8') as file:
	cook_book = {}
	for line in file.read().split('\n\n'):
		name, _, *args = line.split('\n')
		cook_li = []
		for arg in args:
			arg_list = arg.split(' | ')
			cook_li.append({"ingredient_name": arg_list[0], "quantity": arg_list[1], "measure": arg_list[2]})
		cook_book[name] = cook_li

	print("Словарь с кулинарной книгой cook_book:\n=============")
	pprint.pprint(cook_book, sort_dicts=False)
	print("\nПодсчёт количества продуктов:\n=============")
	pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

