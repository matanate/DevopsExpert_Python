# Question 1:
print("Output 1:")
identification = ["Matan", "Atedgi", 29, "0525758426"]
for i in identification:
    print(i)

# Question 2:
print("\nOutput 2:")
list_1 = [1, 2, 3, 4, 5]
list_2 = [5, 4, 3, 2, 1]
if len(list_1) != len(list_2):
    print("Error: the lists are not at the same length")
else:
    new_list = []
    for i, j in zip(list_1, list_2):
        if i > j:
            new_list.append(i)
        else:
            new_list.append(j)

print(new_list)

# Question 3:
print("\nOutput 3:")
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
is_str = False
odd_count = 0
even_count = 0
for i in list:
    if isinstance(i, str):
        is_str = True
        break
    elif i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
if is_str:
    print("It’s a string!!!")
else:
    print(
        f"""Number of even numbers : {even_count}
Number of odd numbers : {odd_count}
"""
    )

# Question 4:
print("\nOutput 4:")


def sum_int(list):
    result = 0
    for i in list:
        result += i
    return result


result = sum_int([1, 2, 3, 4])
print(f"The sum of the integers in the list is: {result}")

# Question 5:
print("\nOutput 5:")


def multiple_int(list):
    result = 1
    for i in list:
        result *= i
    return result


result = multiple_int([1, 2, 3, 4])
print(f"The multiplication of the integers in the list is: {result}")


# Question 6:
print("\nOutput 6:")


def min_int(list):
    result = list[0]
    for i in list[1:]:
        if i < result:
            result = i
    return result


result = min_int([1, 2, 3, -1, 4])
print(f"The minimum value of the integers in the list is: {result}")

# Question 6:
print("\nOutput 7:")


def upper_lower_count(str):
    upper_count = 0
    lower_count = 0
    for i in str:
        if i.islower():
            lower_count += 1
        elif i.isupper():
            upper_count += 1
    print(
        f"""No. of Uppercase characters: {upper_count}
No. of Lower case Characters: {lower_count}
"""
    )


upper_lower_count("Alex Kuznetsov")


# Challenge 1:
print("\nOutput Challenge 1:")


def unique_list(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list


result = unique_list([1, 1, 1, 1, 1, 5, 2, 6, 1, 1, 2, 2])
print(result)

# Challenge 2:
print("\nOutput Challenge 2:")
text = ""
for i in range(1, 9):
    text += f"{i}"
    print(text)

# Challenge 3:
print("\nOutput Challenge 3:")

print(
    """
 ****
 *
 *
  ***
     *
     *
 ****"""
)
