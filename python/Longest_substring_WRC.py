n = int(input())

for i in range(n):
    s = input()
    ans = 0
    left = 0
    pos = {}
    
    for j in range(len(s)):
        c = s[j]
        if c in pos and pos[c] >= left:
            left = pos[c] + 1
        pos[c] = j
        ans = max(ans, j - left + 1)
    
    print(ans)