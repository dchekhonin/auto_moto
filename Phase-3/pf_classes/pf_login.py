__author__ = 'dchekhonin'


from pf_homepage import HomePage
import pf_locators
from Page_factory.pageobject_support import cacheable, callable_find_by as find_by
from selenium.webdriver.common.by import By
from selenium  import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from datetime import datetime

class LoginPage(object):

    login_box = find_by(how=By.ID,using=pf_locators.email_id)
    submit_email_button = find_by(how=By.ID,using=pf_locators.email_confirm_next_id)
    pass_box = find_by(how=By.ID,using=pf_locators.email_password_id)
    submit_signin_button = find_by(how=By.ID,using=pf_locators.email_signin_id)
    error_message = find_by(how=By.ID,using=pf_locators.email_error)
    password_error = find_by(how=By.ID,using=pf_locators.password_error)

    def __init__(self,driver):
        self._driver = driver


    def login_error_mail(self,email):
        try:
            self.login_box().send_keys(email)
            self.submit_email_button().click()
            time.sleep(2)
            return self.error_message().text
        except Exception as e:
            print e
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self._driver.get_screenshot_as_file('screenshot-%s in LoginPage_login_er_mail.png' % now)

    def login_error_password(self,email,password):
        try:
            self.login_box().send_keys(email)
            self.submit_email_button().click()
            self.pass_box().send_keys(password)
            self.submit_signin_button().click()
            time.sleep(2)
            return self.password_error().text
        except Exception as e:
            print e
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self._driver.get_screenshot_as_file('screenshot-%s in LoginPage_login_er_pass.png' % now)

    def login(self,email,password):
        try:
            self.login_box().send_keys(email)
            self.submit_email_button().click()
            self.pass_box().send_keys(password)
            self.submit_signin_button().click()
            self._driver.implicitly_wait(5)
            return HomePage(self._driver)
        except Exception as e:
            print e
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self._driver.get_screenshot_as_file('screenshot-%s in LoginPage_login.png' % now)


