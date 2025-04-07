def fibonacci(x, dic):
    if x in dic:
        return dic[x]
    else:
        answer =  fibonacci(x-1,dic) + fibonacci(x-2, dic)
        dic[x] = answer
        return answer
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

x = fib(30)       
dic = {1:1, 2:2}
x2 = fibonacci(30,dic)
print(f"This is the final X: {x}")
print(f"This is the final X2: {x2}")

#both do the same, 
#but fibonacci uses a dictionary to dont 
#waste memory with calculus
#we did before