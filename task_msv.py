
#
# k, l = [], []
# for i in range(1, 11):
#     k.append(10 -i)
# for i in range(1, 11):
#     l.append(k[5] - k[i - 1])
# print(k)
# print(l)



k, l = list(range(1, 11)), list(range(1, 11))
for i in range(1, 11):
    k[i - 1] = 10 - i
for i in range(1, 11):
    l[i - 1] = k[5] - k[i - 1]
print(k)
print(l)
# count_k = 0
# for value in k:
#     if value < 0:
#         count_k += 1
# count_l = 0
# for value in l:
#     if value < 0:
#         count_l += 1
count_k = len([value for value in k if value < 0])
count_l = len([value for value in l if value < 0])
print(f'колличество отрицательных элементов = {count_k + count_l}')