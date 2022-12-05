import pyautogui as pg
import time
import webbrowser as web
phone_no = "+51958898045"
parsedMessage = " "
web.open('https://web.whatsapp.com/send?phone=' +
         phone_no+'&text='+parsedMessage)
time.sleep(20)
pg.write('🍿')
pg.write(' ')
pg.press('enter')
print('Mensaje  enviado')
time.sleep(4)
pg.hotkey('ctrl', 'w')
