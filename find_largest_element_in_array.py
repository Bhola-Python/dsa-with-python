from array import *

def largest_num(user_input):
    
    
    number_lst = list(map(int, user_input.split()))
    print('The array : ',number_lst)
    
    arr = array('i',number_lst)
    
    largest_int = arr[0]
    
    for num in arr:
        if largest_int <= num: #If current number is greater than or equal to largest_int

            largest_int = num  #Set largest_int to the current number 
            
    print('Largest number : ',largest_int)
    
user_input = input('Enter : ')

largest_num(user_input)