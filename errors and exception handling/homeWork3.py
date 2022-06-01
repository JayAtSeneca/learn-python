def ask():
    while True:
        try:
            result = int(input('Please enter a number:'))
        except:
            print('An error occurred')
        else:
            break
    print('Thank you the number is:',result**2)