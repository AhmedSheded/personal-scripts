import pyautogui as p
import time as t
t.sleep(2)
positions = [[1870, 140], [1630, 411], [1615, 250], [170, 333], [1000, 755], [1130, 592]]
time = [2, 2, 5, 5, 3, 6]
positions2 = [[1221, 445], [686, 481], [811, 526]]
time2 = [3, 1, 0.3]


def movement(positions, time):
    for i in range(len(time)):
        p.click(x=positions[i][0], y=positions[i][1])
        t.sleep(time[i])


movement(positions, time)

p.moveTo(936, 384)
p.doubleClick()
p.write("password")
t.sleep(0.2)

movement(positions2, time2)

p.write("Sorry I can't explain")
t.sleep(0.5)
p.click(x=707, y=725)
t.sleep(2)
p.click(x=1091, y=553)
