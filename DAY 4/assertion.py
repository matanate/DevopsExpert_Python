def func(input_list):
    assert not len(input_list) < 5, "List to short"
    print(input_list)


func([1, 2, 3, 4, 5, 6])
func([1, 2, 3])
