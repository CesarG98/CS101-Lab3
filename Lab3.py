#welcoming user to game
print('Welcome to the Flarsheim Guesser')

#setting up while loop to continue or exit the game
cont = 'Y'
while cont == 'Y':

    #asking user their number they want to guess, not inputing
    print()
    print('Please think of a number between and including 1 and 100.')
    print()
    
    #setting variable num1 to remainder of guess divided by 3
    num1 = int(input('What is the remainder when your number is divided by 3 ?:'))
    

    while  (num1 < 0 or num1 >= 3):
        while num1 < 0:
            print('The value entered must be 0 or greater')
            num1 = int(input('What is the remainder when your number is divided by 3 ?:'))
        while num1 >= 3:
            print('The value entered must be less than 3')
            num1 = int(input('What is the remainder when your number is divided by 3 ?:'))
        else:
            continue

    #space
    print()

    #setting variable num2 to remainder of guess divided by 5
    num2 = int(input('What is the remainder when your number is divided by 5 ?:'))

    while  (num2 < 0 or num2 >= 5):
        while num2 < 0:
            print('The value entered must be 0 or greater')
            num2 = int(input('What is the remainder when your number is divided by 5 ?:'))
        while num2 >= 5:
            print('The value entered must be less than 5')
            num2 = int(input('What is the remainder when your number is divided by 5 ?:'))
        else:
            continue
    
    #space
    print()

    #setting variable num3 to remainder of guess divided by 7
    num3 = int(input('What is the remainder when your number is divided by 7 ?:'))

    while  (num3 < 0 or num3 >= 7):
        while num3 < 0:
            print('The value entered must be 0 or greater')
            num3 = int(input('What is the remainder when your number is divided by 7 ?:'))
        while num3 >= 7:
            print('The value entered must be less than 7')
            num3 = int(input('What is the remainder when your number is divided by 7 ?:'))
        else:
            continue

    #calculating answer of the guessed number with variable num1,num2, and num3
    #setting answer to variable x
    for i in range(1,101):
        if i % 3 == num1 and i % 5 == num2 and i % 7 == num3:
            x = i
    
    #space
    print()

    #outputing result
    print(f'Your number was {x}')
    print('How amazing was that?')
    print()


    #asking user if they want to play again, repeat if answer isn't Y or N
    cont = str(input('Do you want to play again? Y to continue, N to quit ==>'))
    while (cont != 'Y' and cont != 'N'):
        cont = str(input('Do you want to play again? Y to continue, N to quit ==>'))
            

    
        

    

    

    

     
        
         
        
        
