# write a program to shuffle all the strings of a input word
import random
def shuffle(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)
print(shuffle(input('Enter a word: ')))

if __name__ == '__main__':
    usr_inp = input('Enter a word: ')
    print(shuffle(usr_inp))
