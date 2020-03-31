from .die import Die

from .utils import i_just_throw_an_exception

class GameRunner:
    
    

    def __init__(self):
        
        self.dice = Die.create_dice(5)
        
        self.reset()

    def reset(self):
        
        self.round = 1
        self.win = 0
        self.lose = 0

    def answer(self):
        total = 0
        for die in self.dice:
            
######------total += 1 
            
            total += die.value #corrected
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        c = 0
        win = 0  #corrected
        lose = 0  #corrected
        
        while True:
            runner = cls()
            c += 1  #corrected
            
 #######----print("Round {}\n".format(runner.round))-----------------------

            print("Round {}\n".format(c))#corrected

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
 #######----print("Congrats, you can add like a 5 year old...")----------------
                print("Well done") #corrected
 ########-------runner.wins += 1
 ########-------c += 1
                win += 1  #corrected
            else:
                
                 print("Sorry that's wrong")
                 print("The answer is: {}".format(runner.answer()))
                 print("Like seriously, how could you mess that up")
 ########-------runner.loses += 1
 ########-------c = 0
                 lose += 1    #corrected
 ########-------print("Wins: {} Loses {}".format(runner.wins, runner.loses))
 ########-------runner.round += 1
            print("Win: {} Lose {}".format(win, lose)) #corrected
             
             
            if c == 6:
                
                if win == 6: #corrected
                
                     print("You won... Congrats...")
# I think this line is not needed----print("The fact it took you so long is pretty sad")
                else: #corrected
                     print("You lose") #corrected
    
                break

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt == 'y' or prompt == '':
                continue
            elif prompt == 'n':
                print("You lose")
            else:
                i_just_throw_an_exception()
