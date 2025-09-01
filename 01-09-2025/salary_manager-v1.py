salaries = []
salaries.append(1000)
salaries.append(5000)
salaries.append(7000)
print(salaries)

salaries.remove(7000)
print(salaries)

index = -1
I = 0
search = 5000
for salary in salaries:
    if salary == search:
        index = I
        break
    I += 1
print(index)