"""
Employee Management System

This module defines classes for different types of employees with salary calculation methods.
"""

class Employee:
    """Base class representing an employee."""

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.identifier = kwargs.get('identifier', '')
        self.base_salary = 0

    def cal_salary(self):
        """Calculate the salary."""
        return self.base_salary

    def __str__(self):
        return f"{self.name} (ID: {self.identifier})"


class PermanentEmployee(Employee):
    """Class representing a permanent employee."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.benefits = kwargs.get('benefits', [])

    def cal_salary(self):
        """Calculate the salary for a permanent employee."""
        if "health_insurance" in self.benefits and "retirement" in self.benefits:
            return self.base_salary * 0.7
        elif "retirement" in self.benefits:
            return self.base_salary * 0.8
        elif "health_insurance" in self.benefits:
            return self.base_salary * 0.9
        else:
            return self.base_salary

    def __str__(self):
        return f"{super().__str__()} - Permanent Employee"


class Manager(Employee):
    """Class representing a manager."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bonus = kwargs.get('bonus', 0)

    def cal_salary(self):
        """Calculate the salary for a manager."""
        return self.base_salary + self.bonus

    def __str__(self):
        return f"{super().__str__()} - Manager"


class TemporaryEmployee(Employee):
    """Class representing a temporary employee."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hours = kwargs.get('hours', 0)

    def cal_salary(self):
        """Calculate the salary for a temporary employee."""
        return self.base_salary * self.hours

    def __str__(self):
        return f"{super().__str__()} - Temporary Employee"


class Consultant(TemporaryEmployee):
    """Class representing a consultant."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.trips = kwargs.get('trips', 0)

    def cal_salary(self):
        """Calculate the salary for a consultant."""
        return (self.base_salary * self.hours) + (self.trips * 1000)

    def __str__(self):
        return f"{super().__str__()} - Consultant"


class ConsultantManager(Consultant, Manager):
    """Class representing a consultant manager."""

    def __init__(self, **kwargs):
        Consultant.__init__(self, **kwargs)
        Manager.__init__(self, **kwargs)

    def cal_salary(self):
        """Calculate the salary for a consultant manager."""
        return (self.base_salary * self.hours) + (self.trips * 1000) + self.bonus

    def __str__(self):
        return f"{super().__str__()} - Consultant Manager"


############################################################
############################################################
############################################################

def main():
    ''' ##### DRIVER CODE #####
        ##### Do not change. '''

    # create employees
    chris = Employee(name="Chris", identifier="UT1")
    emma = PermanentEmployee(name="Emma", identifier="UT2", salary=100000, benefits=["health_insurance"])
    sam = TemporaryEmployee(name="Sam", identifier="UT3", salary=100,  hours=40)
    john = Consultant(name="John", identifier="UT4", salary=100, hours=40, travel=10)
    charlotte = Manager(name="Charlotte", identifier="UT5", salary=1000000, bonus=100000)
    matt = ConsultantManager(name="Matt", identifier="UT6", salary=1000, hours=40, travel=4, bonus=10000)

    # print employees
    print(chris, "\n")
    print(emma, "\n")
    print(sam, "\n")
    print(john, "\n")
    print(charlotte, "\n")
    print(matt, "\n")

    # calculate and print salaries
    print("Check Salaries")
    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["health_insurance"]
    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["retirement", "health_insurance"]
    print("Emma's Salary is:", emma.cal_salary())
    print("Sam's Salary is:", sam.cal_salary())
    print("John's Salary is:", john.cal_salary())
    print("Charlotte's Salary is:", charlotte.cal_salary())
    print("Matt's Salary is:",  matt.cal_salary())

if __name__ == "__main__":
    main()
