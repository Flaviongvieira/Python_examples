# Task 1
import random

class Animal:
    animal_id = 0
    animal_type = ''

    def __init__(self, animal_id_in=None, animal_type_in=None):
        self.animal_id = animal_id_in
        self.animal_type = animal_type_in


    def display_details(self):
        print('Animal:')
        print('\tId: {}'.format(self.animal_id))
        print('\tType: {}'.format(self.animal_type))


class Greyhound(Animal):
    gh_name = ''
    gh_sex = ''
    gh_father = ''
    gh_mother = ''
    gh_litters = 0
    gh_pups = 0

    def __init__(self, gh_name_in=None, gh_sex_in=None, gh_father_in=None, gh_mother_in=None):
        animal_id_in = random.randint(1000, 9999)
        animal_type_in = 'Greyhound'
        # gh_name_in = random.choice(['brown', 'piggy'])
        # gh_sex_in = random.choice(['female','male'])
        # gh_father_in = random.choice(['bigolboy', 'badassdog'])
        # gh_mother_in = random.choice(['luka', 'lily', 'flower'])
        Animal.__init__(self, animal_id_in, animal_type_in)
        self.gh_name = gh_name_in
        self.gh_sex = gh_sex_in
        self.gh_father = gh_father_in
        self.gh_mother = gh_mother_in
        self.gh_litters = 0
        self.gh_pups = 0

    def update_breeding_record(self, pups_in):
        self.gh_pups += pups_in
        self.gh_litters += 1

    def gh_display_details(self):
        self.display_details()
        print('Name: {}'.format(self.gh_name))
        print('Sex: {}'.format(self.gh_sex))
        print('Father: {}'.format(self.gh_father))
        print('Mother: {}'.format(self.gh_mother))
        print('Litters: {}'.format(self.gh_litters))
        print('Pups: {}'.format(self.gh_pups))


testGh = Greyhound('Mrs Flash', 'female', 'Tom Foley', 'The Late Late Show')
testGh.gh_display_details()
print('*'*40)
testGh.update_breeding_record(4)
testGh.update_breeding_record(5)
testGh.gh_display_details()


# Task 2

class Employee:
    name = ''
    number = 0
    wages = 0
    hours_worked = 0


    def __init__(self, name_in=None, number_in=None, wages_in=0, hours_worked_in=0):
        try:
            self.set_name(name_in)
            self.set_number(number_in)
            self.set_wages(wages_in)
            self.set_hours_worked(hours_worked_in)
        except Exception as e:
            raise Exception('Employee  was not created.')

    def set_name(self, name_in):
        if name_in is not None:
            self.name = name_in
        else:
            raise Exception('Name cannot be blank.')

    def set_number(self, number_in):
        if number_in < 0:
            self.number = 0
        else:
            self.number = number_in

    def set_wages(self, wages_in):
        if wages_in < 0:
            self.wages = 0
        else:
            self.wages = wages_in

    def set_hours_worked(self, hours_worked_in):
        if hours_worked_in < 0:
            self.hours_worked = 0
        else:
            self.hours_worked = hours_worked_in

    def calculate_salary(self):
        salary = (self.wages * self.hours_worked)
        return salary

    def print_emp_details(self):
        print('Name: {}'.format(self.name))
        print('Number: {}'.format(self.number))
        print('wages: {}'.format(self. wages))
        print('hours worked: {}'.format(self.hours_worked))



class Trainee(Employee):
    trainningHours = 0

    def __init__(self, name_in=None, number_in=None, wages_in=0, hours_worked_in=0, trainningHours_in=0):
        Employee.__init__(self, name_in, number_in, wages_in, hours_worked_in)
        self.set_training_hours(trainningHours_in)

    def set_training_hours(self, trainning_hours_in):
        if int(trainning_hours_in) < 0:
            self.trainningHours = 0
        else:
            self.trainningHours = trainning_hours_in

    def T_calculate_salary(self):
        week_sal = super().calculate_salary()
        tra_sal = self.trainningHours*5
        total_salary = tra_sal + week_sal
        return int(total_salary)

    def print_tr_details(self):
        super().print_emp_details()
        print('-'*35)
        print('Salary: {}'.format(self.T_calculate_salary()))
        print('Includes hours Training: {}'.format(self.trainningHours))


testTrain = Trainee('Karen', 1234, 20, 40, 2)
testTrain.print_tr_details()
