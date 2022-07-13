# Lab 4

# Taks 1:
def print_range(firstValue, secondValue):
    while firstValue <= secondValue:
        print(firstValue)
        firstValue += 1
print_range(3, 9)

# Task2:
def discount_calc(RRP, discPerc=0):
    if discPerc == 0:
        salePrice = RRP
    else:
        discPercDec = discPerc / 100
        salePrice = RRP*(1 - discPercDec)
        salePrice = round(salePrice, 2)
    print("Sale price is {} Eur".format(salePrice))


discount_calc(100, 50)
discount_calc(100)
discount_calc(10, 20)

# Task 3
def temperature_converter(temperature_user, tempScale=None):
    if tempScale == 'Celsius':
        celToFahr = (temperature_user*1.8) + 32
        return celToFahr
    elif tempScale == 'Fahrenheit':
        fahrToCel = (temperature_user - 32) * 0.5666
        return fahrToCel
    else:
        print('Please insert Celsius or Fahrenheit')

print(temperature_converter(50, 'Celsius'))
print(temperature_converter(102, 'Fahrenheit'))

# Task 4
def list_contains(oneDList=None, valueCheck=None):
    listToCheck = []
    listSize = int(input('please insert the length of the list: '))
    for i in range(listSize):
        listValue = int(input('please add list value: '))
        listToCheck.append(listValue)
    valueTocheck = int(input('please enter value to check: '))
    numberOfOcu = listToCheck.count(valueTocheck)
    if numberOfOcu > 1:
        # validation = True
        # return validation
        print('The value {} is in the list {}  times -> More than once'.format(valueTocheck, numberOfOcu))
    else:
        # validation = False
        # return validation
        print('The value {} is in the list {} time(s) -> Equal or less than once'.format(valueTocheck, numberOfOcu))

list_contains()
