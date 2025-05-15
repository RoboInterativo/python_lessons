n = input().strip()

interes=0
for i in range(1, len(n) - 1):
    current = int(n[i])%2==0



    prev = int(n[i - 1])%2==0
    next_ = int(n[i + 1])%2==0

    if (current and prev and next_)==True:
        interes=interes+1
    if (current and prev and next_)==False:
            interes=interes+1

print(interes)
