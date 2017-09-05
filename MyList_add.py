class MyList:
    def __init__(self, List):
        self.List = List

    def __add__(self, rhs):
        for i in rhs.List:
            if i not in self.List:
                self.List.append(i)
        return self.List
    


L1 = MyList([1,2,3,4])
L2 = MyList([3,4,5,6])
L3 = L1 + L2
print(L3)
