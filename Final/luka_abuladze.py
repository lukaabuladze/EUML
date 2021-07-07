import numpy as np
import mysql.connector
import random
import string
from random import randint
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rimtariro",
    database="personal"
)

mycursor = mydb.cursor()
sql = "INSERT INTO employees (personal_id, name, surname, age) VALUES (%s, %s, %s, %s)"
sql2 = "INSERT INTO times (work_times) VALUES (%s)"


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


employees = []

ages_lis = []
rand_times = []
spent_time_in_days = []
ids = []
i = 0

chars = "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ"
names_lis = []
surnames_lis = []

while i < 100:
    rand_id = random_with_N_digits(9)
    if rand_id not in employees:
        employees.append(rand_id)
        ids.append(rand_id)
        rand_name = ''.join(random.choices(chars, k=5))
        employees.append(rand_name)
        names_lis.append(rand_name)
        rand_surname = ''.join(random.choices(chars, k=10))
        employees.append(rand_surname)
        surnames_lis.append(rand_surname)
        rand_age = random.randrange(20, 60)
        ages_lis.append(rand_age)
        employees.append(rand_age)
        for x in range(30):
            rand_t = round(random.uniform(0, 12), 1)
            rand_times.append(rand_t)
        i += 1

# print(ids)


print(employees)
# print(rand_times)

n = 4
m = 30

# using list comprehension
final = [employees[i * n:(i + 1) * n] for i in range((len(employees) + n - 1) // n)]
final_t = [rand_times[i * m:(i + 1) * m] for i in range((len(rand_times) + m - 1) // m)]

res = [tuple(i) for i in final]
res2 = [tuple(i) for i in final_t]

# print(res2)

# print(res)


val = res
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

mycursor.execute("SELECT * FROM employees")
myresult = mycursor.fetchall()
for item in myresult:
    print(item)

# val2 = res2
# mycursor.executemany(sql2, val2)
# mydb.commit()
# print(mycursor.rowcount, "was inserted.")


average_age = np.mean(ages_lis)
print(average_age)

empoyees_older_than_average = []
for i in final:
    if i[3] > average_age:
        empoyees_older_than_average.append(i)

print(empoyees_older_than_average)

df = pd.DataFrame({'Data': empoyees_older_than_average})
writer = pd.ExcelWriter('personal.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()



