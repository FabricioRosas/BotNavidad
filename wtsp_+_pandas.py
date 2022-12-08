from random import randint
import pyautogui as pg
import time
import webbrowser as web
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

df1 = pd.read_excel('archivo1.xlsx', header=None)
total_rows1 = len(df1.axes[0])
random = randint(0, total_rows1)
reg1 = df1.loc[random, 0]
phone_no = "+51973675245"
parsedMessage = " "
web.open('https://web.whatsapp.com/send?phone=' +
         phone_no+'&text='+parsedMessage)
time.sleep(8)
pg.write(reg1)
pg.press('enter')
print('Mensaje enviado')
pass
pg.alert('Bomba de mensajes finalizada')
