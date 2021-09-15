import pyautogui as p
import time as t

p.hotkey('ctrl', 'alt', 't')
t.sleep(0.6)
commands =["cd Downloads/", "mv *.pdf *.doc *.pptx *.epub pdf/", "mv *.mp4 *.mkv vedios/",
           "mv *.zip *.jar *.deb *.rar *.sh *.bin *.gz packages/",
           "mv *.torrent torrent/", "mv *.csv *.txt *.py *.ipynb files/", "mv *.mp3 *.mpga sound/",
           "mv *.jpg *.svg *.png *.jpeg *.webp *.gif photos/", "exit"]

for i in commands:
    p.write(i)
    p.press('enter')


