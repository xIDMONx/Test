from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

#
usuario = ""
contrasena = ""
# IP:PUERTO
proxy = "201.163.73.93:53281"
# Para mas proxys, verifica la siguiente liga: https://free-proxy-list.net/anonymous-proxy.html

# Opciones para el navegador, en este caso utilizare Google Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % proxy)
#
# Declaro la variable con la ruta donde se encuentra el controlador de chrome
executable_path = "C:/dev/chromedriver_win32/chromedriver.exe"
# Con proxy
chrome = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
# Sin proxy
# chrome = webdriver.Chrome(executable_path=executable_path)
# Indicamos la url del sitio a visitar, en este caso sera Instagram
chrome.get("https://www.instagram.com/accounts/login/")
chrome.maximize_window()
chrome.implicitly_wait(15)
#
# Datos que extraeremos de la pagina inspeccionada
username = chrome.find_element_by_xpath("//*[@name='username']")
# print(username)
password = chrome.find_element_by_xpath("//*[@name='password']")
# print(password)
#
time.sleep(2)
# Enviamos los datos
username.send_keys(usuario)
password.send_keys(contrasena)
# Emulamos un keypress
password.send_keys(Keys.ENTER)
# Verificamos si el inicio de sesion fue correcto
cookies_list = chrome.get_cookies()
#
login_status = False
for cookie in cookies_list:
    if cookie['name'] == 'csrftoken':
        login_status = True
        break

if login_status:
    print ('Sesion Iniciada')
    #
    Ahora_no = chrome.find_element_by_css_selector("button.HoLwm")
    # Cerramos el modal de la notificacion
    Ahora_no.click()
    # Nos movemos hasta la tematica de manga
    chrome.get("https://www.instagram.com/explore/tags/manga/")
    #
    # print len(chrome.find_elements_by_css_selector('div.eLAPa'))
    #
    # Si la cantidad obtenida de elementos es mayor a cero
    if len(chrome.find_elements_by_css_selector('div.eLAPa')) > 0:
        # Genero una lista de los elementos obtenidos
        elementos = chrome.find_elements_by_css_selector('div.eLAPa')
        # Del numero total de elementos, obtengo un numero aleatorio
        index = random.randint(0, len(chrome.find_elements_by_css_selector('div.eLAPa')))
        # print index
        # print elementos[index]
        # Emulo un click sobre la imagen
        elementos[index].click()
        # Sobre el fancybox, busco el elemento span que gace referencia al "Me Gusta" y hago click
        chrome.find_element_by_css_selector('div.eo2As').find_element_by_css_selector('span.fr66n').click()
    time.sleep(5)
    # Cerramos sesion
    chrome.get("https://instagram.com/accounts/logout/")
    # Cerramos chrome
    chrome.quit()
else:
    print ('Sesion no iniciada')
