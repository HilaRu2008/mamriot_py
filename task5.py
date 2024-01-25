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
    with open(rf"{file_path}", "r") as my_file:  # open the file
        content = my_file.read()  # read the file
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

    # print(f"Key: {key}")
    # print(f"decrypted Text: {new_text}")

    return new_text


def decrypt_group(group_text, key):
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

    with open(file_path, "a") as file_of_mails:  # open the empty file of miles
        file_of_mails.writelines(list_to_write)  # append the list elements (mails + '\n') to the file




def extract_mails_from_text(text):
    """Gets all the valid mails from the given text

    :param text: the text that should contain the mail addresses
    :type text: str
    :return: The mail addresses that we need to save
    :rtype: list og strings
    """
    lst_of_needed_emails = []
    if is_mail(text):  # if this is the file with the emails
        lst_of_mails = text.split(' ')  # turns text of emails to a list of emails
        for mail in lst_of_mails:  # go over every mail in the list
            if ("hotmail.com" in mail) or ("yahoo.com" in mail) or ("gmail.com" in mail):  # if the email is the with the address we need
                lst_of_needed_emails.append(mail)  # add the email to the list of emails we want to save

        return lst_of_needed_emails


def is_mail(text):
    """Checks if the given mail is valid

    :param text: the mail address to check
    :type text: str
    :return: True if the mail is valid, and False if not
    :rtype: bool
    """
    list_of_emails = text.split(' ') # if the file contains emails, they will be separated with space
    for email in list_of_emails:  # go over the "emails" elements of the lst
        if email.count('@') == 1 and email[0] != '@':  # email valid check
            if (email.count('.') == 1) and (email.index('.') > email.index('@')) and (email.index('.') != email.index('@') + 1) and (email[-1] != '.') :  # email valid check
                return True
            else:
                return False
        else:
            return False




def main():
    # txt1: "C:\Users\Cyber_Mamriot\Desktop\homework\milestone1_A\1.txt"
    # txt2: "C:\Users\Cyber_Mamriot\Desktop\homework\milestone1_A\2.txt"
    # txt3: "C:\Users\Cyber_Mamriot\Desktop\homework\milestone1_A\3.txt"
    # txt4: "C:\Users\Cyber_Mamriot\Desktop\homework\milestone1_A\4.txt"
    # txt5: "C:\Users\Cyber_Mamriot\Desktop\homework\milestone1_A\5.txt"
    # txt_test_5432 : "C:\Users\Cyber_Mamriot\Desktop\homework\milestone1_A\testcase5432.txt"  # input without "" (BC the the input gets it as a text)

    file_of_keys = r"C:\Users\Cyber_Mamriot\Desktop\homework\milestone1_A\keys.txt"
    path_for_mails_needed = r"C:\Users\Cyber_Mamriot\Desktop\homework\milestone1_A\emails_needed.txt"
    key_test = '5432'
    path_of_file_to_read = input("enter path of the file: ")

    # create a list of all the keys in the file
    lst_of_keys = read_file(file_of_keys).split(',')
    # print(lst_of_keys)

    while path_of_file_to_read != '999':

        for my_key in lst_of_keys:  # try every key to decrypt the file

            text_decrypted = decrypt_text(read_file(path_of_file_to_read), my_key)  # call the func that decrypt the file in read_file

            # create a list of mails we need (task 3) if it is a text of emails
            if extract_mails_from_text(text_decrypted) is not None:  # if the decrypted text contains emails

                print("key: ", my_key)
                print("text_decrypted: ", text_decrypted)  # ===== after check - the code only enters the file of mails the last file's mails ("w") =====

                lst_mails_we_need = extract_mails_from_text(text_decrypted)  # creates a list of emails we need

                # add to every element in the list '\n' to insert the emails to the  file as lines and not one line
                for index in range(len(lst_mails_we_need)):
                    lst_mails_we_need[index] = lst_mails_we_need[index] + '\n'
                # print(lst_mails_we_need)

                # the func that adds the mails we need we extracted to a file of mails
                write_to_file(path_for_mails_needed, lst_mails_we_need)

                break  # if a correct decrypted text (text with emails) found stop checking for more keys

        path_of_file_to_read = input("enter path of the file: ")  # input new file for decrypting and checking

    with open(path_for_mails_needed, "r") as file_of_mails:  # maybe using the func? ======
        mails = file_of_mails.read()
        print(mails)



if __name__ == "__main__":
    main()



