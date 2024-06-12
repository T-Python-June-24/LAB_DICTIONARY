
def arrange(L:list) -> list:
    L.sort()
    L.reverse()
    return L

List= [5, 0, 34, 9, 0, 13, 8]

print(f"The arranged list: {arrange(List)}")
