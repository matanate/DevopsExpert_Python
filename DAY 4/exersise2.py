def div(x, y):
    try:
        result = x / y
    except ZeroDivisionError as msg:
        print(msg)
        print("Division by zero")
    except TypeError:
        print("Type error")
    except:
        print("Everything")
    else:
        print(result)
    finally:
        print("Finished")


div(2, 3)
div(2, 0)
div(2, "Alex")
