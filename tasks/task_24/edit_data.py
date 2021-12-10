from datetime import datetime
from random import randint, choice

f_name = None

with open(r"data\fmale_name.txt", "r", encoding="utf-8") as out_file:

    data = out_file.readlines()[::2]
    data = list(map(lambda x: x.split(), data))
    for i in range(len(data)):
        data[i] = data[i][0]

    f_name = data

with open(r"data\male_name.txt", "r", encoding="utf-8") as out_file:

    data = out_file.readlines()[::2]
    data = list(map(lambda x: x.split(), data))
    for i in range(len(data)):
        data[i] = data[i][0]

    m_name = data

f_sname = []
with open(r"data\fmale_sname.txt", "r", encoding="utf-8") as out_file:

    data = out_file.readlines()[::]
    data = list(map(lambda x: x.split('\n')[:-1], data[:-1]))
    for i in range(3):
        for j in range(len(data[i])):
            f_sname.extend(list(map(lambda x: x[:-1], data[i][j].split())))

m_sname = []
with open(r"data\male_sname.txt", "r", encoding="utf-8") as out_file:

    data = out_file.readlines()[::]
    data = list(map(lambda x: x.split('\n')[:-1], data[:-1]))

    for i in range(4):
        m_sname.extend(data[i][0].split())


def rand_date():
    year = str(randint(1967, 2003))

    month = randint(1, 13)
    if month < 10:
        month = "0" + str(month)
    else:
        month = str(month)

    if month == 2:
        day = randint(1, 29)
    else:
        day = randint(1, 32)
    if day < 10:
        day = "0" + str(day)
    else:
        day = str(day)

    date = "-".join([year, month, day])
    return date

data = []

for i in range(100):

    data.append([f_name[randint(0, len(f_name) - 1)], f_sname[randint(0, len(f_sname) - 1)], rand_date(), "F", randint(1, 6),
                 randint(0, 1)])

for i in range(100):

    data.append([m_name[randint(0, len(m_name) - 1)], m_sname[randint(0, len(m_sname) - 1)], rand_date(), "M", randint(1, 6),
                 randint(0, 1)])
data1 = []
for i in range(200):
    data1.append(choice(data))
    ind = data.index(data1[i])
    del data[ind]
print(*data1, sep=',\n')