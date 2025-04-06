def fibonacci(x=0, y=1, repeat=100):
    if repeat <= 0:
        return y
    return fibonacci(y, x+y, repeat-1)

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

x = fib(12)       
x2 = fibonacci(0,1,12)
print(f"This is the final X: {x}")
print(f"This is the final X2: {x2}")

#both do the same, duh