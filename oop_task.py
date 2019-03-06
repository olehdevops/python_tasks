# ITA Softserve, DevOps - Oleh Smahliuk


class Department(object,):
    list_of_managers = []

    def add_manager(self, emp):
        self.list_of_managers.append(emp)

    def get_salary(self):
        for manager in self.list_of_managers:
            print(manager.give_salary())
            for emp in manager.team:
                print("\t", emp.give_salary())

    def show_dep(self):
        for manager in self.list_of_managers:
            print(manager)
            for emp in manager.team:
                print("\t", emp)


class Employee(object):

    def __init__(self, first_name, second_name, salary, experience):

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


class Manager(Employee):

    team = []

    def __init__(self, first_name, second_name, salary, experience):
        super(Manager, self).__init__(first_name, second_name, salary, experience)

    def add_team(self, emp):
        self.team.append(emp)

    def give_salary(self):

        """add bonus to salary"""

        self.salary = super().give_salary_base()
        if len(self.team) > 10:
            self.salary = self.salary + 300
        elif len(self.team) > 5:
            self.salary = self.salary + 200

        count = 0
        for i in self.team:
            if isinstance(i, Developer):
                count += 1
        if count > len(self.team)/2:
            self.salary = self.salary * 1.1

        return "{0} {1}: got salary: {2}$".format(self.first_name, self.second_name, self.salary)

    def __repr__(self):
        return "{0} {1}, experiance: {2}".format(self.first_name, self.second_name, self.experience)


class Developer(Employee):

    def __init__(self, first_name, second_name, salary, experience, manager=None):
        super(Developer, self).__init__(first_name, second_name, salary, experience)
        self.manager = manager

    def give_salary(self):
        return "{0} {1} got salary: {2}$".format(self.first_name, self.second_name, self.give_salary_base())

    def __repr__(self):
        return "{0} {1}, manager: {2} {3}, experiance: {4}".format(self.first_name, self.second_name,
                                                                   self.manager.first_name,
                                                                   self.manager.second_name,
                                                                   self.experience)


class Designer(Employee):

    def __init__(self, first_name, second_name, salary, experience, coef_eff, manager=None):
        super(Designer, self).__init__(first_name, second_name, salary, experience)
        self.manager = manager
        self.coef_eff = coef_eff

    def give_salary(self):
        self.salary = self.give_salary_base() * self.coef_eff
        return "{0} {1} got salary: {2}$".format(self.first_name, self.second_name, self.salary)

    def __repr__(self):
        return "{0} {1}, manager: {2} {3}, experiance: {4}".format(self.first_name, self.second_name,
                                                                   self.manager.first_name,
                                                                   self.manager.second_name,
                                                                   self.experience)


dep = Department()
Petia = Manager("Petia", "Bor", 10, 5)
dep.add_manager(Petia)
vasya = Developer("Vasia", "Neck", 10, 3, manager=Petia)
kolia = Designer("Kolia", "Rush", 10, 7, 1, manager=Petia)
Petia.add_team(vasya)
Petia.add_team(kolia)

dep.get_salary()

dep.show_dep()
