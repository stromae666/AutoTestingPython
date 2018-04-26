# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class firsttest(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_firsttest(self):
        success = True
        wd = self.wd
        wd.get("https://www.auto-club.biz/")
        wd.find_element_by_link_text("АВТОКЛУБ").click()
        wd.find_element_by_link_text("ПРОЕКТЫ").click()
        wd.find_element_by_link_text("ПОЛЬЗОВАТЕЛЮ").click()
        wd.find_element_by_link_text("ПАРТНЕРУ").click()
        wd.find_element_by_link_text("БИЗНЕСУ").click()
        wd.find_element_by_link_text("ВХОД").click()
        wd.find_element_by_name("USER_LOGIN").click()
        wd.find_element_by_name("USER_LOGIN").clear()
        wd.find_element_by_name("USER_LOGIN").send_keys("camryvod")
        wd.find_element_by_name("USER_PASSWORD").click()
        wd.find_element_by_name("USER_PASSWORD").clear()
        wd.find_element_by_name("USER_PASSWORD").send_keys("Mycamry17")
        wd.find_element_by_name("Login").click()
        wd.find_element_by_link_text("ГЛАВНАЯ").click()
        wd.find_element_by_link_text("ЛИЧНЫЙ КАБИНЕТ").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
