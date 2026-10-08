price = [2,7,11,15]
target = 9

# flag = False
# for i in range(len(price)):
#     for j in range(i + 1, len(price)):
#         if price[i] + price[j] == target:
#             print(price[i], price[j])
#             flag = True
#             break

# if not flag:
#     print("not found")

seen = {}
for i in range(len(price)):
    comp = target - price[i]
    if comp in seen:
        print(price[i],comp)
        break
    else:
        seen[price[i]] = i
else:
    print("not found")