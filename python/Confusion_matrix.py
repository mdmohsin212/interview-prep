y_true = list(map(int, input().split()))
y_pred = list(map(int, input().split()))

cm = [
    [0, 0],
    [0, 0]
]
for t, p in zip(y_true, y_pred):
    cm[t][p] += 1


# using dict
all_counts = {(0, 1) : 0, (0, 0) : 0, (1, 0) : 0, (1, 1) : 0}
for t, p in zip(y_true, y_pred):
    all_counts[(t, p)]
    
cm2 = [
    [all_counts[(0, 0)], all_counts[(0, 1)]],
    [all_counts[(1, 0)], all_counts[(1, 1)]],
]

print("Using list -> ", cm)
print("Using dict -> ", cm)