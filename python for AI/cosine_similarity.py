import math
nums = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

i = math.sqrt(sum(map(lambda x : x ** 2, nums)))
j = math.sqrt(sum(map(lambda x : x ** 2, nums2)))

dot_p = sum(a * b for a, b in zip(nums, nums2))
ans = dot_p / (i * j)

print(f"{ans:.3f}")