nums = list(map(int, input().split()))

mean = sum(nums) / len(nums)
std = sum((x - mean) ** 2 for x in nums) /len(nums)

print("Mean: ", mean, ", Std: ", std ** 0.5)