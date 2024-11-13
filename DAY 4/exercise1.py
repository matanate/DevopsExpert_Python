def func(input_list):
    num_list = []
    letters_list = ""
    for i in input_list:
        if type(i) is int:
            num_list.append(i)
        else:
            letters_list += i
    return letters_list, num_list


print(func([1, "a", 2, "b", "v", 3]))
