from array import *

def find_second_largest(user_input):
    number_lst = list(map(int, user_input.split()))
    
    print('The array : ',number_lst)
    
    arr = array('i',number_lst)
    
    # find the largest element 
    largest = float(" -inf ")
    
    for num in arr:
        if num > largest:
            largest = num
            
    second_largest = float(' -inf ') # Find the second largest element (must be less than largest)
    
    for num in arr:
        if num != largest and num > second_largest:
            second_largest = num
     
            
    if second_largest == float(' -inf '): # Handle cases where no second largest exists
        print('No second largest Element ')
    
    else:
        print('Second largest number : ',second_largest)
        
        
user_input = input('Enter Space-separated integer : ')

find_second_largest(user_input)