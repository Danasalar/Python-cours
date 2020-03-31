class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Lamb', 'Rabbit', 'Hedgehog']


    def printMembers(self):
        print('Printing members of harmless Mammals') 
        for member in self.members: 
            print('\t%s ' % member)
