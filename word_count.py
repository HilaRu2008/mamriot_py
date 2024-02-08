

def read_file(file_path):
    """
    this func read a file with a given path and returns the content of the file
    :param file_path: the path of the file (str)
    :return: the content in the file (str)
    """

    with open(rf"{file_path}", "r") as my_file:
        content = my_file.read()

    return content



def str_to_lst(file_content):
    """
    this func turns a file of words into a list of words
    :param file_content: the content of the file (str)
    :return: a list of every word in the file (list)
    """
    # remove any '\n' from the text
    num_of_line_break = file_content.count('\n')
    file_content = file_content.replace('\n', " ", num_of_line_break)

    # lower all upper letters in the string
    file_content = file_content.lower()

    # make a list of lower words of the text
    list_of_words = file_content.split(" ")
    return list_of_words



def add_words(list_of_words):
    """
    this func adds the words of the list of words to a dictionary together with the value as the number of times they appear
    :param list_of_words: the list of all the words
    :return: the dictionary with the words and values
    """

    dictionary = {}
    for word in list_of_words:  # go over every word in the list of words
        num_of_word = list_of_words.count(word)  # count the am amount of times the word appear
        dictionary[word] = num_of_word  # add the word to the dictionary with the amount of time it appears
    return dictionary


def main():

    content = read_file(r"C:\Users\naama\Downloads\hila_work\text_for_dictionary.txt")  # the content of the file
    lst_of_words = str_to_lst(content)  # the list of words
    dictionary = add_words(lst_of_words)  # the final dictionary with the words
    print(dictionary)

if __name__ == '__main__':
    main()
