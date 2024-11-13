import string
import os
import re
from typing import List


def get_common_letters(input_string: str) -> List[str]:
    """
    Count the occurrences of letters in the input string
    and return the top 4 common letters sorted by frequency.

    Input:
    - input_string (str): Input string to analyze.

    Output:
    - list: List of the top 4 common letters.
    """
    letter_count = {}
    for char in input_string.lower():
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
    # Return the top 4 common letters sorted by frequency
    return sorted(letter_count)[:4]


def get_cipher_dict(input_string: str) -> dict:
    """
    Map common letters in the input to English letters (e, t, o, r)
    and vice versa, creating a cipher dictionary.

    Input:
    - input_string (str): Input string to create a cipher dictionary.

    Output:
    - dict: Cipher dictionary mapping common letters.
    """
    common_letters = get_common_letters(input_string)
    eng_common_letters = ["e", "t", "o", "r"]
    cipher_dict = {
        **{key: value for key, value in zip(common_letters, eng_common_letters)},
        **{key: value for key, value in zip(eng_common_letters, common_letters)},
    }
    return cipher_dict


def decrypt_str(input_string: str) -> str:
    """
    Decrypt the input string using the cipher dictionary.

    Input:
    - input_string (str): Encrypted input string.

    Output:
    - str: Decrypted string.
    """
    cipher_dict = get_cipher_dict(input_string)
    decrypted_list = []
    for char in input_string:
        if char.lower() in cipher_dict:
            # Preserve the case of the original characters
            if str.isupper(char):
                decrypted_list.append(cipher_dict[char.lower()].upper())
            else:
                decrypted_list.append(cipher_dict[char])
        else:
            decrypted_list.append(char)
    return "".join(decrypted_list)


def decrypt_file(path: str) -> None:
    """
    Decrypt the content of a file and create a new file with the decrypted text.

    Input:
    - path (str): File path.

    Output:
    - None
    """
    try:
        with open(path, "r+") as f:
            # Read the original text from the file
            original_text = f.read()
            # Decrypt the text using the decryption function
            decrypted_text = decrypt_str(original_text)
            # Write the decrypted text back to the original file
            if original_text[-1] == "\n":
                f.write(f"\nThe encryption for the above text is:\n{decrypted_text}")
            else:
                f.write(f"\n\nThe encryption for the above text is:\n{decrypted_text}")
        # Create a new file with the decrypted text
        new_path = path.replace(os.path.basename(path), "result.txt")
        with open(new_path, "w") as f:
            f.write(decrypted_text)
    except FileNotFoundError as e:
        print(f"Error: {e}")


def get_longest_words(path: str) -> list:
    """
    Find the longest word in a file, considering only alphabet letters.

    Input:
    - path (str): File path.

    Output:
    - list: List containing the longest word(s).
    """
    with open(path, "r") as f:
        # Extract words from the file and strip punctuation
        word_list = f.read().split()
        word_list = [word.strip(string.punctuation) for word in word_list]
        # Use regular expression to filter out non-alphabetic characters
        regex = re.compile("[^a-zA-Z]")
        # Sort the words by length in descending order
        word_list.sort(key=lambda x: len(regex.sub("", x)), reverse=True)
        result = []
        for word in word_list:
            # Collect words with the same length as the longest word
            if len(regex.sub("", word)) == len(regex.sub("", word_list[0])):
                result.append(word)
            else:
                break
        return result


def get_line_number(path: str) -> int:
    """
    Count the number of lines in a file.

    Input:
    - path (str): File path.

    Output:
    - int: Number of lines in the file.
    """
    with open(path, "r") as f:
        # Count the number of lines in the file
        line_number = sum(1 for _ in f)
    return line_number


def get_pattern(rows: int) -> str:
    """
    Generate a pattern of '*' characters based on the specified number of rows.

    Input:
    - rows (int): Number of rows in the pattern.

    Output:
    - str: Pattern of '*' characters.
    """
    columns = rows - 2
    pattern = []
    k = -1
    # Loop through the pattern rows.
    for i in range(rows):
        # Loop through the pattern columns.
        for j in range(columns):
            # Add '*' at the beginning and end of the row in the first and last rows.
            if (i == 0 or i == rows - 1) and (j == 0 or j == columns - 1):
                pattern.append("*")
            # Add the x pattern in the rest of the rows.
            elif i != 0 and i != rows - 1 and (j == k or j == columns - 1 - k):
                pattern.append("*")
            # Add space where there should be no '*'
            else:
                pattern.append(" ")
        k += 1
        # Add a newline character at the end of each row
        pattern.append("\n")
    # Convert the list of pattern characters to a string and return
    return "".join(pattern)


def main():
    """
    Main function: Decrypt the content of the file, find the longest word,
    count the number of lines, append the longest word lines time to the file
    and append a pattern to the file.
    """
    # Decrypt the content of the file
    decrypt_file("file.txt")
    # Find the longest word in the file
    longest_word = get_longest_words("result.txt")[0]
    # Count the number of lines in the file
    lines_number = get_line_number("result.txt")
    # Create a string with the longest word repeated for each line
    write_string = " ".join([longest_word] * lines_number) + "\n"
    with open("file.txt", "a") as f:
        f.write(f"\nThe longest word is: {longest_word}")
        f.write(f"\nThe number of lines are: {lines_number}")
        # Append the string to the file
        f.write(f"\nThe requested string is: {write_string}")

    with open("file.txt", "a") as f:
        # Append the pattern to the file
        f.write(f"\n{get_pattern(7)}")


if __name__ == "__main__":
    # Execute the main function when the script is run
    main()
