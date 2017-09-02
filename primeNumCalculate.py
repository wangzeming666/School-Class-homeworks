from math import sqrt
primeNumList = []
num = int(input("Enter a number:"))
while num != 1:
    for i in range(2,int(sqrt(num))+1):
        if num % i == 0:
            primeNumList.append(i)
            num = int(num/i)
    else:
        break
num = primeNumList.pop()
# 打印 
for i in primeNumList:
    print('',i,'*',end='')
print('',num)
