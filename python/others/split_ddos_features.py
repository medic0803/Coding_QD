features = []
values = []
while True:
    raw = input()
    if len(raw) == 0:
        break
    features.append(raw.split()[:-1])
    values.append(raw.split()[-1])

# for algorithm

feature_line = ["\"" + ' '.join(features[n]) + "\"" for n in range(len(features))]
print(', '.join(feature_line))

# excel
print('\n'.join(feature_line))

print('\n'.join(values))
