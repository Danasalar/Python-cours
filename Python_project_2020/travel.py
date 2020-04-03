

#!/usr/bin/env pythonStockholm

#matplotlib inline

from matplotlib import pyplot as plt
import time
import itertools
import inquirer
import random
import sys





class Point(complex):
    x = property(lambda p: p.real)
    y = property(lambda p: p.imag)
    
City = Point

def distance(A, B): 
    "The distance between two points."
    return abs(A - B) 


Stockholm = City(59.320, 18.060)
Uppsala = City(59.870, 17.700)
Gävle = City(60.660, 17.120)
Västerås = City(59.600, 16.550)
Linköping = City(58.510, 13.170)
Göteborg = City(57.690, 11.890)
Karlstad = City(59.390, 13.480)
Borlänge = City(60.48000, 15.420)
Örebro = City(59.280, 15.180)
Mora = City(61.000, 14.540)

##########################


############################


cities = [
            inquirer.List('tours',
                 message = "Cities",
                  choices = ['Stockholm', 'Göteborg', 'Uppsala', 'Gävle', 'Västerås', 'Linköping', 'Karlstad', 'Borlänge', 'Mora'],
            ),
]
answers = inquirer.prompt(cities)
print (answers["tours"])


#####################################
"""

cities_list = []
cities = set(cities_list)
"""
def alltours_tsp(cities):
    "Generate all possible tours of the cities and choose the shortest tour."
  
    return shortest_tour(alltours(cities))

alltours = itertools.permutations 


def shortest_tour(tours): 
    "Choose the tour with the minimum tour length."
    return min(tours, key=tour_length)


def nearest_neighbor(A, cities):
    "Find the city in cities that is nearest to city A."
    return min(cities, key=lambda c: distance(c, A))

def nn_tsp(cities, start=None):
    """Start the tour at the first city; at each step extend the tour 
    by moving from the previous city to its nearest neighbor 
    that has not yet been visited."""
    if start is None: start = first(cities)
    tour = [start]
    unvisited = set(cities - {start})
    while unvisited:
        C = nearest_neighbor(tour[-1], unvisited)
        tour.append(C)
        unvisited.remove(C)
    return tour

list(alltours(cities))

def alltours(cities):
    "Return a list of tours, each a permutation of cities, but each one starting with the same city."
    start = first(cities)
    return [[start] + Tour(rest)
            for rest in itertools.permutations(cities - {start})]

def first(collection):
    "Start iterating over collection, and return the first element."
    return next(iter(collection))

Tour = list  # Tours are implemented as lists of cities

def tour_length(tour):
    "The total of distances between each pair of consecutive cities in the tour."
    return sum(distance(tour[i], tour[i-1]) 
               for i in range(len(tour)))

def valid_tour(tour, cities):
    "Is tour a valid tour for these cities?"
    return set(tour) == set(cities) and len(tour) == len(cities)

######################################----------

def plot_tour(tour):
    "Plot the cities as circles and the tour as lines between them. Start city is red square."
    start = tour[0]
    plot_lines(list(tour) + [start])
    plot_lines([start], 'rs') # Mark the start city with a red square
    plot_labeled_lines(list(tour)+ [start])
    
def plot_lines(points, style='bo-'):
    "Plot lines to connect a series of points."
    plt.plot([p.x for p in points], [p.y for p in points], style)
    plt.axis('scaled'); plt.axis('off')
###############################
    
def plot_tsp(algorithm, cities):
    "Apply a TSP algorithm to cities, plot the resulting tour, and print information."
    # Find the solution and time how long it takes
    t0 = time.clock()
    tour = algorithm(cities)
    t1 = time.clock()
    assert valid_tour(tour, cities)
    plot_tour(tour); plt.show()
    print("{} city tour with length {:.1f} in {:.3f} secs for {}"
          .format(len(tour), tour_length(tour)*100, t1 - t0, algorithm.__name__))
   
    
    

###################################

def plot_labeled_lines(points, *args):
    """Plot individual points, labeled with an index number.
    Then, args describe lines to draw between those points.
    An arg can be a matplotlib style, like 'ro--', which sets the style until changed,
    or it can be a list of indexes of points, like [0, 1, 2], saying what line to draw."""
    # Draw points and label them with their index number
    plot_lines(points, 'bo')
    for (label, p) in enumerate(points):
        plt.text(p.x, p.y, '  '+str(label))
    # Draw lines indicated by args
    style = 'bo-'
    for arg in args:
        if isinstance(arg, str):
            style = arg
        else: # arg is a list of indexes into points, forming a line
            Xs = [points[i].x for i in arg]
            Ys = [points[i].y for i in arg]
            plt.plot(Xs, Ys, style)
    plt.axis('scaled'); plt.axis('off'); plt.show() 
###################################################################
    
    
print(alltours_tsp(cities))
print('')
print('')

print('Distance :', tour_length(alltours_tsp(cities))* 100, 'km')
print('')
print('')

for city in enumerate(cities): 
    print (city)
    
print('')
print('')
plot_tsp(alltours_tsp, cities)
