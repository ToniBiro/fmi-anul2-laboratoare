# with open("intrare.in", 'r') as fin:
#     n = next(fin).split()
#
# n = int(n[0])
# print(n)
#
# pusher = 0
#
# v = [0] * n
# for i in range(n):
#     j = i
#     while j % (n + 1) != 0:
#         j += 1
#     v[j] = 1
#
# for idx, elem in enumerate(v):
#     if elem == 1:
#         print(idx)

x = []
for i in range(0, 100):
    x.append(i)

while True:
    print(x)
    n = len(x)
    if n == 1:
        break
    x = x[::2]
    if n % 2 == 1:
        x = x[1:]

print(x[0]+1)

a = [1, 2, 3, 4, 5]

print(a[::3])