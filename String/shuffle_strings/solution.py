# write a program to shuffle all the strings of a input word

#  Importing random module
import random


#  Defining a function
def shuffle(word):

    #  Converting string to list
    word = list(word)

    #  Shuffling the list
    random.shuffle(word)

    #  Converting list to string
    return ''.join(word)


if __name__ == '__main__':
    #  Taking input from user
    usr_inp = input('Enter a word: ')

    #  Printing shuffled word
    print(shuffle(usr_inp))
