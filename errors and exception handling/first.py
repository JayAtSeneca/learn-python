#getting familiar with the syntax of exception handling
try:
    f = open('test.txt', 'r')
    f.write('write a test line')
except TypeError:
    print('there was a type error')
except OSError:
    print('OS ERROR')
finally: #this will always run
    print('I always run')