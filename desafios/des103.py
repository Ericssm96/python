def player(name, score=0):
    if len(name) == 0:
        print(f'The mysterious player scored {score} points.')
    else:
        print(f'The player {name} scored {score} points.')


n1 = str(input('Type the name of the player: '))
sc = int(input('How many goals did he score? '))
player(name=n1, score=sc)
