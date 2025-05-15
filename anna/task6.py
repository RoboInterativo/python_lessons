#Минимальное 2х значное кратное 5
n=int(input()) #число чисел
l=[]
for i in range(n):
    num=int(input())
    l.append(num)


list7=[]
for num in l:
    if (num>100 and num<=999):
        if num %7==0:
            list7.append(num)


if len(list7)>0:
    min=list7[0]

    for num in list7:
        if num<min:
            min=num

    print(min)
else:
    print("NO")
