def summer_69(myList):
    stopLoop = False
    retSum = 0
    for num in myList:
        if stopLoop == False or num == 9:
            if num == 6:
                stopLoop = True
            elif num == 9:
                stopLoop = False
            else:
                retSum += num
        else:
            pass
    return retSum