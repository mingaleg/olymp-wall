from figlet import generate
from textdraw import TextDraw
from textmul import multiply

from sys import argv

ID = argv[1]
SURNAME = argv[2]
NAME = argv[3]
GRAD = argv[4] + ' класс'

YEAR = '2014'

T = TextDraw(128, 320)

T.box(0, 0, 127, 319)

T.box(3, 3, 35, 315)
T.puttext(generate('Региональный этап'), 5, 5, y1=314)
T.puttext(generate('всероссийской олимпиады школьников'), 15, 5, y1=314)
T.puttext(generate('по информатике'), 25, 5, y1=314)

T.box(36, 3, 84, 315)

T.box(30, 228, 40, 290)
T.puttext(generate(YEAR), 32, 230, y1=288)
T.box(30, 28, 40, 90)
T.puttext(generate(GRAD), 32, 30, y1=86)

T.box(85, 3+133+56, 124, 181+134)
T.puttext(open('banner').read(), 87, 5+134+56)

T.box(85, 3, 124, 134+56)
T.puttext(multiply(generate(ID), 4), 91, 5, y1=132+56)

T.puttext(multiply(generate(SURNAME), 2), 45, 5, y1=314)
T.puttext(multiply(generate(NAME), 2), 65, 5, y1=314)

T.print()
