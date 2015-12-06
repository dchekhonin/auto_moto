__author__ = 'dchekhonin'

import time
from datetime import datetime
from selenium.webdriver.common.by import By

import pf_locators
from Page_factory.pageobject_support import cacheable, callable_find_by as find_by
from Page_factory.pf_classes import LoggerMixin
from pf_new_mail import Sent_mail_page


class HomePage(LoggerMixin):

    sure_link = find_by(how=By.ID,using=pf_locators.to_be_sure_id)
    sent_email_button = find_by(how=By.XPATH,using=pf_locators.sent_mail_menu)
    inbox_email_button = find_by(how=By.XPATH,using=pf_locators.inbox_mail_menu)

    def __init__(self, driver):
        super(HomePage, self).__init__()
        self._driver = driver

    def to_be_sure_link(self):

        return self.sure_link().text


    def default_active_menu_check(self):
        return self.inbox_email_button().get_attribute("tabindex")


    def active_menu_indication_check(self):
        self.sent_email_button().click()
        time.sleep(2)
        return self.sent_email_button().get_attribute("tabindex")


    def sent_mail_page(self):
        self.sent_email_button().click()
        time.sleep(5)
        return Sent_mail_page(self._driver)

