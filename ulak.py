#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import ulak_bot


def koltuk_bul(metin):
    
    sayaç = -1
    while(True):
        if (metin[sayaç] == '('):
            break
        else:
            sayaç = sayaç - 1
    
    yer_sayısı = 0
    for i in range(sayaç * (-1) -2 ):
        yer_sayısı += int(metin[(i*(-1))-2]) * pow(10,i)
    
    return yer_sayısı
        
        


driver = webdriver.Firefox()
driver.get("https://ebilet.tcddtasimacilik.gov.tr/view/eybis/tnmGenel/tcddWebContent.jsf")



time.sleep(2)
nereden = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/ul/li[1]/div/form/div[1]/p[4]/input")
nereye = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/ul/li[1]/div/form/div[2]/p[4]/input")
tarih = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/ul/li[1]/div/form/div[1]/p[6]/span/input")



nereden.send_keys("İzmit YHT")
nereye.send_keys("Konya")
tarih.clear()
tarih.send_keys("3.10.2022")

ulak_bot.gönder(f"Alarm Kuruldu...")
nereden.click()

time.sleep(2)

search_button = "/html/body/div[3]/div[2]/div/div[2]/ul/li[1]/div/form/div[3]/p[3]/button/span"
buton = driver.find_element(By.XPATH,search_button)
buton.click()

time.sleep(4)

#seferler = driver.find_elements(By.CSS_SELECTOR,"label.ui-selectonemenu-label.ui-inputfield.ui-corner-all")


seferler = driver.find_elements(By.CSS_SELECTOR,"tr.ui-widget-content")#.ui-datatable-even
#seferler2 = (driver.find_elements(By.CSS_SELECTOR,"tr.ui-widget-content.ui-datatable-odd"))

del seferler[-4:] #Boşluklu nesneler silindi

Kapasite = list()

for i in seferler:
    #print(i.text)
    #print("***************")
    #print(i.text.split("\n"))
    Kapasite = i.text.split("\n")
    if (koltuk_bul(Kapasite[9]) > 2):
        print("Yer var: ")
        print(i.text.split("\n"))
        ulak_bot.gönder("Yer var: "+ str(i.text.split("\n")) )



time.sleep(1)
driver.close()

