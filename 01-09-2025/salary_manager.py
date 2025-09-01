salaries = []
#CRUD - Create, Read All, Read By ID, Update, Delete
#                         Read By Salary

def create_salary(salary):
    global salaries
    salaries.append(salary)
    
#create_salary(1000)
#print(salaries)

def read_all():
    return salaries

def read_by_salary(salary): #return first occurance index of salary #range(stop) | range(start, stop) | range(start, stop, step)
    for I in range(len(salaries)): #len(salaries)=5, I=0,1,2,3,4
        if salaries[I] == salary:
            return I
    return -1

def update(old_salary, new_salary):
    global salaries
    index = read_by_salary(old_salary)
    salaries[index] = new_salary

def delete_by_salary(salary):
    global salaries
    index = read_by_salary(salary) #index of 1000=0
    salaries.pop(index) #0

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