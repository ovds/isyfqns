import numpy as np

employees = []

with open("input_question_1.txt", 'r') as f:
    for line in f.readlines():
        employees.append(list(map(int, line.strip().split())))

employees = np.array(employees)

min_age = np.min(employees[:, 1])
max_age = np.max(employees[:, 1])

mean_salary = np.mean(employees[:, 2])
std = np.std(employees[:, 2])

# sort by age
ageSort = employees[employees[:, 1].argsort()]

#sort by salary
salarySort = employees[employees[:, 2].argsort()]

#sort by years of service
serviceSort = employees[employees[:, 3].argsort()]

f = open("output_question_1.txt", "a")
f.seek(0)
f.truncate()
f.write(str(min_age) + " " + str(max_age) + "\n\n")
f.write(str(mean_salary) + " " + str(std) + "\n\n")
f.write(str(ageSort).replace(r'[', '').replace(r']', '').split() + "\n\n")
f.write(str(salarySort).replace(r'[', '').replace(r']', '') + "\n\n")
f.write(str(serviceSort).replace(r'[', '').replace(r']', '') + "\n\n")
f.close()
