highCount = 0
def balldown(high, times):
    global highCount
    highCount += high
    if times == 0:
        return (high, highCount)
    return balldown(high*0.5, times -1)
print(balldown(int(input()),int(input())))
