i = 0
while i <= 30:

    if i % 2 == 0:
        print(i, sep=' ', end=' ')
    i += 1

print()



i = 65
k = 0
while i < 91:
    print(chr(i), sep=' ', end=' ')
    k += 1
    if k % 5 == 0:
        print()
    i += 1
print()



i = 65
j = 97
k = 0
while i < 91:
    print(chr(i), chr(j), sep=' ', end=' ')
    k += 1
    if k % 5 == 0:
        print()
    i += 1
    j += 1


i = int(input("Please enter a number for beginning:"))
j = int(input("Please enter a number for ending:"))
k = 0
while i <= j:
    print(chr(i), sep=' ', end=' ')
    k += 1
    if k % 5 == 0:
        print()
    i += 1

