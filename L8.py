#   Tuples for Recipes


pizza = (" Margherita Pizza","Italian",45,"Easy")
noodles = ("Chicken Noodles","Chinese",30,"Easy")

print("Recipe 1: ",pizza)
print("Recipe 2: ",noodles)



print("Name of Recipe: ",pizza[0])
print("Cuisine of Recipe 1: ",pizza[1])
print("Average Time Taken for Recipe 1: ",pizza[2])
print("Difficulty level to make Recipe 1: ",pizza[3])

all_recipes = (pizza,noodles)

print("Name of Recipe: ",all_recipes[1][0])
print("Average Time Taken: ",all_recipes[1][2])
print("Recipe 1:",pizza[1:4])

#Iterating tuple

print("Details of Noodles Recipe: ")
for detail in noodles:
    print(" -",detail)


#Creating sets for ingredients

pizza_ingredients = {"Cheese","Tomato","Dough","Herbs","Spices","Custom Toppings","Dough"}
noodles_ingredients = {"Noodles","Cooked Chicken","Spices","Boiling Water"}

print("Pizza Ingredients: ",pizza_ingredients)
print("Noodles Ingredients: ",noodles_ingredients)

noodles_ingredients.add("Vegetables")
noodles_ingredients.discard("Cooked Chicken")

print("Vegetarian Noodles Ingredients: ",noodles_ingredients)

#Set operations

all_ingredients = pizza_ingredients.union(noodles_ingredients)
common = pizza_ingredients.intersection(noodles_ingredients)
only_pizza = pizza_ingredients.difference(noodles_ingredients)
unique_to_each = pizza_ingredients.symmetric_difference(noodles_ingredients)

print("\nAll ingredients: ",all_ingredients)
print("Common Ingredients: ",common)
print("Only in Pizza: ",only_pizza)
print("Not shared ingredients: ",unique_to_each)
