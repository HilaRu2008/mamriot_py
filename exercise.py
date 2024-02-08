def example():
    # >> Write your code here
    return "Hello World!"
    # >>


def ex1(strings):
    """
    The function return the last item in the tuple "strings"
    :param strings: Tuples of strings
    :return: str
    """
    # >> Write your code here
    return strings[-1]
    # >>


def ex2(strings_tuple):
    """
    The function gets a tuple of strings and returns a new tuple with the longest string and it's length
    for example, for the input (“Hello”, “Hi”, “How are you?”, “Bye”)
    output will be: (“How are you?”, 12)
    :param strings_tuple: a tuple of strings
    :return: tuple
    """
    # >> Write your code here
    length = 0
    longest_word = ""
    for string in strings_tuple:
        if len(string) > length:
            length = len(string)
            longest_word = string

    return(longest_word, length)
    # >>


def ex3(key, value):
    """
    The function return a dictionary with one pair of the given key and value
    :return: dict
    """
    # >> Write your code here
    dictionary = {}
    dictionary[key] = value
    return dictionary
    # >>


def ex4(dictionary):
    """
    The function check if the key "Wubbalubbadubdub" is exist in the dictionary
    :param dictionary:
    :return: Boolean (True/False)
    """
    key = "Wubbalubbadubdub"
    # >> Write your code here
    if key in dictionary:
        return True
    else:
        return False
    # >>

def ex5(dictionary):
    """
    The function append the pair {"best student": "betty the bot"} to the given
    dictionary
    :return: None
    """
    # >> Write your code here
    update_dict = {"best student": "betty the bot" }
    dictionary.update(update_dict)
    # >>


def ex6():
    """
    The function will return a dictionary that it's keys are the numbers in the
    range 1 - 100 and the values are the keys as str
    Example: {1: "1", 2: "2", 3: "3" ..}
    :return: dict
    """
    # >> Write your code here
    dict = {}
    for num in range(1, 100):
        dict[f"{num}"] = num
    return dict
    # >>
