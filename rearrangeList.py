def rearrange(numbrList:list):
    tempList = []
    for num in numbrList:
        if num == 0:
            tempList.append(num)
            numbrList.remove(num)
            
    numbrList = numbrList + tempList
    return numbrList


numbers = [5, 0, 34, 9, 0, 13, 8]
rearrangedNumbers = rearrange(numbers)
print(rearrangedNumbers)