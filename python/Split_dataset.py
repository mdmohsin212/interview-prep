data = list(map(int, input().split()))
tarin_ratio = float(input())

split_index = int(len(data) * tarin_ratio)
train = data[:split_index]
test = data[split_index:]

print("Train: ", train, ", Test: ", test)