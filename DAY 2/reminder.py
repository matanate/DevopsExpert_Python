x = "Python Course"
space_index = x.find(" ")
y = f"{x[space_index + 1:]} {x[:space_index]}"
print(y)