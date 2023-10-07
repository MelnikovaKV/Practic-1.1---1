
from map import Map
import time
import os

TICK_SLEEP = 0.05
TREE_APDATE = 50
OLDTREE_APDATE = 40
FIRE_APDATE = 500
FIRE_ADD = 50

field = Map(20,10)
field.Generate_forests(30,100)
field.Generate_river(10)
field.Generate_river(5)        
field.Generate_shop(2,2)
field.Generate_apgrade(9,19)
field.print_map()



tick = 1

while True:
    os.system('cls')
    print('TICK ', tick)
    field.print_map()
    tick += 1
    time.sleep(TICK_SLEEP)
    if tick % TREE_APDATE == 0:
        field.Add_tree()
    if tick % OLDTREE_APDATE == 0:
        field.Generate_oldtree()
    if tick % FIRE_ADD == 0:
        field.Add_fire()
    if tick % FIRE_APDATE == 0:
        field.Apdate_fires()