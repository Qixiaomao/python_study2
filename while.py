number = 23
running = True

while running:
    guess = int(input('Enter the integer:'))

    if guess == number:
     print('Congratulation,you guessed it.')
        #这将导致while循环中止
     running = False

    

    elif guess < number:
     print('No,it is a little lower than that.')

    elif guess > number:
        print('No,it is a little higher than that.')

    else:
     print('The while loop is over.')

print('Done')