def is_palindrome(_str):
    for i in range(int(len(_str) / 2)):
        if _str[i] != _str[-i - 1]:
            return False
    return True


print(is_palindrome("abaa"))
