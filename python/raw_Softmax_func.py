import numpy as np
nums = list(map(float, input().split()))

def softmax(x):
    ex = np.exp(x - np.max(x))
    return ex / ex.sum()

print(softmax(nums))