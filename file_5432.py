ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
       't', 'u', 'v', 'w', 'x', 'y', 'z', '@', '.', ' ']


def read_file(file_path):
    """Reads the text from a file

    :param file_path: the path of the file to read from
    :type file_path: string
    :return: The text that the file contains
    :rtype: string
    """
    # my_file = open(rf"{file_path}", "r")
    with open(rf"{file_path}", "r") as my_file:
        content = my_file.read()
    return content


def decrypt_text(encrypted_text, key):
    """Decrypt the encrypted text with the given key (by Vigenere encryption algorithm)

    :param encrypted_text: the encrypted text to decrypt (from read_file() func)
    :param key: the key for decryption ( go over the key in a loop + use it when colling in here)
    :type encrypted_text: string
    :type key: string
    :return: The decrypted text
    :rtype: string
    """
    group_separator_value = len(key)
    index = 0
    new_text = ""

    while not index + len(key) > len(encrypted_text):  # repeat until we got to the end of the file (if last index of the new group is bigger than the length of the file- stop)
        group_text = encrypted_text[index: index + len(key)]  # get the group from the text with the length of the full key as the separator
        decrypt_group_ = decrypt_group(group_text, key)  # call the func that Decrypt the group.
        new_text += decrypt_group_  # add the Decrypt group to the decrypt file
        index += len(key)  # get to the first index of the next group

    return new_text


def decrypt_group(group_text, key):  # '5423'
    """Decrypt the encrypted group with the given key (by Vigenere encryption algorithm)

    :param group_text: the encrypted group from the text to decrypt
    :param key: the key for decryption
    :type group_text: string
    :type key: string
    :return: The decrypted group text
    :rtype: string
    """
    deciphered_group = ""
    key_for_index = 0  # start position - index 0

    for letter in group_text:  # go over every letter in the group to give it different offset
        # shift here
        encrypted_letter_index = ABC.index(letter)  # find the index of the letter we want to decrypt
        offset = key[key_for_index]
        deciphered_letter_index = (encrypted_letter_index - int(offset)) % len(ABC)  # calculate the index of the deciphered letter (the letter we want to find)
        key_for_index += 1
        deciphered_group += ABC[deciphered_letter_index]  # add the new letter (in the ABC list) to the group

    # print(deciphered_group, end='')

    return deciphered_group


def write_to_file(file_path, list_to_write):
    """Writes the given list to a file in the given path

    :param file_path: the path of the file to write to
    :param list_to_write: the list to write to the file
    :type file_path: string
    :type list_to_write: list of strings
    """

    pass


def extract_mails_from_text(text):
    """Gets all the valid mails from the given text

    :param text: the text that should contain the mail addresses
    :type text: str
    :return: The mail addresses that we need to save
    :rtype: list og strings
    """
    pass


def is_mail(text):
    """Checks if the given mail is valid

    :param text: the mail address to check
    :type text: str
    :return: True if the mail is valid, and False if not
    :rtype: bool
    """
    pass


def main():
    # txt1: "C:\Users\Cyber_Mamriot\Desktop\homework\milestone1_A\1.txt"
    # txt2: "C:\Users\Cyber_Mamriot\Desktop\homework\milestone1_A\2.txt"
    # txt3: "C:\Users\Cyber_Mamriot\Desktop\homework\milestone1_A\3.txt"
    # txt4: "C:\Users\Cyber_Mamriot\Desktop\homework\milestone1_A\4.txt"
    # txt5: "C:\Users\Cyber_Mamriot\Desktop\homework\milestone1_A\5.txt"
    # txt_test_5432 : "C:\Users\Cyber_Mamriot\Desktop\homework\milestone1_A\testcase5432.txt"  # input without "" (BC the the input gets it as a text)

    key_test = '5432'

    path_of_file_to_read = input("enter path of the file: ")

    file_of_keys = r"C:\Users\Cyber_Mamriot\Desktop\homework\milestone1_A\keys.txt"
    # print(read_file(path_of_file_to_read))  # print th content of the file of keys
    print(decrypt_text(read_file(path_of_file_to_read), key_test))  # call the func that decrypt the file in read_file


if __name__ == "__main__":
    main()
