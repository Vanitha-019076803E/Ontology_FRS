from owlready2 import *


def check_if_user_eats_the_ingredient(user, ingredients, ingredients_in):
    specific_ingredient = input(
        "Enter a specific ingredient to check whether the user eats it: ")
    v = user.eats
    count = 0
    instances = []
    for j in ingredients:
        if j.name.lower() == specific_ingredient.lower():
            if j.name not in instances:
                instances.append(j.name)
                ingredients_in = True
                print("Ingredient found")

                for i in v:
                    if(j in i.instances()):
                        count = count+1
                        print(f"{user} eats {specific_ingredient}")
                if count == 0:
                    print(f"{user} does not eat {specific_ingredient}")

    if ingredients_in == False:
        print("Ingredient not found")


def get_food_user_eats(user):
    v = user.eats
    for i in v:
        print(f"Ingredients that {user.name} eats:")
        print(i.instances())


def get_food_user_does_not_eat(user):
    v = user.doesNotEat
    for i in v:
        print(i.instances())


if __name__ == "__main__":
    user = input("Enter the user: ")
    onto = get_ontology(
        "/Users/venkateshwaran/Downloads/FoodMenuDisplay/expectation-backend/FoodMenu.owl").load()
    users = list(onto.User.subclasses())
    users_list = []
    complete_users_list = []
    dummy_list = []
    for i in users:
        if len(list(i.subclasses())) > 0:
            users_list.append(i)
            dummy_list = list(i.subclasses())
        else:
            users_list.append(i)

    complete_users_list = users_list + dummy_list

    # print(complete_users_list)
    ingredients = list(onto.Food.instances())
    user_in = False
    ingredients_in = False

    for i in complete_users_list:
        if i.name.lower() == user.lower():
            user_in = True
            print("User found")
            get_food_user_eats(i)
            get_food_user_does_not_eat(i)
            check_if_user_eats_the_ingredient(i, ingredients, ingredients_in)

    if user_in == False:
        print("User not found")
