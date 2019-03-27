from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#
usuario = "jchamps_gb"
contrasena = "aNh8htTGBZhZyzGMX9s3CYuwzpo4tU25E50fq1LB2XV8A9LOSs"
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
# chrome = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
# Sin proxy
chrome = webdriver.Chrome(executable_path=executable_path)
# Indicamos la url del sitio a visitar, en este caso sera Instagram
chrome.get("https://www.instagram.com/accounts/login/")
#
time.sleep(2)
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
