import random as r

print("Welcome. This bot provides numbers for the following lottery draws, with their abbreviation in"
      " brackets: Lotto (L), EuroMillions(EM), Thunderball(TB),"
      "and EuroMillions HotPicks(HP)")

lotteryChoice = input("Which lottery do you want to draw numbers for? Use the chosen draws abbreviation from the"
                      " options above:").upper()

lotteryNumbers = []
bonusBalls = []

# Functions of each game
def lotto():
    for i in range(0, 6):
        number = r.randint(1, 59)
        while number in lotteryNumbers:
            number = r.randint(1, 59)
        lotteryNumbers.append(number)


def euro():
    for i in range(0, 5):
        number = r.randint(1, 50)
        while number in lotteryNumbers:
            number = r.randint(1, 50)
        lotteryNumbers.append(number)

    for i in range(0, 2):
        number = r.randint(1, 12)
        while number in bonusBalls:
            number = r.randint(1, 12)
        bonusBalls.append(number)

def thunder():
    for i in range(0, 5):
        number = r.randint(1, 39)
        while number in lotteryNumbers:
            number = r.randint(1, 39)
        lotteryNumbers.append(number)

    for i in range(0, 1):
        number = r.randint(1, 14)
        while number in bonusBalls:
            number = r.randint(1, 14)
        bonusBalls.append(number)

def eurohp():
    for i in range(0, 5):
        number = r.randint(1, 50)
        while number in lotteryNumbers:
            number = r.randint(1, 50)
        lotteryNumbers.append(number)


# Calls certain function regarding user game selection
def reCall():
    if lotteryChoice == 'l'.upper():
        lotto()

    elif lotteryChoice == 'em'.upper():
        euro()

    elif lotteryChoice == 'tb'.upper():
        thunder()

    elif lotteryChoice == 'hp'.upper():
        eurohp()

    else:
        print("Sorry, that is not one of the abbreviations listed.")

# Function that returns a result
def draw_response():
    reCall()
    lotteryNumbers.sort()
    bonusBalls.sort()

    if len(bonusBalls) == 0:
        print(f"Todays lottery numbers are: {lotteryNumbers}. Best of luck!")

    else:
        print(f"Todays lottery numbers are: {lotteryNumbers} , bonus balls are {bonusBalls} . Best of luck!")


draw_response()




