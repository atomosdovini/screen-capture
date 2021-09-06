import pyautogui
import time
x= 1

while True:
    print('captura-%s.png' % x)
    captura = pyautogui.screenshot(region=(533,132, 290, 575))
    captura.save(r'/home/ovni/nodau/screenCap/salvos/Tela-%s.png' % x)
    x = x+1
    time.sleep(2)
    if x > 11:
        break


#corte iphone 11, monitor lg22 
  #region=(533,132, 290, 575)