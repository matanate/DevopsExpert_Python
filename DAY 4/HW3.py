# QUESTION 1:
users_dict = {
    ("name", "last_name"): "Matan Atedgi",
    "age": 29,
    "phone number": "0525758426",
}

# print(users_dict)


# QUESTION 2:
def replace_fifth_ex(input_list):
    try:
        input_list[5] = "@"
    except Exception as msg:
        return msg
    else:
        return input_list


# print(replace_fifth_ex([1, 2, 3, 4, 5, 6]))
# print(replace_fifth_ex([1, 2, 3]))
# print(replace_fifth_ex([]))
# print(replace_fifth_ex("A"))
# print(replace_fifth_ex(1))


# QUESTION 3:
def replace_fifth_as(input_list):
    assert len(input_list) > 5, "List to Short, minimum length is 5"
    input_list[5] = "@"
    return input_list


# print(replace_fifth_as([1, 2, 3, 4, 5, 6]))
# print(replace_fifth_as([1, 2, 3]))


# QUESTION 4:
def add_to_dict(dict, key, value):
    dict[key] = value
    return dict


# dict = {}
# print(add_to_dict(dict, "name", "Matan"))


# QUESTION 5:
def create_dict(n):
    if n == 0:
        return {}
    return {n: n + 3} | create_dict(n - 1)


# print(create_dict(5))


# QUESTION 6:
def concatenate_dict(*dicts):
    if dicts == tuple():
        return {}
    return dicts[0] | concatenate_dict(*dicts[1:])


# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# print(concatenate_dict(dic1, dic2, dic3))


# QUESTION 7:
# for loop
def count_chars_for(input_str):
    dict = {}
    for char in input_str:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


# print(count_chars_for("HANNANNN"))


# recursive
def count_chars_rec(input_str, dict={}):
    if input_str == "":
        return dict
    char = input_str[0]
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1
    return count_chars_rec(input_str[1:], dict)


# print(count_chars_rec("HANNANNN"))


# QUESTION 8:
def combine_dict(*dicts):
    new_dict = dicts[0].copy()
    for dict in dicts[1:]:
        for key in dict.keys():
            if key in dicts[0]:
                new_dict[key] += dict[key]
            else:
                new_dict[key] = dict[key]
    return new_dict


# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {"a": 300, "b": 200, "d": 400}
# print(combine_dict(d1, d2))


# CHALLENGE 1:
def fact(n):
    assert not n < 0, "fact() accepts only positive integers"
    if n == 0:
        return 1
    return n * fact(n - 1)


# print(fact(4))


# CHALLENGE 2:
def series_sum(n):
    if n == 0:
        return 0
    return n + series_sum(n - 1)


# print(series_sum(4))


# CHALLENGE 3:
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)


# print(power(3, 2))


# Challenges 1)


# Option 1:
def is_valid_parentheses(input_str):
    open_parentheses = []
    close_parentheses = []
    dict_parentheses = {"(": ")", "{": "}", "[": "]"}
    for char in input_str:
        if char in ("(", "{", "["):
            open_parentheses.append(char)
        elif char in (")", "}", "]"):
            close_parentheses.append(char)
    if close_parentheses == [dict_parentheses[char] for char in open_parentheses][::-1]:
        return True
    else:
        return False


# print(is_valid_parentheses("(())"))

# Option 2:


def is_valid_parentheses(input_str):
    open_parentheses = []
    close_parentheses = []
    dict_parentheses = {"(": ")", "{": "}", "[": "]"}
    for char in input_str:
        if char in ("(", "{", "["):
            open_parentheses.append(char)
        elif char in (")", "}", "]"):
            if (
                len(open_parentheses) == 0
                or char != dict_parentheses[open_parentheses.pop(-1)]
            ):
                return False
            close_parentheses.append(char)
    if len(open_parentheses) == 0:
        return True
    else:
        return False


# print(is_valid_parentheses("(([({()()()})]{))"))


# Challenges 2)


def unique_subsets(input_list):
    subsets = [[]]
    for i, num in enumerate(input_list):
        current_set = [[num]]
        for j in range(i + 1, len(input_list)):
            for k in range(0, len(current_set)):
                current_set.append(current_set[k] + [input_list[j]])
        subsets += current_set
    return subsets


# print(unique_subsets([1, 2, 3, 4, 5]))


def unique_subsets(nums):
    result = [[]]
    for num in nums:
        result += [cur + [num] for cur in result]
    return result


print(unique_subsets([1, 2, 3, 4, 5]))
