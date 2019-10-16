from selenium import webdriver
import request
import urllib.request
import pandas as pd
import time
import random
import os
##import loginYap

userAgentData = pd.read_excel(r'..\instabot\useragent.xlsx')
userAgentDF = pd.DataFrame(userAgentData, columns = ['useragent'])
userAgent = userAgentDF.useragent.tolist()
biyografiData = pd.read_excel(r'..\instabot\biyografiler.xlsx')
biyografiDF = pd.DataFrame(biyografiData, columns = ['biyografiler'])
biyoGrafiler = biyografiDF.biyografiler.tolist()

def MAC():

    if i <= 25:
        os.system('spoof-mac.py set 00:1a:78:6d:57:63 en0')
    elif 25 < i <= 50:
        os.system('spoof-mac.py set 99:2a:87:8d:75:36 en0')
    elif 50 < i <= 75:
        os.system('spoof-mac.py set 50:3a:56:7d:93:42 en0')
    elif 75 < i <= 100:
        os.system('spoof-mac.py set 25:4a:65:1d:39:24 en0')
    else:
        os.system('spoof-mac.py set 75:5a:12:3d:30:17 en0')

    
for i in range(150):

    os.system('cmd/c "adb shell settings put global airplane_mode_on 0"')
    MAC()
    time.sleep(4)

    profile = webdriver.FirefoxProfile()
    url = "https://www.instagram.com"
    user_agent = random.choice(userAgent)
    request = urllib.request.Request(url, headers = {'User-Agent': user_agent})
    response = urllib.request.urlopen(request)
    html = response.read()
    print(user_agent)

    profile.set_preference("browser.privatebrowsing.autostart", True)
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False)
    
    profile.update_preferences()

    data = pd.read_excel (r'..\instabot\isimlistesi.xlsx')
    nameList = pd.DataFrame(data, columns = ['name'])
    surnameList = pd.DataFrame(data, columns = ['surname'])

    isim = nameList.name.tolist()
    soyIsim = surnameList.surname.tolist()

    numaralar = list(range(100, 9999))
    for i in range(len(numaralar)):
        numaralar[i] = str(numaralar[i])

    epostaUzantilari = ["@outlook.com", "@yahoo.com", "@aol.com", "@yandex.com", "@protonmail.com", "@zoho.com",
                        "@tutanaota.com","@tutanota.de", "@tutamail.com", "@tuta.io", "@keemail.me", "@icloud.com"]

    class Kisiler():

        def __init__(self, isim, soyIsim, numaralar, epostaUzantilari):
            self.isim = isim
            self.soyIsim = soyIsim
            self.numaralar = numaralar
            self.epostaUzantilari = epostaUzantilari

        def isimOlustur(self):
            olusanIsim = self.isim + self.soyIsim
            return olusanIsim

        def kullaniciAdi(self):
            olusanKullaniciAdi = self.isim + self.soyIsim + self.numaralar
            return olusanKullaniciAdi

        def epostaOlustur(self):
            olusanEposta = self.isim + self.soyIsim + self.numaralar + self.epostaUzantilari
            return olusanEposta

    girilecekIsim = random.choice(isim)
    girilecekSoyIsim = random.choice(soyIsim)
    girilecekNumara = random.choice(numaralar)
    girilecekEposta =  random.choice(epostaUzantilari)

    hesapOlustur = Kisiler(girilecekIsim, girilecekSoyIsim, girilecekNumara, girilecekEposta)

    print(hesapOlustur.isimOlustur())
    print(hesapOlustur.epostaOlustur())
    print(hesapOlustur.kullaniciAdi())

    browser = webdriver.Firefox(firefox_profile = profile)
    browser.get("https://www.instagram.com")
    time.sleep(5)

    epostaGir = browser.find_element_by_name("emailOrPhone")
    isimGir = browser.find_element_by_name("fullName")
    kullaniciAdiGir = browser.find_element_by_name("username")
    sifreGir = browser.find_element_by_name("password")

    epostaGir.send_keys(hesapOlustur.epostaOlustur())
    isimGir.send_keys(hesapOlustur.isimOlustur())
    kullaniciAdiGir.send_keys(hesapOlustur.kullaniciAdi())
    sifreGir.send_keys("aazz11224455bbyy")
    print("aazz11224455bbyy")
    time.sleep(5)

    kaydolButonu = browser.find_element_by_xpath("/html/body/span/section/main/article/div[2]/div[1]/div/form/div[7]/div/button")
    kaydolButonu.click()
    time.sleep(5)

    try:
        controlElement2 = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div/span')
        if controlElement2.is_enabled() == True:
            time.sleep(3)
             
            takipEtButtons = browser.find_elements_by_css_selector("._0mzm-.sqdOP.L3NKy")
            takipEtButtons[2].click()
            time.sleep(2)
            takipEtButtons[3].click()
            time.sleep(2)
            takipEtButtons[5].click()
            time.sleep(2)
            takipEtButtons[7].click()
            time.sleep(2)
            takipEtButtons[11].click()
            time.sleep(2)
            browser.close()
            with open("bilgiler.txt", "a") as text_file:
                text_file.write(hesapOlustur.kullaniciAdi()+":"+"aazz11224455bbyy\n")

            time.sleep(7)

            ##loginYap.loginYap()

            browser.delete_all_cookies()
            browser.close()
            print("**************************************")
            os.system('cmd/c "adb shell settings put global airplane_mode_on 1"')
            time.sleep(7)

    except:
        print("hesap olusturulamadi.....")
        print("********************************")
        browser.close()
        os.system('cmd/c "adb shell settings put global airplane_mode_on 1"')
        time.sleep(7)
