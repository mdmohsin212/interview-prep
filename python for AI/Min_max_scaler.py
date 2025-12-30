nums = list(map(int, input().split()))
ans = []
for n in nums:
    ans.append((n-min(nums)) / (max(nums) - min(nums)))

print(ans)