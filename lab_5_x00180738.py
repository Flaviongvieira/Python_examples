# Lab 5

# Task 1
class studentLab:
    studentId = ""
    name = ""
    subject = ""
    ca1Result = 0
    ca2Result = 0

    def print_details(self):
        print("*****************************************")
        print("********** Student Details **************")
        print("Student ID: \t\t", self.studentId)
        print("Student Name: \t\t", self.name)
        print("Subject: \t\t", self.subject)
        print("CA 1 Result: \t\t", self.ca1Result)
        print("CA 2 Result: \t\t", self.ca2Result)
        print("*****************************************")


std1 = studentLab()
std1.name = "Flavio"
std1.studentId = "x00180738"
std1.subject = "OOS"
std1.ca1Result = 100
std1.ca2Result = 100
std1.print_details()

# Task 2
class printCard:
    accountNumber = ""
    password = ""
    numberOfCredits = 0

    def print_details(self):
        print("*****************************************")
        print("************* Card Details **************")
        print("Account Number: \t\t", self.accountNumber)
        print("Number of Credits: \t\t", self.numberOfCredits)
        print("*****************************************")

cardA = printCard()
# cardA.accountNumber = input("Please enter account number: ")
cardA.accountNumber = "x00180738"
# cardA.numberOfCredits = input("Please enter number of credits: ")
cardA.numberOfCredits = 60
# cardA.password = input("Please enter password: ")
cardA.password = "abcd1234"
cardA.print_details()

# Task 3
def calculateAverage(resultOne, resultTwo):
    total = resultOne + resultTwo
    avarageResult = total/2
    return avarageResult

student_average = calculateAverage(std1.ca1Result, std1.ca2Result)
if student_average >= 70:
    cardA.numberOfCredits += 400

cardA.print_details()