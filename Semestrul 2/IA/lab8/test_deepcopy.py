from copy import deepcopy

a = [[1, 2, 3],
     [4, 5, 6]]

b = deepcopy(a)

print(f"a: {a}")

b[0][0] = 100

print(f"a: {a}")
print(f"b: {b}")