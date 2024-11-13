import string


def hello_counter(file_url, message):
    with open(file_url, "w+") as file:
        file.write(message)
        file.seek(0)
        words_list = file.read().lower().split()
        hello_count = words_list.count("hello")
    return hello_count


print(hello_counter("file.txt", "hello my name is Hello HELLO"))


def hello_counter(file_url, message):
    with open(file_url, "w+") as file:
        file.write(message)
        file.seek(0)
        words_list = file.read().lower().strip().split()
        hello_count = 0
        for word in words_list:
            if word.strip(string.punctuation) == "hello":
                hello_count += 1
    return hello_count


print(hello_counter("file.txt", "hello! my name is Hello. HELLO"))
