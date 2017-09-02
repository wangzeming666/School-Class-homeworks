from time import sleep
def fib(x):
    sleep(0.005)
    if x < 2:return 1
    return( (fib(x-2)+fib(x-1)))

print(fib(5))
