from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import random

def loginYap():

    browser = webdriver.Firefox(firefox_profile = profile)
    browser.get("https://www.instagram.com/")
    time.sleep(2)

    girisYap = browser.find_element_by_xpath("/html/body/span/section/main/article/div[2]/div[2]/p/a")
    girisYap.click()
    time.sleep(2)

    userGir = browser.find_element_by_name("username")
    sifreGir = browser.find_element_by_name("password")

    userGir.send_keys(hesapOlustur.kullaniciAdi())
    sifreGir.send_keys("aazz11224455bbyy")
    time.sleep(2)

    girisButton = browser.find_element_by_xpath("/html/body/span/section/main/div/article/div/div[1]/div/form/div[4]/button/div")
    girisButton.click()
    time.sleep(5)

    simdiDegil = browser.find_element_by_css_selector("button.aOOlW:nth-child(2)")
    simdiDegil.click()
    time.sleep(2)

    profileDuzenleButton = browser.find_element_by_xpath("/html/body/span/section/main/div/header/section/div[1]/a/button")
    profileDuzenleButton.click()
    time.sleep(2)

    biyografiDuzenleButton = browser.find_element_by_xpath("//*[@id='pepBio']")
    biyografiDuzenleButton.click()
    time.sleep(2)
    biyografiDuzenleButton.send_keys(random.choice(biyoGrafiler))

    gonderButton = browser.find_element_by_xpath("/html/body/span/section/main/div/article/form/div[11]/div/div/button[1]")
    gonderButton.click()
    time.sleep(5)

    profileButton = browser.find_element_by_xpath("/html/body/span/section/nav/div[2]/div/div/div[3]/div/div[3]/a/span")
    profileButton.click()
    time.sleep(5)

    followersButton = browser.find_element_by_xpath("/html/body/span/section/main/div/header/section/ul/li[3]/a")
    followersButton.click()
    time.sleep(3)

    anyFollower = browser.find_elements_by_class_name("FPmhX.notranslate._0imsa")
    anyFollower[0].click()
    time.sleep(3)

    gonderiAc = browser.find_element_by_class_name("eLAPa")
    gonderiAc.click()
    time.sleep(4)

    begenBas = browser.find_element_by_css_selector("html.js.logged-in.client-root body div._2dDPU.vCf6V div.zZYga div.PdwC2._6oveC.Z_y-9 article.M9sTE.L_LMM.JyscU.ePUX4 div.eo2As section.ltpMr.Slqrh span.fr66n button.dCJp8.afkep._0mzm-")
    begenBas.click()
    time.sleep(3)

    carpiBas = browser.find_element_by_class_name("ckWGn")
    carpiBas.click()
    time.sleep(3)

    profileButton = browser.find_element_by_xpath("/html/body/span/section/nav/div[2]/div/div/div[3]/div/div[3]/a/span")
    profileButton.click()
    time.sleep(5)

    menuButton = browser.find_element_by_css_selector("html.js.logged-in.client-root body span#react-root section._9eogI.E3X2T main.SCxLW.o64aR div.v9tJq.VfzDr header.vtbgv section.zwlfE div.nZSzR div.AFWDX button.dCJp8.afkep._0mzm- span.glyphsSpriteSettings__outline__24__grey_9.u-__7")
    menuButton.click()
    time.sleep(3)

    logOut = browser.find_element_by_xpath("/html/body/div[3]/div/div/div/button[6]")
    logOut.click()
    time.sleep(3)
