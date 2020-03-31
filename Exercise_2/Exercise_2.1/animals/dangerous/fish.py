class Fish:



    def __init__(self):

        self.members = ['Axolotl', 'Telescope Goldfish','Seahorses','Sea-Monkeys','Clownfish','Pufferfish']



    def printMembers(self):

        print('Printing members of dengerous Fish:')

        for member in self.members:

            print('\t%s' % member)