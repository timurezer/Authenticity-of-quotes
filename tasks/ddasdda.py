summ = 0
n = 3
for i in range(1, 9*n + 1):
    summ += (((i+1)*(i+2)//2)**2+1)//2

print(summ)
