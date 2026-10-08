t = input()
s = input()

if len(t) != len(s):
    print(False)
else:
    c_t = {}
    for i in range(len(t)):
        if t[i] in c_t:
            c_t[t[i]] += 1
        else:
            c_t[t[i]] = 1
    c_s = {}
    for i in range(len(s)):
        if s[i] in c_s:
            c_s[s[i]] += 1
        else:
            c_s[s[i]] = 1
    if c_t == c_s:
        print(c_t)
        print(c_s)
        print(True)
    else:
        print(c_t)
        print(c_s)
        print(False)
    