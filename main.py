from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime



current_time = datetime.now()
print(current_time)

if __name__ == '__main__':
    calculate_salary()
    get_employees()
