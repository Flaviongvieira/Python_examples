## Lab 3
# task 1

import csv

# create pima 2D list
with open("pima.csv", "r") as file:
    pima_2D_list = list(csv.reader(file))

# create lists from the pima 2D list
blood_pressure_list = [float(row[2]) for row in pima_2D_list]

nonZeroValues = []
sumOfNonZeroValues = 0
numberOfNonZeroValues = 0
for x in blood_pressure_list:
    if x != 0:
        nonZeroValues.append(x)
        numberOfNonZeroValues += 1
        sumOfNonZeroValues += x
    else:
        pass
newBloodPressure = sumOfNonZeroValues / numberOfNonZeroValues
newBloodPressure = round(newBloodPressure, 2)

for x in blood_pressure_list:
    instanceLocation = blood_pressure_list.index(x)
    bloodPressLocation = 2
    if x == 0:
        pima_2D_list[instanceLocation][bloodPressLocation] = newBloodPressure
    else:
        pima_2D_list[instanceLocation][bloodPressLocation] = x

    with open("pimaNew.csv", "a", newline="") as file:
        dataEntry = pima_2D_list[instanceLocation]
        writer = csv.writer(file)
        writer.writerow(dataEntry)

# Task 2
import random
def print_random_numbers():
    numberRandom = random.randint(0, 100)
    print(numberRandom)


for i in range(10):
    print_random_numbers()


# task 3
def odd_number(limitNumber=None):
    max = int(input('please enter the limit: '))
    for i in range(0, max):
        if i % 2 != 0:
            print(i)
        else:
            pass


odd_number()


# task 4
def longer_string(firstString=None, secondString=None):
    firstString = input('please type first word or phrase: ')
    secondString = input('please type second word or phrase: ')
    srtingOneLength = len(firstString)
    stringTwoLength = len(secondString)
    if srtingOneLength > stringTwoLength:
        print('{0} is longer than {1}.'.format(firstString, secondString))
    elif srtingOneLength == stringTwoLength:
        print('{0} and {1} have the same length.'.format(firstString, secondString))
    else:
        print('{1} is longer than {0}.'.format(firstString, secondString))


longer_string()
