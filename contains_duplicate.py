st = list(map(int, input().split()))

# seen = set()
# for i in range(len(st)):
#     if st[i] in seen:
#         print("Duplicate found", st[i])
#         break
#     else:
#         seen.add(st[i])
# else:
#     print("No duplicates found")
    
# print("unique elements:", seen)

seen = {}
for i in range(len(st)):
    if st[i] in seen:
        seen[st[i]] += 1
    else:
        seen[st[i]] = 1
print(seen)   