# to find the pattern of 0 0 7 in the list
def spy_game(myList):
    listWanted = [0,0,7,'x']
    for num in myList:
        if num == listWanted[0]:
            listWanted.pop(0)
        else:
            pass
    return len(listWanted) == 0