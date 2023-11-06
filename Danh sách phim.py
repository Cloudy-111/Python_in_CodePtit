idxFilm = 1


class Film:
    def __init__(self, type, start, name, vols):
        self.type = type
        global idxFilm
        self.id = f'P{idxFilm:03d}'
        idxFilm += 1
        self.name = name
        self.day = start[:2]
        self.month = start[3:5]
        self.year = start[6:]
        self.vols = vols

    def __str__(self):
        return f'{self.id} {self.type} {self.day}/{self.month}/{self.year} {self.name} {self.vols}'


n, m = [int(x) for x in input().split()]
type = []
for i in range(n):
    type.append(input())

film = []
for i in range(m):
    tp = input()
    start = input()
    name = input()
    vols = int(input())
    film.append(Film(type[int(tp[2::]) - 1], start, name, vols))

film = sorted(film, key=lambda x: (x.year, x.month, x.day, x.name, -x.vols))
for i in film:
    print(i)
