import time
import random
import numpy as np
from collections import defaultdict, Counter
from ahk import AHK
import pyautogui as pgui
import easyocr as ocr

ahk = AHK()

def respawn():
    ahk.key_press('escape')
    time.sleep(0.1)  # Wait for the menu to open
    ahk.key_press('r')
    time.sleep(0.1)  # Wait for the menu to open
    ahk.key_press('enter')
    time.sleep(7) # wait for respawn
    ahk.key_press('o')
    ahk.send_input('....')
    time.sleep(0.3)  # wait for camera to rotate
    if ahk.pixel_get_color(960, 1050) == '0xFFFF00':  # Check if the pixel at (960, 1050) is yellow
        ahk.send_input('....')
        return True
    else:
        ahk.send_input('....')
        return False

def memoryGame(location=''):

    chances = 6

#    items = {
#        'royaljelly': {
#            'color': '0x9A6EB%',
#            'checkCount': False
#        },
#        'blueberry': {
#            'color': '0xB1803E',
#            'checkCount': False
#        }
#    }

    if location != 'extreme':
        cards = {
            1: {
                'x': 839,
                'y': 419,
                'item': '',
            },
            2: {
                'x': 919,
                'y': 419,
                'item': '',
            },
            3: {
                'x': 999,
                'y': 419,
                'item': '',
            },
            4: {
                'x': 1079,
                'y': 419,
                'item': '',
            },
            5: {
                'x': 839,
                'y': 499,
                'item': '',
            },
            6: {
                'x': 919,
                'y': 499,
                'item': '',
            },
            7: {
                'x': 999,
                'y': 499,
                'item': '',
            },
            8: {
                'x': 1079,
                'y': 499,
                'item': '',
            },
            9: {
                'x': 839,
                'y': 579,
                'item': '',
            },
            10: {
                'x': 919,
                'y': 579,
                'item': '',
            },
            11: {
                'x': 999,
                'y': 579,
                'item': '',
            },
            12: {
                'x': 1079,
                'y': 579,
                'item': '',
            },
            13: {
                'x': 839,
                'y': 659,
                'item': '',
            },
            14: {
                'x': 919,
                'y': 659,
                'item': '',
            },
            15: {
                'x': 999,
                'y': 659,
                'item': '',
            },
            16: {
                'x': 1079,
                'y': 659,
                'item': '',
            },
        }

        for _ in range(chances):
            groupedCards = defaultdict(list)
            for cardId, card in cards.items():
                item = card['item']
                if item != '':
                    groupedCards[item].append(cardId)

            pairs = {item: ids for item, ids in groupedCards.items() if len(ids) >= 2}
            if len(pairs) >= 1:  # Check if there are at least 1 pairs
                print(pairs)
                firstPair = list(pairs.values())[0]
                for card in firstPair:
                    ahk.click(cards[card]['x'], cards[card]['y'])
                    ahk.mouse_move(960, 360)  # Center the mouse position
                    print(f"Clicked on card {card} at ({cards[card]['x']}, {cards[card]['y']})")
                    del cards[card]  # Remove the card from the dictionary
                    time.sleep(0.8)  # Wait for the card to flip
            else:
                clickedCard = random.choice([item for item in cards.items() if item[1]['item'] == ''])
                print('clicked (random)', clickedCard)
                ahk.click(clickedCard[1]['x'], clickedCard[1]['y'])  # Click on the card
                ahk.mouse_move(960, 360)  # Center the mouse position
                time.sleep(0.8)  # Wait for the card to flip
                clickedColor = ahk.pixel_get_color(clickedCard[1]['x'], clickedCard[1]['y'])  # Get the color of the card
#                clickedColor = '0xF93600'
                clickedCard[1]['item'] = clickedColor
#                colorSuccess = False
#                for color, item in items.items():
#                    if clickedColor == color: # Check if the color matches any item
#                        colorSuccess = True
#                        clickedCard[1]['item'] = item  # Set the item for the card
#                        break
#                if not colorSuccess:
#                    items[f'{_}1'] = clickedColor
#                    clickedCard[1]['item'] = '{_}'  # Set the item for the card to '{_}' if no match found
                match = None
                for card, value in cards.items():
                    if value['item'] == clickedCard[1]['item'] and card != clickedCard[0]:
                        print(value['item'])
                        print(clickedCard[1]['item'])
                        print('match found')
                        match = card
                        break
                if match:
                    ahk.click(cards[match]['x'], cards[match]['y'])
                    ahk.mouse_move(960, 360)  # Center the mouse position
                    print('clicked (match)', match)
                    del cards[clickedCard[0]], cards[match]
                else:
                    clickedCard2 = random.choice([item for item in cards.items() if item[1]['item'] == '' and item[0] != clickedCard[0]])
                    print('clicked (random)', clickedCard2)
                    ahk.click(clickedCard2[1]['x'], clickedCard2[1]['y'])  # Click on the card
                    ahk.mouse_move(960, 360)  # Center the mouse position
                    #time.sleep(0.8)  # Wait for the card to flip
                    clickedColor2 = ahk.pixel_get_color(clickedCard2[1]['x'], clickedCard2[1]['y'])  # Get the color of the card
#                    clickedColor2 = '0x9A6EB5'
                    clickedCard2[1]['item'] = clickedColor2
#                    colorSuccess2 = False
#                    for color, item in items.items():
#                        if clickedColor2 == color:
#                            colorSuccess2 = True
#                            clickedCard2[1]['item'] = item
#                            break
#                    if not colorSuccess2:
#                        items[f'{_}2'] = clickedColor2
#                        clickedCard2[1]['item'] = '{_}'  # Set the item for the card to '{_}' if no match found
                    if clickedCard[1]['item'] == clickedCard2[1]['item']:
                        del cards[clickedCard[0]], cards[clickedCard2[0]]
            time.sleep(1.5)
        print(cards)
#        print(items)

   # print(clickedCards)

def getMovespeed():
    ahk.click(x=253, y=129)
    ahk.mouse_move(315, 211, relative=False, speed=3)  # Move the mouse to (315, 211)
    ahk.mouse_drag(315, 726, relative=False, speed=4) # Holds down primary button and moves the mouses
    time.sleep(0.3)  # Wait for the drag to complete
    img = np.array(pgui.screenshot(region=(213, 170, 70, 35)))
    reader = ocr.Reader(['en'])
    result = reader.readtext(img, detail = 0)
    return int(result[0]) if result else None

def containerFull():
   # print(ahk.pixel_get_color(1200, 50))
    if ahk.pixel_get_color(1239, 39) == '0xF70017':  # Check if the pixel at (960, 1050) is red
        print('full')
        return True
    else:
        print('not full')
        return False


time.sleep(2)
memoryGame()
