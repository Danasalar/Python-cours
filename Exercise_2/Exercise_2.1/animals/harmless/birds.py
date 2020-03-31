class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals 
        self.members = ['Pionus Parrot','Dove','Budgerigar','Hyacinth Macaw','Finch']


    def printMembers(self):
        print('Printing members of the harmless birds:') 
        for member in self.members: 
           print('\t%s ' % member)
