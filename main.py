from datetime import datetime, date, time
from application.salary import calculate_salary
from application.db.people import get_employees

def main():
    print(datetime.today())



if __name__ == '__main__':
    main()
    calculate_salary()
    get_employees()
