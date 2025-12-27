a = list(map(int, input().split()))

# option 1
print(list(set(a)))

# option 2
print(list(dict.fromkeys(a)))