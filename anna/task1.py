n = input().strip()  # Ввод числа (например, "51224")
hills = 0  # Счётчик "горок"
valleys = 0  # Счётчик "ям"

for i in range(1, len(n) - 1):
    current = int(n[i])
    prev = int(n[i - 1])
    next_ = int(n[i + 1])

    if current > prev and current > next_:
        hills += 1
    elif current < prev and current < next_:
        valleys += 1

print(hills, valleys)
