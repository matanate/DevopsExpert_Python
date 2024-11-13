def count_letters(input_str):
    final_dict = {}
    for i in input_str:
        i = i.lower()
        final_dict[i] = final_dict.get(i, 0) + 1
    return final_dict


# print(count_letters("anaaaaakAAAjnfd"))


def count_words(input_str):
    final_dict = {}
    for word in input_str.split():
        final_dict[word] = final_dict.get(word, 0) + 1
    return set(final_dict.items())


first_set = count_words("a s asd df dsgf dfgh dfh")
second_set = count_words("a s asd df dsgf dfgh dfh asdas sadsad sada")
print(first_set & second_set)
print(first_set ^ second_set)
