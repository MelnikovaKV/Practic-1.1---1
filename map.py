from utils import randbool
from utils import randcell
from utils import randcell2



# 🟩🚁💦🔥🌫️🌿🌳💙🛒🏥🟫💧
# 0 - поле
# 1 - вертолет
# 2 - река
# 3 - огонь
# 4 - облако
# 5 - саженец
# 6 - дерево
# 7 - жизнь
# 8 - магазин
# 9 - аптека
# 10 - край поля
# 13 - 
# 14 - 
# n - количество водоемов

CELL_TYPES = [('🟨'), ('🚁 '), ('💦 '), ('🔥 '), ('🌫️ '), ('🌿 '), ('🌳 '), ('💙 '), ('🛒 '), ('🏥 '), ('🟫')]

BONUS_TREE = 100
# FINE_TREE = 200
UPGRADE_COST = 5000
# TODO: поднять до 10000
LIFE_COST = 1000


class Map:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range (h)]
        self.generate_forests(5,10)
        self.generate_river(10)
        self.generate_river(10)
        self.generate_upgrade_shop()
        self.generate_hospital()
        

    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True
    
    def print_map(self, helico, clouds):
        a = 1
        b = 1
        print('X :', end = '')
        while a < self.w:
            if a < 10:
                print(a," ", end='')
                a += 1
            else:
                print(a,"", end='')
                a += 1
        print(a)
        print("🟫 " * (self.w + 2))
        for ri in range (self.h):
            print("🟫",end="")
            for ci in range (self.w):
                cell  = self.cells[ri][ci]
                if (clouds.cells[ri][ci] == 1):
                    print('☁️  ', end='')
                elif (clouds.cells[ri][ci] == 2):
                    print('⚡ ', end='')
                elif (helico.x == ri and helico.y == ci):
                    print('🚁 ', end='')
                elif (cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end = "")
            print("🟫",end = '')
            print(b)
            b += 1
        print("🟫 " * (self.w + 2))
           
    def generate_river(self, l):
        rc = randcell((self.w-2), (self.h-2))
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if (self.check_bounds(rx2, ry2)):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1

    def generate_forests(self, r, mxr):
        for ri in range (self.h):
            for ci in range (self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 5

    # def generate_oldtree(self):
    #     rc = randcell(self.w, self.h)
    #     rx, ry = rc[0], rc[1]
    #     if self.cells[rx][ry] == 5:
    #         self.cells[rx][ry] = 6

    def generate_upgrade_shop(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 8

    def generate_hospital(self):
        rc = randcell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        if self.cells[rx][ry] != 8:
            self.cells[rx][ry] = 9
        else:
            self.generate_hospital()
    
    def add_fire(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 5:
            self.cells[cx][cy] = 3

    def add_tree(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 0:
           self.cells[cx][cy] = 5

    def update_fires(self):
        for ri in range (self.h):
            for ci in range (self.w):
                cell = self.cells[ri][ci]
                if cell  == 3:
                    self.cells[ri][ci] = 0
        for i in range (10):
            self.add_fire()

    def process_helicopter(self, helico, clouds):
        c = self.cells[helico.x][helico.y]
        d = clouds.cells[helico.x][helico.y]
        if (c == 2):
            helico.tank = helico.mxtank
        if (c == 3 and helico.tank > 0):
            helico.tank -= 1
            helico.score += BONUS_TREE
            self.cells[helico.x][helico.y] = 6
        if (c == 8 and helico.mxtank != 5 and helico.score >= UPGRADE_COST):
            helico.mxtank += 1
            helico.score -= UPGRADE_COST
        if (c == 9 and helico.score >= LIFE_COST):
            helico.lives += 10
            helico.score -= LIFE_COST
        if (d == 2):
            helico.lives -= 1
            if helico.lives == 0:
                helico.game_over()

    def export_data (self):
        return {"cells ": self.cells}
    
    def import_data(self, data):
        self.cells = data["cells"] or [[0 for i in range(self.w)] for j in range (self.h)]





'''print('Задайте параметры поля для игры, каждый более 10 ед.')
field = Map(int(input('Введите длину поля ')), int(input('Введите ширину поля ')))
field.print_map()

field.generate_forests(int(input("Сколько % поля занимает лес? ")),100)
field.print_map()

print('Разместите на поле водоёмы')
n = (int(input("Сколько на поле водоемов? (только > 0)")))
if n == 1:
    print('Площадь водоёма ')
    field.generate_river(l = int(input()))
elif n == 2:
    print('Площадь водоёма ')
    field.generate_river(l = int(input()))
    print('Площадь водоёма ')
    field.generate_river(l = int(input()))
else:
    for i in range(n):
        while i < n-1:
            print('Площадь водоёма ')
            field.generate_river(l = int(input()))
            i += 1
        
field.print_map()



print('введите координаты магазина Y и X')
field.cells[int(input("Y ="))-1][int(input("X ="))-1]= 8
field.print_map()

print('введите координаты госпиталя Y и X')
field.cells[int(input("Y ="))-1][int(input("X ="))-1]= 9
field.print_map()
'''
