def fact(a):
    if a == 0:
        return 1
    return a * fact(a - 1)


def sum_values(x):
    if x == []:
        return 0
    return x[-1] + sum_values(x[:-1])


def reverse_list(x):
    if x == []:
        return []
    return [x[-1]] + reverse_list(x[:-1])


print(reverse_list([1, 2, 3]))
