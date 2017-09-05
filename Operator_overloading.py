import copy
class OrderSet():
    def __init__(self, Set):
        self.Set = Set

    def __and__(self, other):
        set1 = copy.deepcopy(self.Set)
        set2 = copy.deepcopy(other.Set)
        Set = []
        for i in set1:
            if i in set2:
                Set.append(i)
        return Set

    def __or__(self, other):
        set1 = copy.deepcopy(self.Set)
        set2 = copy.deepcopy(other.Set)
        Set = []
        for i in range(len(set1)):
            Set.append(i)
        for i in range(len(set2)):
            if i not in Set:
                Set.add(i)
        return Set

    def __xor__(self, other):
        set1 = copy.deepcopy(self.Set)
        set2 = copy.deepcopy(other.Set)
        Set = []
        for i in set1:
            if i not in set2:
                Set.append(i)
        for i in set2:
            if i not in set1:
                Set.append(i)
        return Set

    def __eq__(self, other):
        set1 = copy.deepcopy(self.Set)
        set2 = copy.deepcopy(other.Set)
        if set1 == set2:
            return True
        else:
            return False

    def __ne__(self, other):
        set1 = copy.deepcopy(self.Set)
        set2 = copy.deepcopy(other.Set)
        if set1 == set2:
            return False
        else:
            return True

    def __contains__(self, other):
        set1 = copy.deepcopy(self.Set)
        set2 = copy.deepcopy(other.Set)
        k = 0
        for i in set1:
            for j in set2:
                if i == j:
                    k += 1

        if k == len(set1):
            return True
        elif k == len(set2):
            return True
        else:
            return False
    
