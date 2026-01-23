import math

x = list(map(int, input().split()))
y = list(map(int, input().split()))
lr = float(input())
epochs = int(input())
w = [0.0]
b = 0.0 
m = len(y)

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

for epoch in range(epochs):
    dw = [0.0]
    db = 0.0
    for i in range(m):
        z = w[0] * x[i] + b
        y_pred = sigmoid(z)
        error = y_pred - y[i]
        dw[0] += error * x[i]
        db += error
    
    dw[0] /= m
    db /= m
    w[0] -= lr * dw[0]
    b -= lr * db


predictions = []
for i in range(m):
    z = w[0] * x[i] + b
    y_pred = sigmoid(z)
    predictions.append(1 if y_pred >= .5 else 0)

print("Weights:", [round(w[0], 2)])
print("Bias:", round(b, 2))
print("Predictions:", predictions)