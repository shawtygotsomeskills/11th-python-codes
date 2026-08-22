import numpy as np  
arr = np.array([250, 300, 350, 400, 450])
small = arr[0]
for i in arr:
    if i < small:
        small = i
print("Smallest value:", small)  
