isRaining = True
isSunny = False
if isRaining and isSunny:
    print("Rainbow")
if isRaining or isSunny:
    print("Might be raining or it might be sunny")
if not isRaining:
    print("It's Raining")
elif not isSunny:
    print("It's Sunny")
print()
ages = [12, 18, 39, 87, 7, 2]
for age in ages:
    isAdult = age > 17
    if not isAdult:
        print("Being " + str(age) + " does not make you an adult")
print()
print(10 < 75)
print(75 < 10)
if 10 < 75:
    print("The bigger number is bigger")
print()
cat = 10
tiger = 75
if cat < tiger:
    print("The cat weighs less than the tiger")
mouse = 1
if mouse < cat < tiger:
    print("The mouse weighs the least")
print()

# False --> 0
# True --> 1
# 0 > 1 --> False
print(False > True)
print()

# Looking for first mismatched letter
# A - Z --> 1-26
# > --> greater --> than (c > k)
print("Michael" > "Mike")
print()

# len() --> returns length start = 1, end = n
firstName = "Michael"
lastName = "Butler"
print(len(firstName))
print(len(lastName))
print()
ages = [1, 11, 34, 12, 19]
print(len(ages))
print()
i = 0
for i in range(0, len(ages)):
    print(ages[i])
print()

print(len(["bob", "tim", "sarah"]))
bookCollection = {"bob": 10, "tim": 15, "sarah": 13}
print(len(bookCollection))
print()

# Range -> range instance that holds all nums counting by one between 0 and the first input
# List -> lists numbers from the inputted tuple
numberedContestants = range(30)
print(numberedContestants)
print(list(numberedContestants))
for c in list(numberedContestants):
    print("Contestant " + str(c) + " is here")

# starting at 7 going to 29 counting by 5s
# 7 + 5 = 12, 12 + 5 = 17, 17... 22... 27
luckyWinners = range(7, 30, 5)
print(list(luckyWinners))
print()

# Minimum and Maximum
playerOneScore = 10
playerTwoScore = 4
print(min(playerOneScore, playerTwoScore))
print(min(0, 12, -19, 252))
print(min('Layla', 'Levi', 'Luke', 'Logan'))  # a comes before e, u, o
print(min("Angelo", 'Bart', "Crystal"))  # A comes before B, C
print(max(playerOneScore, playerTwoScore))
playerThreeScore = 20
print(max(playerOneScore, playerTwoScore, playerThreeScore))
print(max('Layla', 'Levi', 'Logan', 'Luke'))  # Lu is closest to the end of the alphabet
print()

# Python Rounding, Absolute Value, and Exponents

# round() rounds to the closest int
# 1.5 rounds up to 2; 1.499 rounds down to 1
myGpa = 3.6
amountOfSalt = 1.4999
APPL = -1.2
print(round(myGpa))
print(round(amountOfSalt))
print(round(APPL))
print()

# abs() absolute value
distanceAway = -13
print(abs(distanceAway))
lenOfRootInGround = -2.50
print(abs(lenOfRootInGround))
print()

# pow(x, y) base, exponent
# 3^2 -> 3 is base, 2 is exponent -> 3 * 3 = 9
changesOfTails = .5
inARowTails = 3  # number of coin flips
print(pow(changesOfTails, inARowTails))  # .5 ^ 3 = .125
chanceOfOne = .167  # 1/6 odds on a fair dice
inARowOne = 2  # number of rolls
print(pow(chanceOfOne, inARowOne))
print()

# Least to Greatest
pointsInAGame = [0, -10, -15, -2, 1, 12]
sortedGame = sorted(pointsInAGame)
print(sortedGame)

# Reverse
print(sorted(pointsInAGame, reverse=True))
print()

# Alphabetically
children = ['Bob', 'Steve', 'Linda']
print(sorted(children))
print(sorted(children, reverse=True))
print(sorted(['Bob', 'Steve', 'linda']))  # case matters when sorting unless stated otherwise

# Key Parameters
print(sorted("My favorite hero is goku".split(), key=str.upper))
print()
leaderBoard = {231: "CKL", 123: "ABC", 432: "JKC"}
print(sorted(leaderBoard))
print(sorted(leaderBoard.values()))
print(sorted(leaderBoard, reverse=True))
print(sorted(leaderBoard.values(), reverse=True))
print()
# name, grade, age
students = [('alice', 'B', 12), ('eliza', 'A', 16), ('tae', 'C', 15)]
print(sorted(students, key=lambda student: student[0]))  # sorting based on Name (A-Z)
print(sorted(students, key=lambda student: student[1]))  # sorting based on Grade (A-Z)
print(sorted(students, key=lambda student: student[2]))  # sorting based on Age (Youngest-Oldest)
print()

# type() function
r = range(0, 30)
print(type(r))

# isinstance(x,y)
"""Input: one object and one class info

   Output: Boolean whether or not the object is an instance
   of the class given by class info
   
   object is an instance of the class -> True
   object is not an instance of the class -> False
"""


class Car:
    pass


class Truck(Car):
    pass


c = Car()
c2 = Car()
t = Truck()

print(type(c))
print(type(t))
print(type(c) == type(t))
print(type(c) == type(c2))
print(isinstance(c, Car))  # is c and instance for Car? -> True
print(isinstance(t, Car))  # is t and instance for Car? -> True because isInstance take into consideration inheritance
print(isinstance(c,
                 Truck))  # is c and instance for Truck? -> False, because c is instigated from the base class Car
# which does not inherit from Truck

if isinstance(r, range):  # if r is in instance of range
    print(list(r))  # print out the value at r in the range

# better to use isinstance over type function in case of inheritance

