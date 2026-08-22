dish_ordered = "pasta"
match dish_ordered:
    case " pasta":
        print("chef mario will prepare your pasta")
        cooking_time = 15
    case "pizza":
        print("directing to our pizza station")
        cooking_time= 20
    case "salad":
        print("sending to cold kitchen")
        cooking_time = 10
    case _:
        print("please check our menu for available itmes")
        cooking_time = 0
