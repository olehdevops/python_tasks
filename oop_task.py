# ITA Softserve, DevOps - Oleh Smahliuk


class Department(object):
    id_employee = 0
    list_of_manager = {}  # list of managers with their teams
    info_employee = {}  # general information about employees

    def __init__(self):
        Department.id_employee += 1


class Employee(Department):

    def __init__(self, first_name=None, second_name=None, salary=None, experience=None):
        super().__init__()

        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.experience = experience
        self.base_salary = 0

    def give_salary_base(self):

        """add bonus for experience"""

        self.base_salary = self.salary
        if self.experience > 5:
            self.base_salary = (self.base_salary * 1.2) + 500
        elif self.experience > 2:
            self.base_salary = self.base_salary + 200
        return self.base_salary


class Developer(Employee):

    def __init__(self, first_name=None, second_name=None, salary=None, experience=None, manager=None):
        self.manager = manager
        super().__init__(first_name, second_name, salary, experience)

        # add to list general information about developers and designers

        if self.manager in self.list_of_manager.keys():
            Employee.info_employee[Employee.id_employee] = [self.first_name, self.second_name,
                                                            self.manager, self.experience, self.salary]

            Employee.list_of_manager[self.manager].append("%s %s" % (self.first_name, self.second_name))

        else:
            print("{0} not yet on the list of managers."
                  " Add {0} to the list of managers first.".format(self.manager))

    def give_salary(self):

        """add bonus to salary"""

        print("{0} {1}: got salary: {2}$".format(self.first_name, self.second_name, super().give_salary_base()))

    def __repr__(self):
        return "{0} {1}, manager: {2}, experiance: {3}".format(self.first_name, self.second_name,
                                                               self.manager, self.experience)


class Designer(Employee):

    def __init__(self, first_name=None, second_name=None, salary=None, experience=None,
                 manager=None, coef_eff=None):
        super().__init__(first_name, second_name, salary, experience)
        self.manager = manager
        self.coef_eff = coef_eff

        # add to list general information about developers and designers

        if self.manager in self.list_of_manager.keys():
            Employee.info_employee[Employee.id_employee] = [self.first_name, self.second_name, self.manager,
                                                            self.coef_eff, self.experience, self.salary]
            Employee.list_of_manager[self.manager].append("%s %s" % (self.first_name, self.second_name))

        else:
            print("{0} not yet on the list of managers."
                  " Add {0} to the list of managers first.".format(self.manager))

    def give_salary(self):

        """add bonus to salary"""

        print("{0} {1}: got salary: {2}$".format(self.first_name, self.second_name,
                                                 super().give_salary_base() * self.coef_eff))

    def __repr__(self):
        return "{0} {1}, manager: {2}, experiance: {3}".format(self.first_name, self.second_name,
                                                               self.manager, self.experience)


class Manager(Employee):

    def __init__(self, first_name=None, second_name=None, salary=None, experience=None):
        super().__init__(first_name, second_name, salary, experience)

        # add to list general information about developers and designers

        if "{0} {1}".format(self.first_name, self.second_name) not in self.list_of_manager.keys():
            Employee.list_of_manager["{0} {1}".format(self.first_name, self.second_name)] = []
            Employee.info_employee[self.id_employee] = [self.first_name, self.second_name,
                                                        self.experience, self.salary]

        else:
            print("%s %s is already on the list. To view the entire list "
                  "use method view_list_of_managers" % (self.first_name, self.second_name))

    def give_salary(self):

        """add bonus to salary"""

        self.salary = super().give_salary_base()
        if len(self.list_of_manager["{0} {1}".format(self.first_name, self.second_name)]) > 10:
            self.salary = self.salary + 300
        elif len(self.list_of_manager["{0} {1}".format(self.first_name, self.second_name)]) > 5:
            self.salary = self.salary + 200

        print("{0} {1}: got salary: {2}$".format(self.first_name, self.second_name, self.salary))

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
        return "{0} {1}, experiance: {2}".format(self.first_name, self.second_name, self.experience)


person1 = Manager(first_name="Ivan", second_name="Reva", salary=1000, experience=7)
person2 = Developer(first_name="Vasia", second_name="Pupkin", salary=2000, experience=7, manager="Ivan Reva")
person3 = Designer(first_name="Bob", second_name="Pupkin", salary=2000, experience=7, coef_eff=1, manager="Ivan Reva")
person4 = Designer(first_name="Bob", second_name="Pupkin", salary=2000, experience=7, coef_eff=1, manager="Ivan Reva")
person5 = Designer(first_name="Bob", second_name="Pupkin", salary=2000, experience=7, coef_eff=1, manager="Ivan Reva")
person6 = Designer(first_name="Bob", second_name="Pupkin", salary=2000, experience=7, coef_eff=1, manager="Ivan Reva")
person7 = Designer(first_name="Bob", second_name="Pupkin", salary=2000, experience=7, coef_eff=1, manager="Ivan Reva")
person8 = Designer(first_name="Bob", second_name="Pupkin", salary=2000, experience=7, coef_eff=1, manager="Ivan Reva")
person9 = Designer(first_name="Bob", second_name="Pupkin", salary=2000, experience=7, coef_eff=1, manager="Ivan Reva")
person10 = Designer(first_name="Bob", second_name="Pupkin", salary=2000, experience=7, coef_eff=1, manager="Ivan Reva")
person11 = Designer(first_name="Bob", second_name="Pupkin", salary=2000, experience=7, coef_eff=1, manager="Ivan Reva")
person12 = Designer(first_name="Bob", second_name="Pupkin", salary=2000, experience=7, coef_eff=1, manager="Ivan Reva")
person15 = Manager(first_name="Jo", second_name="Rush", salary=1000, experience=7)
person13 = Designer(first_name="Bob", second_name="Pupkin", salary=2000, experience=7, coef_eff=1, manager="Jo Rush")
person14 = Designer(first_name="Bob", second_name="Pupkin", salary=2000, experience=7, coef_eff=1, manager="Jo Rush")


# person1.give_salary()
# person5.give_salary()
# person1.view_list_of_managers()
# print(person15)
