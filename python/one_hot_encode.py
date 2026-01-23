labels = list(set(map(str, input().split())))

mapping = {label : idx for idx, label in enumerate(labels)}

encoded = []
for label in labels:
    vector = [0] * len(labels)
    vector[mapping[label]] = 1
    encoded.append(vector)
    
print(encoded)