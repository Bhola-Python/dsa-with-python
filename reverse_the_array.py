from array import *

def reverse_the_array(user_input):

    number_lst = list(map(int, user_input.split()))

    arr = array('i',number_lst)

    print('the array : ',arr)

    reverse_the_array = []

    for i in range(len(arr)-1,-1,-1):
        reverse_the_array.append(arr[i]) # inserting element one by one 

    print('Reversed Array : ',reverse_the_array)


user_input = input('Enter : ')

reverse_the_array(user_input)
