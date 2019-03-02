# ITA Softserve, DevOps - Oleh Smahliuk

class Employee(object):

    id_employee = 0
    list_of_manager = {}  # list of managers with their teams
    info_employee = {}  # general information about employees

    def __init__(self, first_name=None, second_name=None, position=None, salary=None,
                 experience=None, coef_eff=None, manager=None):

        self.first_name = first_name
        self.second_name = second_name
        self.position = position
        self.salary = salary
        self.experience = experience
        self.coef_eff = coef_eff
        self.manager = manager

        Employee.id_employee += 1

        if self.manager is not None:  # add to list general information about developers and designers

            if self.manager in self.list_of_manager.keys():
                Employee.info_employee[self.id_employee] = [self.first_name, self.second_name,
                                                            self.manager, self.coef_eff,
                                                            self.experience, self.salary]
                Employee.list_of_manager[self.manager].append("%s %s" % (self.first_name,
                                                                         self.second_name))

            else:
                print("{0} not yet on the list of managers."
                      " Add {0} to the list of managers first.".format(self.manager))

        if self.manager is None:  # add to list general information about managers

            if "{0} {1}".format(self.first_name, self.second_name) not in self.list_of_manager.keys():
                Employee.list_of_manager["{0} {1}".format(self.first_name, self.second_name)] = []
                Employee.info_employee[self.id_employee] = [self.first_name, self.second_name,
                                                            self.experience, self.salary]

            else:
                print("%s %s is already on the list. To view the entire list "
                      "use method view_list_of_managers" % (self.first_name, self.second_name))

    def give_salary(self, arg):

        """add bonus to salary"""

        count = 0
        for id_person, info in self.info_employee.items():
            if "{0} {1}".format(info[0], info[1]) == arg:

                base_salary = info[-1]  # add bonus for experience
                if info[-2] > 2:
                    base_salary = info[-1] + 200
                if info[-2] > 5:
                    base_salary = (info[-1] * 1.2) + 500

                if info[-3] is not None and len(info) > 4:  # add bonus for effectiveness
                    base_salary *= info[-3]

                if arg in self.list_of_manager.keys():  # add bonus for team management
                    if len(self.list_of_manager[arg]) > 5:
                        base_salary += 200
                    elif len(self.list_of_manager[arg]) > 10:
                        base_salary += 300
                print("{0}: got salary: {1}$".format(arg, int(base_salary)))
                count += 1
        if count == 0:
                print("{0} is not in the department".format(arg))

    def view_list_of_managers(self):

        """shows a list of managers with their teams"""

        for key, values in self.list_of_manager.items():
            if len(values) == 0:
                print("{0} doesn`t have a team yet".format(key))
            else:
                print("{0}:".format(key))
                for value in values:
                    print("\t {0}".format(value))

    def __repr__(self):
        if self.manager is None:
            return "{0} {1}, experiance: {2}".format(self.first_name, self.second_name, self.experience)
        else:
            return "{0} {1}, manager: {2}, experiance: {3}".format(self.first_name, self.second_name,
                                                                   self.manager, self.experience)


person1 = Employee(first_name="Ivan", second_name="Reva",
                   position="manager", salary=1000, experience=3)
person2 = Employee(first_name="Vasia", second_name="Pupkin",
                   position="Dev", salary=2000, experience=7, manager="Ivan Reva")
person3 = Employee(first_name="Stepan", second_name="Rak",
                   position="Dev", salary=2000, experience=2, manager="Ivan Reva")
# person4 = Employee(first_name="Jo", second_name="Rush", position="manager",
#                    salary=3000, experience=3)
# person5 = Employee(first_name="Bob", second_name="Pupkin", position="Dis",
#                    salary=2000, experience=7, coef_eff=0.5, manager="Jo Rush")
# person6 = Employee(first_name="Den", second_name="Broun", position="manager",
#                    salary=3000, experience=3)
# person7 = Employee(first_name="Din", second_name="Broun", position="manager",
#                    salary=1000, experience=7)
# person8 = Employee(first_name="Vasia", second_name="Pupkin", position="Dev",
#                    salary=2000, experience=2, manager="Den Broun")
# person9 = Employee(first_name="Vasia", second_name="Pupkin", position="Dev",
#                    salary=2000, experience=3, manager="Den Broun")
# person10 = Employee(first_name="Vasia", second_name="Pupkin", position="Dev",
#                     salary=2000, experience=2, manager="Den Broun")
# person11 = Employee(first_name="Vasia", second_name="Pupkin", position="Dev",
#                     salary=2000, experience=7, manager="Ivan Reva")
# person12 = Employee(first_name="Vasia", second_name="Pupkin", position="Dev",
#                     salary=2000, experience=7, manager="Ivan Reva")
# person13 = Employee(first_name="Vasia", second_name="Pupkin", position="Dev",
#                     salary=2000, experience=7, manager="Din Broun")
# person14 = Employee(first_name="Vasia", second_name="Pupkin", position="Dev",
#                     salary=2000, experience=7, manager="Din Broun")
# person15 = Employee(first_name="Vasia", second_name="Pupkin", position="Dev",
#                     salary=2000, experience=7, manager="Jo Rush")
# person16 = Employee(first_name="Vasia", second_name="Pupkin", position="Dev",
#                     salary=2000, experience=7, manager="Ivan Reva")
# person17 = Employee(first_name="Vasia", second_name="Pupkin", position="Dev",
#                     salary=2000, experience=7, manager="Ivan Reva")
# person18 = Employee(first_name="Alan", second_name="Turing", position="manager",
#                     salary=3000, experience=3)
# person19 = Employee(first_name="Vasia", second_name="Pupkin", position="Dev",
#                     salary=2000, experience=7, manager="Alan Turing")

print(person3)
person3.give_salary("Stepan Rak")
person3.view_list_of_managers()
