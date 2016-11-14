#Create a class what is capable of playing exactly one game of
#Cows and Bulls (CAB). The player have to guess a 4 digit number.
#For every digit that the player guessed correctly in the correct place,
#they have a “cow”. For every digit the player guessed correctly in the
#wrong place is a “bull.”

#The CAB object should have a random 4 digit number, which is the goal
#to guess.
#The CAB object should have a state where the game state is stored
#(playing, finished).
#The CAB object should have a counter where it counts the guesses.
#The CAB object should have a guess method, which returns a string of
#the guess result
#All methods, including constructor should be tested

from random import randint

class Cows_and_bulls():

    def __init__(self):
        self.counter = 0
        self.state = "playing"
        self.number = (randint(1,9), randint(0,9), randint(0,9), randint(0,9))

        print("Hello, what's your name?")
        player_name = input()
        self.player_name = player_name

        print("Welcome " + player_name + ", we are going to play a game of cows and bulls.\nYou will have to guess a 4 digit number between 1000 and 9999.\nFor every digit you guess right, you will receive a cow, and for every wrong guess, a bull.\nAre you ready to begin? Y/N")
        player_ready = input()

        if player_ready == "Y" or player_ready == "y" or player_ready == "yes" or player_ready == "YES":
            self.play()
        else:
            quit()

    def play(self):
        output = []
        while self.state == "playing":
            print("Guess a number between 1000 and 9999!")
            player_guess = input()

            if any(i.isdigit() for i in player_guess) is False:
                print("Please enter a valid number!")
                return self.play()
            if len(player_guess) != 4:
                print("The number has to have 4 digits!")
                return self.play()
            else:
                self.counter += 1
                for x in range(len(player_guess)):
                    if int(player_guess[x]) == self.number[x]:
                        output.append("cow")
                    else:
                        output.append("bull")

                if output == ["cow", "cow", "cow", "cow"]:
                    self.state = "finished"
                    break
                else:
    #                print(self.number) #if you enable this, it will show the number you have to guess!
                    print("The result of your guess is: " + str(output))
                    return self.play()

        if output == ["cow", "cow", "cow", "cow"]:
            print("Congratulations " + str(self.player_name) +"! You guessed the right number with only " + str(self.counter) + " guesses!")
            return self.replay()

    def replay(self):
        print("Would you like to play again? Y/N")
        player_replay = input()

        if player_replay == "Y" or player_replay == "y" or player_replay == "yes" or player_replay == "YES":
            self.play()
        else:
            quit()

newgame = Cows_and_bulls()
newgame.play()
