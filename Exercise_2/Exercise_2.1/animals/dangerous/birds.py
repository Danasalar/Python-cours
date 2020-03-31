class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals 
        self.members = ['Cassowary','Eagle','Lammergeier','Great horned owl']


    def printMembers(self):
        print('Printing members of dengerous Birds:') 
        for member in self.members: 
           print('\t%s ' % member)
