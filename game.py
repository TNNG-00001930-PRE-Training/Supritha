import random
while True:
    ur_name=input("Your name ? ")
    print("Welcome to the game ",ur_name)
    print("I have picked a number between 1 and 100!! Try to guess it!!")
    number=random.randint(1,100)
    trials=7
    while trials>0:
        guess=int(input("Try to guess the number I chose: "))
        if guess==number:
            print("Hurray you won,Congratulations You guessed it correct ",number)
            break
        elif guess<number:
            print("Ohoh its Too low,Try again")
            trials-=1
        else:
            print("Oh Its too high,Try again")
            trials-=1
    if trials==0:
        print("out of chances , The correct number was ",number)
    play=input("do u want to play again??(yes/no) ").lower()
    if play!='yes':
        print("Thank you ")
        break
    