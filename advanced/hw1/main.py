
import sys
import time

sys.path.append('./application')
sys.path.append('./application/db')

from datetime import datetime
from salary import calculate_salary
from people import get_employees


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













