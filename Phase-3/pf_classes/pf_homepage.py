__author__ = 'dchekhonin'

import pf_locators
from Page_factory.pageobject_support import cacheable, callable_find_by as find_by
from selenium.webdriver.common.by import By
from pf_new_mail import Sent_mail_page
import time
from datetime import datetime



class HomePage(object):

    sure_link = find_by(how=By.ID,using=pf_locators.to_be_sure_id)
    sent_email_button = find_by(how=By.XPATH,using=pf_locators.sent_mail_menu)
    inbox_email_button = find_by(how=By.XPATH,using=pf_locators.inbox_mail_menu)

    def __init__(self,driver):
        self._driver = driver

    def to_be_sure_link(self):
        try:
            return self.sure_link().text
        except Exception as e:
            print e
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self._driver.get_screenshot_as_file('screenshot-%s in HomePage_tbs_link.png' % now)

    def default_active_menu_check(self):
        try:
            return self.inbox_email_button().get_attribute("tabindex")
        except Exception as e:
            print e
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self._driver.get_screenshot_as_file('screenshot-%s in HomePage_def_act_menu.png' % now)

    def active_menu_indication_check(self):
        try:
            self.sent_email_button().click()
            time.sleep(2)
            return self.sent_email_button().get_attribute("tabindex")
        except Exception as e:
            print e
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self._driver.get_screenshot_as_file('screenshot-%s in HomePage_act_menu_ind.png' % now)

    def sent_mail_page(self):
        try:
            self.sent_email_button().click()
            time.sleep(3)
            return Sent_mail_page(self._driver)
        except Exception as e:
            print e
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self._driver.get_screenshot_as_file('screenshot-%s in HomePage_sent_mail_btn' % now)
