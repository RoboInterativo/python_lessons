n = input().strip()
hills = 0
valleys = 0

for i in range(1, len(n) - 1):
    current = int(n[i])
    prev = int(n[i - 1])
    next_ = int(n[i + 1])

    if current >= prev and current >= next_:  # Нестрогое неравенство
        hills += 1
    elif current <= prev and current <= next_:  # Нестрогое неравенство
        valleys += 1

print(hills, valleys)
