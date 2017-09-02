dict1 = {}
list1 = []
dict1["name"] = input("Please enter a name:")
while len(dict1["name"]) != 0:
    dict1["age"] = input("Please enter the age:")
    dict1["score"] = input("Please enter the score:")
    list1.append(dict1)
    dict1 = {}
    dict1["name"] = input("Please enter a name:")
a = '-'*10
b = '+'
c = '|'
scoreh = input("Please enter a socre, print higher than this:")
print('|', a, '+', a, '+', a, '|',sep='')
print('|', "Name".center(10), '+', "Age".center(10), b, "Score".center(10), '|', sep='')
for i in range(len(list1)):
    if int(list1[i]["age"]) > int(scoreh):
        print(c, list1[i]["name"].center(10), c, list1[i]["age"].center(10), c, list1[i]["score"].center(10), c, sep='')
print('|', a, '+', a, '+', a, '|',sep='')
