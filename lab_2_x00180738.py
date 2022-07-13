# q1
import csv
for i in range(5):
    name = input("please enter your name: ")

    with open("lab2.csv", "a", newline="") as file:
        singleEntry = [name]
        writer = csv.writer(file)
        writer.writerow(singleEntry)

# q2
# create list of names
import csv
with open("lab2.csv", "r") as file:
    list_of_names = file.read().split("\n")
print(list_of_names)

# request name to user
name = input("please enter a name to search: ")
if name in list_of_names:
    print('Name is on the list.')
else:
    print('Name is not on the list.')

# q3
import csv
from statistics import mean

# create pima 2D list
with open("pima.csv", "r") as file:
    pima_2D_list = list(csv.reader(file))
print(pima_2D_list)

# create lists from the pima 2D list
blood_pressure_list = [float(row[2]) for row in pima_2D_list]
# print(blood_pressure_list)
age_list = [int(row[-2]) for row in pima_2D_list]
# print(age_list)

# calculating blood pressure stats
print("the max blood pressure is {0}".format(max(blood_pressure_list)))
print("the min blood pressure is {0}".format(min(blood_pressure_list)))
print("the average blood pressure is {0}".format(mean(blood_pressure_list)))

# calculating age stats
print("the max age is {0}".format(max(age_list)))
print("the min age is {0}".format(min(age_list)))
print("the average age is {0}".format(mean(age_list)))