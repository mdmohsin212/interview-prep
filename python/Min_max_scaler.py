nums = list(map(int, input().split()))
mn = min(nums)
mx =max(nums)

ans = list(map(lambda x : (x - mn) / (mx - mn), nums))
print(ans)