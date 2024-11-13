def func(input_list):
    try:
        input_list[5] = "a"
    except IndexError as msg:
        print(msg)
    except TypeError as msg:
        print(msg)
    except Exception as msg:
        print(msg)
    else:
        return input_list
    finally:
        print("Function Finished")


func([1, 2, 3, 4, 5, 6, 7])
func([1, 2, 3, 4])
func("a")
func((1, 2, 3))
