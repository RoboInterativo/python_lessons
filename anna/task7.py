n = input().strip()  # Ввод числа (например, "51224")

l=[]
for i in range(1, len(n) - 1):
    current = int(n[i])
    l.append(current)
