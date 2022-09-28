import random
from time import time

def bubbleSort(L):
    if len(L) < 2:
        return L
    L_sort = L
    test_break = True
    while test_break == True:
        switch_value = 0
        for val in range(len(L)-1):
            pos_1 = val
            pos_2 = val+1
            if L_sort[pos_1] > L_sort[pos_2]:
                L_sort[pos_1], L_sort[pos_2] = L_sort[pos_2], L_sort[pos_1]
                switch_value = 1
        if switch_value  != 1:
            break
    return L_sort
