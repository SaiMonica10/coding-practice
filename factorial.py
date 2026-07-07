# def factorial(n):
#     res = 1
#     for i in range(1,n+1):
#         res *= i
#     return res

# n = int(input())
# print(factorial(n))

############# using recursion #########

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

n = int(input())
print(fact(n))
