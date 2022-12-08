from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import time

s = Service('./driver/chromedriver')
browser = webdriver.Chrome(service=s)
# nombre de los contactos o parte del nombre, no diferencia entra may y min
contactos = ["Mirella", "Maria", "Mel", "Lestter",
             "Evelyn", "rosario", "julio", "abi", "anais"]
# browser = webdriver.Chrome(executable_path='./driver/chromedriver')

# si el qr aun existe en pantalla retorna true


def validaQR():
    try:
        element = browser.find_element(By.TAG_NAME, "canvas")
    except:
        print("no existe")
        return False
    return True


def buscarChat(nombre: str):
    # entra a la casilla de busqueda de chats
    print("BUSCANDO EL CHAT")
    try:
        browserbox = browser.find_element(
            By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    except StaleElementReferenceException:
        print("FALLO LA BUSQUEDA POR XPATH")
        pass
    browserbox.click()
    # ingresa el nombre del contacto o grupo
    browserbox.send_keys(nombre)
    time.sleep(1)
    browserbox.send_keys(Keys.ENTER)
    # esperamos para que cargue el chat seleccionado
    time.sleep(1)
    enviarMensaje()


def enviarMensaje(mensaje: str):
    chatbox = browser.find_element(
        By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
    chatbox.send_keys(
        "MENSAJE PRUEBA")
    chatbox.send_keys(Keys.ENTER)


def botWhatsapp():
    browser.get("https://web.whatsapp.com/")
    # esperamos que el que el qr cargue en la pag
    time.sleep(10)

    espera = True
    # mientras el qr este en pantalla entonces repetira el ciclo
    while espera:
        print("ESPERANDO QR")
        # si el qr no esta en la pantalla entonces espera cambia a false
        espera = validaQR()
        time.sleep(2)
        if espera == False:
            print("SE AUTENTICO QR")
            break
    # espera para que cargue los chats
    time.sleep(30)
    for nombre in contactos:
        buscarChat(nombre)
        time.sleep(1)


botWhatsapp()
