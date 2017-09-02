from math import sqrt
def prime1(start, stop):
    primeList = []
    for i in range(start, stop):    
        for j in range(2, int(sqrt(stop))):
            if i % j == 0:
                break
        else:
            primeList.append(i)
    return iter(primeList)
[x for x in prime1(1, 100)]

