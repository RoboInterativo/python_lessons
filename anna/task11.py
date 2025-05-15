n = int(input())
digits = []  # Создаём пустой список для цифр

# Преобразуем число в строку и перебираем каждый символ
for d in str(n):
    digits.append(int(d))  # Добавляем цифру в список как число

hills = 0
valleys = 0

for i in range(1, len(digits) - 1):
    current = digits[i]
    prev = digits[i - 1]
    next_ = digits[i + 1]

    if current > prev and current > next_:
        hills += 1
    elif current < prev and current < next_:
        valleys += 1

print(hills, valleys)
