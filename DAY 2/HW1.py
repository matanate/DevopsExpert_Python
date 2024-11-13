# Question 1:
print("Output 1:")

_name = "Matan"
last_name = "Atedgi"
_age = 29
phone_number = "0525758426"
print(
    f"""Name: {_name}
Last Name: {last_name}
Age: {_age}
Phone Number: {phone_number}"""
)

# Question 2:
print("\nOutput 2:")

if phone_number[7] == "a" and phone_number[8] == "b" and phone_number[9] == "c" and len(phone_number) > 7:
    print("True")
else:
    print("False")

# Question 3:
print("\nOutput 3:")

x = "abc"
y = "xyz"
z = f"{y[:2]}{x[2:]} {x[:2]}{y[2:]}"
print(z)

# Question 4:
print("\nOutput 4:")

_str = "str"
if len(_str) > 2:
    if _str[-3:] == "ing":
        _str += "ly"
    else:
        _str += "ing"
print(_str)

# Question 5:
print("\nOutput 5:")

mid_index = int((len(_str) - 1) / 2)
new_str = _str[mid_index]
new_str += _str[1:mid_index]
new_str += _str[-1]
new_str += _str[mid_index + 1 : -1]
new_str += _str[0]
print(f"The rotated string is {new_str}")

mid_index = (len(_str) - 1) // 2
new_str = _str[mid_index] + _str[1:mid_index]+ _str[-1] + _str[mid_index + 1 : -1] + _str[0]
print(f"The rotated string is {new_str}")

# Question 6:
print("\nOutput 6:")

str_1 = "Python 3.0"
str_2 = "Tutorial"
result = str_1.replace(" ", f" {str_2} ")
print(result)

# Question 7:
print("\nOutput 7:")

str_7 = "w3resource"
list_7 = list(str_7)
list_7.sort()
result = "".join(list_7)
print(result)

# Question 8:
_float = "12.9999999"
# hard way
print("\nOutput 8 (hard):")

dp_index = _float.find(".")
num_1 = int(_float[:dp_index])
num_2 = int(_float[dp_index + 1 : dp_index + 3])
num_3 = int(_float[dp_index + 3 : dp_index + 4])
if num_3 > 5:
    num_2 += 1
    if num_2 >= 100:
        num_2 -= 100
        num_1 += 1
        if num_2 < 10:
            num_2 = f"0{num_2}"
new_float = f"{num_1}.{num_2}"
print(new_float)
# easy way
print("Output 8 (easy):")

new_float = f"{"{:.2f}".format(float(_float))}"
print(new_float)

# Question 9
print("\nOutput 9:")

_str = "Welcome to w3resource.com"
occures= _str.count("w3resource.com")
print(f"Occures: {occures}")
