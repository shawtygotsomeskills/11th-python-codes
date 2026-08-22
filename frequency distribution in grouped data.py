mid = [15, 35, 55, 75, 95]
fr = [1, 2, 3, 4, 5]

fx = [f * m for f, m in zip(fr, mid)]

print("After zipping:", fx)

sum_fx = sum(fx)
sum_fr = sum(fr)

mean = sum_fx / sum_fr

print("Mid points:", mid)
print("Frequencies:", fr)
print("Sum of frequency * mid points:", sum_fx)
print("Sum of frequency:", sum_fr)
print("Mean of grouped data:", mean)
