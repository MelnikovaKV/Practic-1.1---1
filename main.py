from pynput import keyboard
from clouds import Clouds
from map import Map
import time
import os
import json
from helicopter import Helicopter as Helico


TICK_SLEEP = 0.05
TREE_APDATE = 50
# OLDTREE_APDATE = 50
CLOUD_UPDATE = 100
FIRE_UPDATE = 100
# FIRE_ADD = 50
MAP_W, MAP_H = 20, 10


field = Map(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
helico = Helico (MAP_W, MAP_H)
tick = 1

MOVES = {'a' : (0,-1),'w':(-1,0),'s':(1,0),'d':(0,1),'A' : (0,-1),'W':(-1,0),'S':(1,0),'D':(0,1)}
# f - сохранение, g - восстановление
def process_key(key):
    global helico, tick, clouds, field
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx,dy)
    if c == "f":
        data = {"helicopter" : helico.export_data(),
                    "clouds" : clouds.export_data(),
                    "field" : field.export_data(),
                    "tick" : tick}
        with open("level.json", "w") as lvl:
            json.dump(data, lvl)
    if c == "g":
        with open("level.json", "r") as lvl:
            data =json.load(lvl)
            helico.import_data(data["helicopter"])
            tick.data["tick"]
            clouds.import_data(data["clouds"])
            field.import_data(data["field"])

listener = keyboard.Listener(
    on_press=None,
    on_release=process_key,)
listener.start()



while True:
    os.system('cls') 
    field.process_helicopter(helico, clouds)
    helico.print_stats()
    field.print_map(helico, clouds)
    print('TICK ', tick)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_APDATE == 0):
        field.add_tree()
    # if (tick % FIRE_ADD == 0):
    #     field.add_fire()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()
    if (tick % CLOUD_UPDATE == 0):
        clouds.update()