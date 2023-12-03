idT = 1
idS = 1


class Team:
    def __init__(self, nameTeam, nameSchool):
        global idT
        self.id = f'Team{idT:02d}'
        idT += 1
        self.nameTeam = nameTeam
        self.nameSchool = nameSchool

    def __str__(self):
        return f'{self.id} {self.nameTeam} {self.nameSchool}'


class Student(Team):
    def __init__(self, nameStudent, nameTeam, nameSchool):
        super().__init__(nameTeam, nameSchool)
        global idS
        self.id = f'C{idS:03d}'
        idS += 1
        self.nameStudent = nameStudent

    def __str__(self):
        return f'{self.id} {self.nameStudent} {self.nameTeam} {self.nameSchool}'


n = int(input())
lstTeam = []
while n > 0:
    lstTeam.append(Team(input(), input()))
    n -= 1
lstStud = []
m = int(input())
while m > 0:
    studentName = input()
    idTeam = input()
    for i in lstTeam:
        if i.id == idTeam:
            lstStud.append(Student(studentName, i.nameTeam, i.nameSchool))
            break
    m -= 1
lstStud = sorted(lstStud, key=lambda x: x.nameStudent)
for i in lstStud:
    print(i)
