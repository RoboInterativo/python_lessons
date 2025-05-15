#Минимальное 2х значное кратное 5
n=int(input()) #число чисел
l=[]
for i in range(n):
    num=int(input())
    l.append(num)


list5=[]
for num in l:
    if (num>10 and num<=99):
        if num %5==0:
            list5.append(num)





min=list5[0]

for num in list5:
    if num<min:
        min=num

print(min)
