print("Hello and welcome to my game field")

playGame = input("Are you interested in playing a game? Yes/No ")
print(playGame)

if playGame != "yes":
    print("Good bye")
    quit()

print("Okay, Lets play :) ")

answer1 = input("A request from a client node is made to a? a)Db b)container c)Server   .... Your Answer =")
if answer1 == "c":
    print("Bravo, Well done :)")
else :
    print("Too bad. That was the wrong answer. Better luck next time :(") 
    quit()
