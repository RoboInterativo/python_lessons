n = input().strip()  # Ввод числа (например, "51224")
summa=0

for i in range(n):
    current = int(n[i])
    if current %2==0:
        summa=summa+current
print(summa)
