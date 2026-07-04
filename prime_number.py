#check if a number is prime or not 

num = int(input())

# if num < 2:
#     print(num, "is not a prime")
# else:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print(num, "is not a prime")
#             break
#     else:
#         print(num, "is prime")



###### series of prime number #########

if num <= 2:
    print(num, "is not a prime")
else:
    for n in range(2, num+1):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                break
        else:
            print(n, "is prime")