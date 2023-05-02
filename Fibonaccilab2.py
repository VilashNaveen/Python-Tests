n = input()

s = [0,1]
for i in range(n-2):
    s.append(s[i]+s[i+1])

print(s)