def make_pizza(*toppings):
    print("pizza toppings")
    for topping in toppings:
        print("-",topping)
make_pizza("pepperoni")
make_pizza('mushrooms','cheese')