from salary_manager import create_salary, read_all, read_by_salary
from salary_manager import salaries, update, delete_by_salary

def menu():
    message = '''
1 - Create salary
2 - Read all salaries
3 - Read by salary
4 - Update
5 - Delete
6 - Exit / Logout
'''
    choice = int(input(message))
    if choice == 1:
        salary = int(input('Salary:'))
        create_salary(salary)
    elif choice == 2:
        result_salaries = read_all()
        print('Salaries:')
        for salary in result_salaries:
            print(salary)
    elif choice == 3:
        salary = int(input('Search Salary:'))
        index = read_by_salary(salary)
        if salary == -1:
            print('Salary not found')
        else:
            print(f'Salary is at index {index}')
    elif choice == 4:
        old_salary = int(input('Salary to update:'))
        new_salary = int(input('New Salary'))
        update(old_salary, new_salary)
    elif choice == 5:
        salary = int(input('Salary to delete:'))
        delete_by_salary(salary)     
    return choice

def menus():
    print('Salary Management App')
    choice = menu()
    while choice != 6:
        choice = menu()
    print('Thank you for using app')

create_salary(1000)
create_salary(5000)
create_salary(8000)
create_salary(3000)

result_salaries = read_all()
for salary in result_salaries:
    print(salary)

print(read_by_salary(8000))
print(read_by_salary(4000))
print(salaries[read_by_salary(8000)])

update(8000, 8500)
print(read_all())

delete_by_salary(1000)
print(read_all())