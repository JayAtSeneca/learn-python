def blackjack(a,b,c):
    total = sum([a,b,c]) 
    if  total<= 21:
        return total
    else:
        if a == 11 or b == 11 or c == 11:
            total -= 10
            if total > 21:
                return 'BUST'
        else:
            return 'BUST'


