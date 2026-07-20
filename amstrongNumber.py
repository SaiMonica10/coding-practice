n = int(input())
l = len(str(n))
a = 0
for i in str(n):
    a += int(i) ** l

if a == n:
    print(n,"yes")
else:
    print(n,"No")