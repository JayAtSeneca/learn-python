from secrets import choice


game_list = [0,1,2]

def display_game(game_list):
    print('Here is the current List')
    print(game_list)

def position_choice():
    choice = 'wrong'
    while choice not in ['0','1','2']:
        choice = input("Pick a position (0,1,2): ")
        if choice not in ['0','1','2']:
            print('Sorry, wrong choice!')
    return int(choice)

def replacement_choice(game_list,positon):
    userInput = input('Type a string for replacement: ')
    game_list[positon] = userInput
    return game_list

def gameOn_choice():
    choice = 'wrong'
    while choice not in ['Y','N','y','n']:
        choice = input('Enter your choice (Y or N): ')
        if choice not in ['Y','N','y','n']:
            print('Please enter Y or N')
        if choice == 'Y' or choice== 'y':
            return True
        else:
            return False