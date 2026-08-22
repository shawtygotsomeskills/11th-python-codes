meal_time = 14
if meal_time <11:
    print("serving breakfast menu")
    menu_type = "breakfast"
elif meal_time <16:
    print("serving lunch menu")
    menu_type = "lunch"
elif meal_time < 22:
    print("serving dinner menu")
    menu_type = "dinner"
else:
    print("sorry , kitchen is closed")
    menu_type = "closed"
    
