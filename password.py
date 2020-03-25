results = []

def find_password(number):
    value = list(map(int, str(number)))
    index = 0
    pairs = []
    increasing = True

    for i in range(0, len(value)-1):
        if value[i] > value[i+1]:
            increasing = False
            break
        else:
            if value[i] == value[i+1]:
                pairs.append(value[i])
                if pairs.count(value[i]) >= 2 and len(set(pairs)) == 1:
                    break
                else:
                    pairs.append(value[i])

    if len(pairs) >= 4 and increasing:
        results.append(number)
        index += 1

for x in range(372002, 809992 + 1):
    find_password(x)

print(len(results))
for i in results:
    print(i)
