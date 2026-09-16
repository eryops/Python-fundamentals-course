name_list = ['Bengt', 'Berit', 'Jonas', 'Stinga', 'Jeanette']
score_list = [2, 56, 77, 67 ,99, 900] #last number will be skipped because this list is longer then name_list
name_score = list(zip(name_list, score_list))
print(name_score)

name_score_dictionary = dict(zip(name_list, score_list))
print(name_score_dictionary)

product_names = ['rice', 'chicken', 'tomatoes', 'mushroom', 'soda']
product_prices = [45, 89, 77, 190, 2]
product_stock = [34, 67, 7, 19, 234]
products = list(zip(product_names, product_prices, product_stock))
print(products)

for name, score in zip(name_list, score_list):
    print(f"name {name} score {score}")

var1 = 10
var2 = 20
var1, var2 = var2, var1
print(var1)
print(var2)