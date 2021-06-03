import random
import string
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector
from random import randint


def randomnu(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="rimtariro",
  database="studentquiz"
)

mycursor = mydb.cursor()
sql = "INSERT INTO students (personal_id, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

#დავალება N1,N2
random_ids = []
rand_times = []
in_week = []
ids = []
i = 0
while i < 100:
    rand_id = randomnu(9)
    if rand_id not in random_ids:
        random_ids.append(rand_id)
        ids.append(rand_id)
        for x in range(7):
            rand_t = round(random.uniform(0, 5), 2)
            random_ids.append(rand_t)
            rand_times.append(round(rand_t))
        i += 1

n = 8
m = 7

final = [random_ids[i * n:(i + 1) * n] for i in range((len(random_ids) + n - 1) // n)]
final_t = [rand_times[i * m:(i + 1) * m] for i in range((len(rand_times) + m - 1) // m)]
res = [tuple(i) for i in final]
print(final_t)
print(ids)

#დავალება N3
in_week=[sum(rand_times[x:x+7]) for x in range(0, len(rand_times), 7)]
print(in_week)
plt.scatter(ids, in_week)
plt.show()

#დავალება N4
spent_time = np.mean(in_week)
print("სტუდენტის მიერ კვირაში დახარჯული არის " + str(spent_time) + "-საათი")
standard_deviation = round(np.std(in_week),2)
print("სტანდარტული გადახრა უდრის " + str(standard_deviation))


# val = res
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "was inserted.")
#
#
# mycursor.execute("SELECT * FROM students")
# myresult = mycursor.fetchall()
# for item in myresult:
#   print(item)
