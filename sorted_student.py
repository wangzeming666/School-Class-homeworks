
list1 = []
    
def input_student(file=None):
    if file:
        f = open(file)
        dict1 = {}
        keyList = ['name', 'age', 'score']
        for eachLine in f:
            i = 0
            dict1[keylist[i]] = eachLine
            i += 1
            if i == 3:
                i = 0
        return list1
                            
    dict1 = {}
    dict1["name"] = input("Please enter a name:")
    while len(dict1["name"]) != 0:
        dict1["age"] = input("Please enter the age:")
        dict1["score"] = input("Please enter the score:")
        list1.append(dict1)
        dict1 = {}
        dict1["name"] = input("Please enter a name, enter Enter to quit:")
    return list1

def delite():
    delname = input("Please enter a name that you want delite:")
    dellist = []
    while delname:
        dellist.append(delname)
        delname = input("Please enter a name that you want delite(Enter enter to quit):")
    for j in delname:
        for i in list1:
            if j in i:
                del list1[i] 

def change():
    changename = input("Please enter a name:")
    try:
        for i in range(len(list1)):
            if changename in list1[i]:
                dict1 = {"name": changename}
                dict1["age"] = input("Please enter the age:")
                dict1["score"] = input("Please enter the score:")
                list1.append(dict1)
    except NameError:
        print("There is no one student in student list!")    

def sorted1():
    list11 = []
    list111 = []
    try:
        for i in list1:
            list11.append(i.get("score"))
    except NameError:
        print("There is no one student in student list!")
        return list111
    sorted(list11,key=None,reverse=True)
    for i in list11:
        for j in range(len(list1)):
            if i == list1[j]['score']:
                list111.append(list1[j])
    return list111

def sorted2():
    list11 = []
    list111 = []
    try:
        for i in list1:
            list11.append(i.get("age"))
    except NameError:
        print("There is no one student in student list!")
        return list111
    sorted(list11,key=None,reverse=True)
    for i in list11:
        for j in range(len(list1)):
            if i == list1[j]['age']:
                list111.append(list1[j])
    return list111

def sorted3():
    list11 = []
    list111 = []
    try:
        for i in (list1):
            list11.append(i.get(("score")))
    except NameError:
        print("There is no one student in student list!")
        return list111
    sorted(list11)
    for i in list11:
        for j in range(len(list1)):
            if i == list1[j]['score']:
                list111.append(list1[j])
    return list111


def output_list():
    a, b, c = '-'*10, '+', '|'
    print('+', a, '+', a, '+', a, '+',sep='')
    print('|', "Name".center(10), '|', "Age".center(10), c, "Score".center(10), '|', sep='')
    try:
        for i in list111:
            print('|', a, '+', a, '+', a, '|',sep='')
            print(c, i['name'].center(10), c, i['age'].center(10), c, i['score'].center(10), c, sep='')
    except NameError:
        print('+', a, '+', a, '+', a, '+',sep='')
        print(c,'There is nothing have input'.center(30), c)
        
    print('+', a, '+', a, '+', a, '+',sep='')
