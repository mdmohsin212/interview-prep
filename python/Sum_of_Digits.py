nums = input()

# option 1
print(sum(map(int, nums)))

# option 2
print(sum(int(d) for d in nums))