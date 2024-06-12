lists=[5, 0, 34, 9, 0, 13, 8]
def edit_list(lists:list)-> list:
    '''
    A function that receives a list containing numbers
    It reorders the list so that zeros are the end of the list, and finally returns the ordered list.
    
    Args:
        lists (list): 
    return:
        lists_edit (list): Return values ​​in order
    
    '''
    lists_edit=[]
    lists_zero=[]

    for num in lists:
        if num !=0:
            lists_edit.append(num)
        elif num == 0:
            lists_zero.append(num)
    lists_edit= lists_edit + lists_zero
    return lists_edit

lists=[5, 0, 34, 9, 0, 13, 8]
print(edit_list(lists))