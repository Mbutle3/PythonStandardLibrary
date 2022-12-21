# Math Module
import math

# Constants
print(math.pi)  # 3.14
print(math.e)  # e
print(math.nan)  # not a number
print(math.inf)  # infinity
print(-math.inf)  # negative infinity
# Trig
print(math.sin(math.pi / 4))
print(math.cos(math.pi / 4))
print(math.cos(math.pi / 4) + math.sin(math.pi / 4))
print(math.tan(math.pi / 4))
print()
# Ceiling and Floor
cookies = 10.1
candy = 7.9
print(math.ceil(cookies))  # Round up to closest integer (10.1 -> 11)
print(math.floor(candy))  # Round down to closest integer (7.9 -> 7)
# Factorial and square root
print(math.factorial(3))  # 3 + 2 + 1
print(math.sqrt(64))
# Greatest Common Denominator - useful for reducing fractions
# 8/52 -> 2/13; GDC Between 8 and 52 is 4
print(math.gcd(52, 8))  # returns GDC 4
print(math.gcd(8, 52))  # order does not matter
print(8 / 52)
print(2 / 13)
# Convert Radians and Degrees
print(math.radians(360))
print(math.pi * 2)
print(math.degrees(math.pi * 2))
print()

# Random Module
import random as rand

print(rand.random())  # range number between 0 and 1
decider = rand.randrange(2)
if decider == 0:
    print("heads")
else:
    print("tails")
print(decider)  # will return a value between 0 and 1
print("You rolled a " + str(rand.randrange(1, 7)))  # dice from 1 - 6
# Random Choices
lotteryWinners = rand.sample(range(100), 5)  # taking a sample of 100 people and picking 5 winners
print("The winning ticket numbers: " + str(lotteryWinners))
possiblePets = ["kittens", "puppies", "fish", "turtles", "parrots"]
print("They won: " + rand.choice(possiblePets))  # randomly pick an item in the list
cards = ["Jack", "Queen", "King", "Ace"]
rand.shuffle(cards)  # shuffle order of elements
print(cards)
print()

# Statistics Module
import statistics as stats

agesData = [2, 2, 3]
print(stats.mean(agesData))  # average
print(stats.median(agesData))  # midpoint
print(stats.mode(agesData))  # most frequent
agesData2 = [10, 13, 14, 12, 11, 10, 11, 10, 15]
print(stats.mean(agesData2))  # average
print(stats.median(agesData2))  # midpoint (11) 11 assuming data is sorted
print(sorted(agesData2))
print(stats.mode(agesData2))  # most frequent
# variance: the average of the squared differences from the mean
print(stats.variance(agesData))  # [ (2 - 2.33) * 2 + (2 - 2.33) * 2 + (3 - 2.33) * 2] / (3 - 1) -> 1/3 or .333
print(stats.variance(agesData2))  # the average of the squared differences from the mean
# standard deviation: the square root of the variance
print(stats.stdev(agesData))  # square root of (1/3)
print(math.sqrt(stats.variance(agesData)))
print(math.sqrt(1 / 3))
print(stats.stdev(agesData2))
print(math.sqrt(stats.variance(agesData2)))
print()

# Itertools Module
import itertools

# Infinite Counting
print("Counting from 1 to 5")
for x in itertools.count(1):
    print("Currently at: " + str(x))
    if x == 5:
        print('Stopping Cycle')
        break
print('Counting to 80 by 5s starting at 50')
for x in itertools.count(50, 5):
    print('Currently at: ' + str(x))
    if x == 80:
        print("Stopping loop.")
        break
x = 0
# Infinite Cycling
for c in itertools.cycle("racecar"):
    print(c)
    x = x + 1
    if x > 10:
        print('Stopping Cycle')
        break
x = 0
for c in itertools.cycle([1, 2, 3, 4]):
    print(c)
    x = x + 1
    if x > 7:
        print('Stopping Cycle')
        break
x = 0
for r in itertools.repeat(True):
    print(r)
    x = x + 1
    if x == 2:
        print("Stopping loop")
        break

# Permutations and Combinations

"""Permutations: A way, especially one of several possible variations, 
                 in which a set or number of things can be ordered or arranged                  
                 Permutations of [1,2,3]: **same items in different orders**
                                 (1,2,3)   (3,1,2)
                                 (1,3,2)   (2,3,1)
                                 (3,2,1)   (2,1,3)
"""

# Permutations: Order matters - some copies with same inputs but in different order
import itertools

election = {1: "Barb", 2: "Karen", 3: "Erin"}
for p in itertools.permutations(election):  # get permutations of keys
    print(p)
print("stopping loop")
for p2 in itertools.permutations(election.values()):  # get permutations of value
    print(p2)
print("stopping loop")
"""Combinations: No set will have the same exact elements as another
                 Combinations of 2 from [work, eat, pay]
                  (work, eat), (work, play), (eat, play)
"""
# Combinations: Order doesn't matter
# list all the painting combinations that can be made with 2 paint colors
colorsForPainting = ['Red', 'Blue', 'Green']
for c in itertools.combinations(colorsForPainting, 2):
    print(c)
print("stopping loop")
colorsForPainting2 = ['Red', 'Blue', 'Purple', 'Orange', 'Yellow', 'Green']
for c in itertools.combinations(colorsForPainting2, 2):
    print(c)
print("stopping loop")

