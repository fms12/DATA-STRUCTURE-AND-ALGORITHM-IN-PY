# write a program to shuffle all the strings of a input word
import random           #  Importing random module
def shuffle(word):          #  Defining a function
    word = list(word)       #  Converting string to list
    random.shuffle(word)        #  Shuffling the list
    return ''.join(word)        #  Converting list to string
print(shuffle(input('Enter a word: ')))         #  Taking input from user

if __name__ == '__main__':
    usr_inp = input('Enter a word: ')           #  Taking input from user
    print(shuffle(usr_inp))         #  Printing shuffled word
