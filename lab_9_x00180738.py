# Task 1

from abc import ABC, abstractmethod

class Assessment(ABC):

    @abstractmethod
    def __init__(self, student_name_in, student_id_in, result_in):
        self.student_name = student_name_in
        self.student_id = student_id_in
        self.result = result_in

    @abstractmethod
    def print_details(self):
        pass


class CA(Assessment):

    def __init__(self, student_name_in, student_id_in, result_in, elapsedDays_in):
        super().__init__(student_name_in, student_id_in, result_in)
        self.elapsedDays = elapsedDays_in

    def print_details(self):
        print('student_name: {}'.format(self.student_name))
        print('student_id: {}'.format(self.student_id))
        print('Result: {}'.format(self.result))
        print('Elapsed Days: {}'.format(self.elapsedDays))


class Examination(Assessment):

    def __init__(self, student_name_in, student_id_in, result_in, date_in, time_in):
        super().__init__(student_name_in, student_id_in, result_in)
        self.date = date_in
        self.time = time_in

    def print_details(self):
        print('student_name: {}'.format(self.student_name))
        print('student_id: {}'.format(self.student_id))
        print('Result: {}'.format(self.result))
        print('Date: {}'.format(self.date))
        print('Time: {}'.format(self.time))


ca1 = CA(student_name_in='Flavio', student_id_in='x00180738', result_in=85, elapsedDays_in=14)
ca2 = CA(student_name_in='Flavio', student_id_in='x00180738', result_in=95, elapsedDays_in=0)
examination = Examination(student_name_in='Flavio', student_id_in='x001807387', result_in=75, date_in='15/12/2021', time_in='19:00')

list_of_evaluations = []
list_of_evaluations.append(ca1)
list_of_evaluations.append(ca2)
list_of_evaluations.append(examination)
total = 0

for evaluation in list_of_evaluations:
    print('*'*50)
    evaluation.print_details()
    if isinstance(evaluation, Examination):
        evaluation: Examination
        total += 0.5 * evaluation.result
    elif isinstance(evaluation, CA):
        total += 0.25 * evaluation.result

print('*' * 50)
print('Overall result: {}'.format(total))

# Task 2

list = []
student_name_in = input('Please insert student name: ')
student_id_in = input('Please insert student id: ')
for i in range(0, 3):
    caType = input('Please select the type of assessment (CA/Examination): ')
    if caType == 'CA':
        result_in = int(input('Please insert result: '))
        elapsedDays_in = input('Please insert elapsed days (0 for in class): ')
        newCA = CA(student_name_in=student_name_in, student_id_in=student_id_in, result_in=result_in, elapsedDays_in=elapsedDays_in)
        list.append(newCA)
    elif caType == 'Examination':
        result_in = int(input('Please insert result: '))
        date_in = input('Please insert date of examination: ')
        time_in = input('Please insert time of the examination: ')
        newExamination = Examination(student_name_in=student_name_in, student_id_in=student_id_in, result_in=result_in, date_in=date_in, time_in=time_in)
        list.append(newExamination)

total = 0
for evaluation in list:
    print('*'*50)
    evaluation.print_details()
    if isinstance(evaluation, Examination):
        evaluation: Examination
        total += 0.5 * evaluation.result
    elif isinstance(evaluation, CA):
        total += 0.25 * evaluation.result

print('*' * 50)
print('Overall result: {}'.format(total))
