x = list(map(int, input().split()))
y = list(map(int, input().split()))
lr = float(input())
w = float(input())
m = len(y)

gradient_sum = 0
for i in range(m):
    y_pred = w * x[i] # y^​= w⋅x
    error = y_pred - y[i] # (y^​ − y)
    gradient_sum += error * x[i] # Σ(y^ ​− y) * x

gradient = gradient_sum / m # 1/m * ​∑(y^​−y)x

w = w - lr * gradient # w − α * 1/m * ​∑(y^​−y)x

print(round(w, 2))