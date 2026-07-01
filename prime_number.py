#check if a number is prime or not 

num = int(input())

for n in range(2, num + 1):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break
    else:
        print(n)