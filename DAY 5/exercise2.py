def new_dict(dict1, dict2):
    final_dict = dict2.copy()
    for i in dict1:
        final_dict[i] = final_dict.get(i, 1) * dict1[i]
    return final_dict


d1 = {"a": 2, "b": 4, "c": 3}
d2 = {"a": 3, "b": -2, "d": 5}
print(new_dict(d1, d2))
