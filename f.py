import pyautogui as pg
import time


#ຕຳແໜ່ງກົດ mye
#Point(x=459, y=1067)

#ຕຳແໜ່ງບ່ອນກົດຂົນຫາ
#Point(x=180, y=57)

#------------#
#ທາງຕຳແໜ່ງບ່ອນເມົ້າ
#print(pg.position())


#for i in range(100):
   #pg.click(x=386, y=433)

pg.moveTo(x=459, y=1067)
time.sleep(10)
pg.doubleClick()
time.sleep(10)
pg.moveTo(x=180, y=57)
pg.click()
time.sleep(10)
pg.typewrite("google.com")
pg.typewrite(['enter'])
pg.moveTo(x=596, y=481)
pg.click()
time.sleep(10)
pg.typewrite("youtube.com")
pg.typewrite(['enter'])
pg.moveTo(x=164, y=309)
pg.click()
pg.moveTo(x=250, y=319)
pg.doubleClick()
pg.moveTo(x=220, y=305)
pg.doubleClick()
