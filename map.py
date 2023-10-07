import random
from utils import randbool
from utils import randcell
from utils import randcell2



# 🟩🚁💦🔥🌫️🌿🌳💙🛒🏥🟫
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

CELL_TYPES = "🟨🚁💦🔥🌫️🌿🌳💙🛒🏥🟫"

class Map:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range (h)]

    def Generate_river(self, l):
        rc = randcell(self.w-2, self.h-2) # рандом исток
        rx, ry = rc[0], rc[1] # координаты исток
        self.cells[rx][ry] = 2 # отмечаем на карте исток реки
        if l > 1:              # если длина > 1
            while l > 1:       #пока длина больше 1
                rc2 = randcell2(rx, ry) #ищем клетку рядом
                rx2, ry2 = rc2[0], rc2[1] # нашли
                if rx2 < 0 or ry2 < 0 or rx2 > self.w or ry2 > self.h: # проверяем на отсутствие клетки на карте
                    rx2, ry2 = rx, ry # возвращаем предыдущие значения, если клетки на поле нет
                    rx, ry = rx2, ry2 # базовая клетка = полученному результату
                    l += 1 # длина +1, т.к 1 ход потерян впустую
                else:
                    self.cells[rx2][ry2] = 2 # закрашиваем, если клетка есть
                    rx, ry = rx2, ry2 # базовая клетка = полученному результату
                    l -= 1 # длина -1, т.к условие выполнено
                                    
    def Generate_forests(self, r, mxr):
        for ri in range (self.h):
            for ci in range (self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 5

    def print_map(self):
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
        print("🟫 "*(self.w + 2))
        for row in self.cells:
            print("🟫",end="")
            for cell in row:
                #if (cell >= 0 and cell <= len(CELL_TYPES)):
                #    print(CELL_TYPES[cell],end="")
                if cell == 0:
                    print('🟨', end='')
                elif cell == 1:
                    print('🚁 ', end='')
                elif cell == 2:
                    print('💦 ', end='')
                elif cell == 3:
                    print('🔥 ', end='')
                elif cell == 4:
                    print('🌫️ ', end='')
                elif cell == 5:
                    print('🌿 ', end='')
                elif cell == 6:
                    print('🌳 ', end='')
                elif cell == 7:
                    print('💙 ', end='')
                elif cell == 8:
                    print('🛒 ', end='')
                elif cell == 9:
                    print('🏥 ', end='')
                elif cell == 10:
                    print('🟫', end='')                       
            print("🟫",end = '')
            print(b)
            b += 1
        print("🟫 " * (self.w + 2))
           
    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            print("данная позиция отсутствует в поле игры")
        return True    

    def Generate_shop(self, rx, ry):
        rc = randcell(self.w, self.h) 
        rx, ry = rc[0], rc[1] 
        self.cells[rx][ry] = 8

    def Generate_apgrade(self, x, y):
        rc = randcell(self.w, self.h) 
        rx, ry = rc[0], rc[1] 
        self.cells[rx][ry] = 9    
    
    def Add_fire(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 6:
            self.cells[cx][cy] = 3

    def Add_tree(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 0:
           self.cells[cx][cy] = 5

    def Generate_oldtree(self):
        rc = randcell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        if self.cells[rx][ry] == 5:
            self.cells[rx][ry] = 6

    def Apdate_fires(self):
        for i in range (self.h):
            for j in range (self.w):
                cell = self.cells[i][j]
                if cell  == 3:
                    self.cells[i][j] = 0
        for i in range (20):
            self.Add_fire()            




'''print('Задайте параметры поля для игры, каждый более 10 ед.')
field = Map(int(input('Введите длину поля ')), int(input('Введите ширину поля ')))
field.print_map()

field.Generate_forests(int(input("Сколько % поля занимает лес? ")),100)
field.print_map()

print('Разместите на поле водоёмы')
n = (int(input("Сколько на поле водоемов? (только > 0)")))
if n == 1:
    print('Площадь водоёма ')
    field.Generate_river(l = int(input()))
elif n == 2:
    print('Площадь водоёма ')
    field.Generate_river(l = int(input()))
    print('Площадь водоёма ')
    field.Generate_river(l = int(input()))
else:
    for i in range(n):
        while i < n-1:
            print('Площадь водоёма ')
            field.Generate_river(l = int(input()))
            i += 1
        
field.print_map()



print('введите координаты магазина Y и X')
field.cells[int(input("Y ="))-1][int(input("X ="))-1]= 8
field.print_map()

print('введите координаты госпиталя Y и X')
field.cells[int(input("Y ="))-1][int(input("X ="))-1]= 9
field.print_map()'''

