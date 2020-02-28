import sys
import random
import string

targetString = "methinks it is like a weasel"
childrenSize = 100
defaultProbability = 5

# Select a random character from a
# set of lowercase letters and whitespace


def generateRandomCharacter():
    return random.choice(string.ascii_lowercase + string.whitespace)

# Generate a random string, the size of the target string


def generateRandomString():
    randomString = ''
    for i in range(0, len(targetString)):
        randomString += generateRandomCharacter()
    return randomString

# Compare how close a given string is to
# the target string by finding the number of
# common letters between the two


def compareWithTarget(candidateString):
    commonLetters = 0
    for i in range(0, len(targetString)):
        if targetString[i] == candidateString[i]:
            commonLetters += 1

    return commonLetters

# Create children based off the parent random string


def generateChildString(randomString, probability):
    childString = randomString
    for i in range(0, len(targetString)):
        randomInter = random.randint(1, 100)
        if randomInter <= probability:
            childString = childString[:i] + \
                generateRandomCharacter() + childString[i + 1:]

    return childString

# Main program


def weasel(probability):
    count = 0
    found = False
    resultList = []
    randomString = generateRandomString()
    startingString = randomString
    while not found:
        # List to keep track of generated children
        stringList = [''] * childrenSize

        # List to keep track of the closeness score of each child
        scoreList = [0] * childrenSize

        # Generate children and closeness score
        for i in range(0, childrenSize):
            stringList[i] = generateChildString(startingString, probability)
            scoreList[i] = compareWithTarget(stringList[i])

        # Track the closest child for this generation
        closestStringIndex = max(scoreList)

        # Mutation found, print to screen and exit loop
        if closestStringIndex == len(targetString):
            found = True
            print('*******************************************')
            print(randomString)
            print('*******************************************')

            print('Generations: ', count)
            print('Probability: ', probability)

        # Use the closest child from previous generation as starting point
        # for new generation
        startingString = stringList[scoreList.index(closestStringIndex)]

        # Generation counter
        count += 1


# Get user probability input or use default if none given
userProbability = input(
    'Specify the probability of making a mistake: \t') or defaultProbability

# Run program
print(weasel(int(userProbability)))
