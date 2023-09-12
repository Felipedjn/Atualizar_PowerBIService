from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

options = ChromeOptions()
options.add_argument('-headless')
navegador = webdriver.Chrome(ChromeDriverManager().install(), options=options)

link_bi = ('https://app.powerbi.com/groups/me/list?experience=power-bi')
link_dash = ('LINK DO DASH AQUI')

def atualizar():
    # Login
    navegador.get(link_bi) # entrar no Site
    navegador.maximize_window() # maximizar o Navegador (Pois os elementos mudam conforme o tamanho da janela)
    sleep(3)
    navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div[1]/div[2]/input').send_keys('EMAIL AQUI') # usuario
    navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/button').send_keys(Keys.RETURN) # enter
    sleep(8)
    navegador.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input').send_keys('SENHA AQUI') # senha
    navegador.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input').send_keys(Keys.RETURN) # enter
    sleep(3)
    navegador.find_element(By.XPATH, '/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input').send_keys(Keys.RETURN) # entrar
    sleep(3)
    navegador.get(link_dash)
    sleep(5)

    intervalo = 3

    while True:
        navegador.find_element(By.XPATH, '/html/body/div[1]/root/mat-sidenav-container/mat-sidenav-content/tri-shell-panel-outlet/tri-extension-panel-outlet/mat-sidenav-container/mat-sidenav-content/div/div/div[1]/tri-shell/tri-extension-page-outlet/div[2]/dataset-details-container/dataset-action-bar/action-bar/action-button[2]/button').send_keys(Keys.RETURN) 
        sleep(2)
        navegador.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/div/div/span[1]/button').send_keys(Keys.RETURN) # atualizar
        sleep(3)
        time.sleep(intervalo)

atualizar()