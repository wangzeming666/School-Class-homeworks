high = 100
highCount = 100
for i in range(10):
    high *= 0.5
    highCount += high
print(high, highCount)
