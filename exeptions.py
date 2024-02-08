

def good_luck(name, number):

    try:
        number = int(number)
        print("Your lucky letter is " + name[number - 1])
        print("Your new lucky number is " + str(number/(number - 1)))

    except ValueError:  # if the number is not a int number
        print("the number cannot be anything but an int")
    except IndexError:  # if the number is too big / too small (-) to find the lucky index
        print("the number cnnot be used to find the lucky letter (out of range)")
    except ZeroDivisionError:  # if the number is  1, and than cannot be used to get the new lucky letter
        print("the number - 1 is 0 so it cant be used for a new number")



def main():
    good_luck("Ophir", 2)
    good_luck("Ophir", "2 Ophir")
    good_luck("Ophir", 8)
    good_luck("Ophir", 5)
    good_luck("Ophir", 1)


if __name__ == '__main__':
    main()
