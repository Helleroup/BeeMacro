import time
from ahk import AHK

ahk = AHK()

def getMultiplier():
    print('sasd')

def getBuffs():
    buffs = {
        'polar power': '86EBFF'
    }
    #buff 1 top right corner 0, 58
    #buff 1 bottom left corner 37, 95
    #buff 1 bottom middle pixel 18, 95
    print('test')
    index = 0
    while True:
        index += 1
        startPos = {
            'x': 18,
            'y': 95
        }
        buffColor = ahk.pixel_get_color(startPos['x'], startPos['y'] * index)
        print(index, buffColor)
        if startPos['y'] * index > 1920:
            break

time.sleep(2)
if __name__ == "__main__":
    getBuffs()
