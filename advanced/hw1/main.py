
import sys
import time

from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


# print(datetime.now())

def time_decorator(func) :
    def wrapped() :
        print(datetime.now())
        func()
    return wrapped



calculate_salary = time_decorator(calculate_salary)
get_employees = time_decorator(get_employees)

if __name__ == '__main__' :
    calculate_salary()
    get_employees()













