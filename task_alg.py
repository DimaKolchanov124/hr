# a, p, s = 1, 0, 0
# while a <= 10:
#     a += 2
#     p += a
#     s += p
# print(f'переменная s := {s}')
#
# a, p, s = 1, 0, 0
# while True:
#     if a > 10:
#         break
#     a += 2
#     p += a
#     s += p
# print(f'переменная s := {s}')

s_ = 1
for n in range(1, 8):
    s_ *= n
print(s_)

# m = 12
# n = 5
# while True:
#     if m == n:
#         break
#     if m > n:
#         m -= 2*n
#     else:
#         n -= 3
# print(m)