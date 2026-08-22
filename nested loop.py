for i in range(1, 10):
    if i == 5:
        print("Outer loop i is 5")
    
    for j in range(1, 10):
        if j == 5:
            continue  
        print("Inner j:", j)
