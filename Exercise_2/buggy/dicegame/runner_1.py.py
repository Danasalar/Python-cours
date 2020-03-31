from .die import Die

from .utils import i_just_throw_an_exception



class GameRunner:



    def __init__(self):

        self.dice = Die.create_dice(5)

        self.reset()



    def reset(self):

        self.round = 1

        self.wins = 0

        self.loses = 0



    def answer(self):

        total = 0

        for die in self.dice:

            #total += 1

            total += die.value

        return total



    @classmethod

    def run(cls):

        # Probably counts wins or something.

        # Great variable name, 10/10.

        c = 0

        wins = 0

        loses = 0

        while True:

            runner = cls()

            c += 1

            #print("Round {}\n".format(runner.round))

            print("Round {}\n".format(c))



            for die in runner.dice:

                print(die.show())



            guess = input("Sigh. What is your guess?: ")

            guess = int(guess)



            if guess == runner.answer():

                #print("Congrats, you can add like a 5 year old...")

                print("Congrats, your answer is correct")

                #runner.wins += 1

                wins += 1

                #c += 1

            else:

                print("Sorry that's wrong")

                print("The answer is: {}".format(runner.answer()))

                #print("Like seriously, how could you mess that up")

                #runner.loses += 1

                loses += 1

                #c = 0

            #print("Wins: {} Loses {}".format(runner.wins, runner.loses))

            print("Wins: {} Loses {}".format(wins, loses))

            #runner.round += 1



            if c == 6:

                if wins == 6:

                    print("You won... Congrats...")

                else:

                    print("The game is over")

                #print("The fact it took you so long is pretty sad")

                break



            prompt = input("Would you like to play again?[y/n]: ")



            if prompt == 'y':

                continue

            if prompt == 'n':

                print("Thank you for playing.")

                break

            else:

                i_just_throw_an_exception()



