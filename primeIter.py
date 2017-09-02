from math import sqrt
def prime(start, stop):
    primeList = []
    for i in range(start, stop):    
        for j in range(2, int(sqrt(stop))):
            if i % j == 0:
                break
        else:
            yield i
    return i
