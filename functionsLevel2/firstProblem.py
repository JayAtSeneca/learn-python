def has_33(myList):
    for num in range(0,len(myList) - 1):
        if num == 3 and num + 1 == 3:
            return True
        else:
            pass
    return False
