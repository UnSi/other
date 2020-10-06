# import random
#
# lst = [i for i in range(1,11)]
# print(lst)
#
# a = sum(lst[:4])
# b = sum(lst[3:6])
# c = sum(lst[5:9])
# d = sum(lst[8:])+lst[0]
#
# print(a, b, c, d)
#
# while True:
#     random.shuffle(lst)
#     a = sum(lst[:4])
#     b = sum(lst[3:6])
#     c = sum(lst[5:9])
#     d = sum(lst[8:]) + lst[0]
#
#     if a == b == c == d:
#         break
#
# print(a, b, c, d)
# print(lst)

lst = [1, 2, 3, 4]
# lst = [i for i in range(1,11)]


def variate(temp_lst: list, stage=-1):

    if len(temp_lst) == 2:
        print(lst)
        lst[-2], lst[-1] = lst[-1], lst[-2]
        print(lst)
        lst[-2], lst[-1] = lst[-1], lst[-2]
        return

    stage += 1
    for i in range(len(temp_lst)):
        lst[stage], lst[stage+i] = lst[stage+i], lst[stage]
        variate(temp_lst[1:], stage)
        lst[stage + i], lst[stage] = lst[stage], lst[stage + i]


variate(lst)