#Python program for implementation of Bubble Sortd

def bubble_sort(alist):

    for i in range(len(alist) - 1, 0, -1):
        no_swap = True
        for j in range(0, i):

            #traversing the array from 0 to n-1-i
            #swapping the element if it si found greater than the nect element
            if alist[j + 1] < alist[j]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                no_swap = False

        if no_swap:
             # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            
            return
 
 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
bubble_sort(alist)
print('Sorted list: ', end='')
print(alist)

#Time complexity of this algorithm is O(n^2);
#Space complexity of this algorithm is O(1);
