with open('../recipes.txt', encoding='utf-8') as file:
	cook_book = {}

	for line in file.read().split('\n\n'):
		name, _, *args = line.split('\n')
		cook_li = []
		for arg in args:
			arg_list = arg.split(' | ')
			cook_li.append({"ingredient_name": arg_list[0], "quantity": arg_list[1], "measure": arg_list[2]})
		cook_book[name] = cook_li

	print(cook_book)