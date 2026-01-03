import math

x = list(map(int, input().split()))
y = list(map(int, input().split()))
lr = float(input())
epochs = int(input())
w = [0.0], b = 0.0, m = len(y)

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

for epoch in epochs:
    