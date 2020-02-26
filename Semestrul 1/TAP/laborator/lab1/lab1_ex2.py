
dict_ = dict()

with open('intrare.in') as fin:
    n = fin.readline()
    n = int(n)
    for indx, line in enumerate(fin):
        data = line.split()
        data.sort()
        for i in range(3):
            for j in range(3):
                if i < j :
                    if (int(data[i]), int(data[j])) not in dict_.keys():
                        dict_[(int(data[i]), int(data[j]))] = [int(data[3-i-j]), 0]
                    else:
                        mini = min(dict_[(int(data[i]), int(data[j]))])
                        if int(data[3-i-j]) > mini:
                            dict_[(int(data[i]), int(data[j]))].remove(mini)
                            dict_[(int(data[i]), int(data[j]))].append(int(data[3-i-j]))

maxi = 0
for key, value in dict_.items():
    print(key, value)
    if maxi < min(key[0], key[1], value[0]+value[1]):
        maxi = min(key[0], key[1], value[0]+value[1])
        the_key = key
        the_value = value

print(f"Raza maxima = {maxi/2}")
print(the_key, the_value)