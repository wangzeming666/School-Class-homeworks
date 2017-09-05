class MyList:
    def __init__(self, List):
        self.List = List

    def __add__(self, rhs):
        self.List.pop()
        self.List.pop()
        for i in self.List:
                rhs.List.append(i)
                
        return rhs.List
    

l1 = [1,2,3,4]
L1 = MyList(l1)
L2 = MyList([3,4,5,6])
L3 = L1 + L2
print(L3)
print(l1)
