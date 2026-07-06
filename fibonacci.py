#n = int(input())

# a,b = 0,1
# for _ in range(0,n):
#     print(a, end=" ")
#     a,b = b, a + b


###### using functions #########
# def fib(n):
#     a,b = 0,1
#     for _ in range(0,n):
#         print(a, end=" ")
#         a,b = b , a+b

# n = int(input())
# fib(n)

###### print fibonacci series as a list ######

# def fib(n):
#     result = []
#     a,b = 0,1
#     for _ in range(0,n):
#         a,b = b , a+b
#         result.append(a)
#     return result

# n = int(input())
# print(fib(n))


##### Check if a number is Fibonacci ####
# def fib(c):
#     a,b = 0,1
#     while a < c:
#         a,b = b , a+b
#     return a == c

# c = int(input())
# if fib(c):
#     print(c,"is in Fibonacii series")
# else:
#     print(c,"not in Fibonacci series")


################ using recursion #######

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
n = int(input())
for i in range(0,n):
    print(fib(i), end=" ")
   