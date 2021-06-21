# -*- coding: utf-8 - *-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import unittest, time, re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class CarvivoConnexion(unittest.TestCase):
    def setUp(self):
        #options = Options()
        #options.headless = True
        #options.add_argument("window-size=1400,600")
        #self.driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\Chloe\Drivers\chromedriver.exe')
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"

    def test_CarvivoConnexion(self):
        driver = self.driver
        driver.get("https://pp-fr.carvivo.com/login")
        print("carvivoLogin")
        driver.set_window_size(1920, 1080)
        print(driver.current_url)
        self.assertEqual("Carvivo Contact | Connexion", driver.title)
        driver.save_screenshot('login.png')
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").send_keys("cmartin@carvivo.com")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").send_keys("xxxx")
        driver.find_element_by_id("_submit").click()
        print("connecter")
        print(driver.current_url)
        driver.switch_to_window(driver.window_handles[0])
        time.sleep(0.400)
        driver.save_screenshot('connexion.png')
        self.assertEqual("Carvivo Contact | Accueil", driver.title)
        driver.find_element_by_css_selector(".roles").click()
        element = driver.find_element_by_css_selector(".roles")
        elementval = element.text
        assert elementval == "Superviseur - Opérateur"
        driver.find_element_by_link_text("Mon compte").click()
        print(driver.current_url)
        self.assertEqual("Carvivo Contact", driver.title)
        driver.save_screenshot('compte.png')
        print("moncompte")
        driver.find_element_by_id("popupBanner").click()
        driver.switch_to_window(driver.window_handles[1])
        driver.set_window_size(1920, 1080)
        print(driver.current_url)
        self.assertEqual("Carvivo Contact", driver.title)
        driver.save_screenshot('popup.png')
        print("popup")
        driver.find_element_by_id("status-pause").click()
        driver.switch_to_window(driver.window_handles[0])
        print(driver.current_url)
        driver.save_screenshot('retour.png')
        print("retour")
        driver.find_element_by_css_selector(".icon-phone").click()
        print(driver.current_url)
        self.assertEqual("Carvivo Contact | Appels sortants", driver.title)
        driver.save_screenshot('phone.png')
        print("phone")
        time.sleep(1)
        driver.find_element_by_css_selector(".icon-envelope").click()
        print(driver.current_url)
        self.assertEqual("Carvivo Contact | Emails", driver.title)
        driver.save_screenshot('mail.png')
        time.sleep(0.5)
        driver.find_element_by_xpath("//a[@href='/operateur/email/modifier/1330527']").click()
        driver.save_screenshot('1mail.png')
        driver.find_element_by_css_selector(".icon-envelope").click()
        driver.find_element_by_xpath("//a[@href='/operateur/email/modifier/1309173']").click()
        driver.save_screenshot('2mail.png')
        print("email")
        driver.find_element_by_css_selector(".icon-search").click()
        driver.save_screenshot('recherche.png')
        print(driver.current_url)
        element = driver.find_element_by_id('search_type_0')
        driver.execute_script("arguments[0].click();", element)
        driver.save_screenshot('1recherche.png')
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='searchForm']/div[2]/div/div[2]/label[4]").click()
        print("recherche")
        driver.save_screenshot('2recherche.png')
        time.sleep(0.15)
        driver.find_element_by_css_selector(".icon-keyboard").click()
        print(driver.current_url)
        self.assertEqual("Carvivo Contact | Leads", driver.title)
        driver.save_screenshot('leads.png')
        print("leads")
        driver.find_element_by_link_text("Carvivo - Compte de démonstration").click()
        driver.save_screenshot('lead.png')
        assert self.driver.find_element(By.CSS_SELECTOR, ".toggle-more").text == "Bonjour concession X à votre écoute"
        elements = self.driver.find_elements(By.ID, "posId")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, "#posNotes > .header")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".icon-plus:nth-child(1)")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, "#customerInfos h3")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".icon-map")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, "#customFieldsBlock h3")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".icon-team")
        assert len(elements) > 0
        driver.find_element(By.CSS_SELECTOR, '#vnFilter').click()
        element = driver.find_element_by_id('lead_interest_40')
        driver.execute_script("arguments[0].click();", element)
        select_element = driver.find_element(By.CSS_SELECTOR, '#lead_VOLead_ads_0_brand')
        select_object = Select(select_element)
        select_object.select_by_index(2)
        driver.save_screenshot('filtre.png')
        print("leadcreat")
        time.sleep(2)
        select_elementbis = driver.find_element(By.CSS_SELECTOR, '#lead_VOLead_ads_0_model')
        select_objectbis = Select(select_elementbis)
        select_objectbis.select_by_index(6)
        driver.find_element(By.CSS_SELECTOR, '#lead_VOLead_ads_0_price').click()
        print("leadcreatv2")
        driver.find_element_by_id("lead_VOLead_ads_0_price").send_keys("3000")
        driver.save_screenshot('creatLead.png')
        element = driver.find_element_by_id('lead_customer_favoriteCommunicationMeans_0')
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_css_selector(".roles").click()
        driver.find_element_by_link_text("Déconnexion").click()
        print(driver.current_url)
        self.assertEqual("Carvivo Contact | Connexion", driver.title)
        driver.save_screenshot('deconnexion.png')
        print("deco")

        driver.close()

if __name__ == "__main__":
        unittest.main()