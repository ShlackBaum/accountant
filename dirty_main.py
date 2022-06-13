from application.db.people import *
from application.salary import *
from datetime import *

if __name__ == '__main__':
    print(f"Сегодняшняя дата - {datetime.now()}")
    get_employees()
    calculate_salary()

