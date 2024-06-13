
#Q2:Write a function that receives a list containing the following numbers :

# [5, 0, 34, 9, 0, 13, 8]
# rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.

def move_zeros_to_end(ls:list)->list :

    """
    Rearranges the given list so that the zeros are at the end of the list.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        list: The rearranged list with zeros at the end.
    """
    
    rearranged_lst = ls.copy() 

    for i in range(len(rearranged_lst)):
        if rearranged_lst[i] == 0 :
            rearranged_lst.append(rearranged_lst.pop(i)) # will remove the elemnt of index i and append it in the last of list  
    return rearranged_lst

user_lst = [5,0,34,9,0,13,8]

reaaranged_ls = move_zeros_to_end(user_lst)

print(f" \n  the original list is {user_lst} and the reaaranged list is {reaaranged_ls} \n ")