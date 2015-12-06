__author__ = 'dchekhonin'

import unittest
import logging
from selenium  import webdriver
from pf_classes.pf_input import main_email_site
from pf_classes.pf_login import LoginPage
import pf_classes.pf_input
import  allure
from allure.constants import AttachmentType


class WebDriverMixin(object):

    def __init__(self):
        self.driver = None

    def init_webdriver(self):
        self.driver = webdriver.Chrome()

        self.driver.get(main_email_site)
        self.driver.implicitly_wait(10)

    def close_webdriver(self):
        self.driver.close()


class MyTestCase(unittest.TestCase, WebDriverMixin):

    def setUp(self):
        self.init_webdriver()

    def tearDown(self):
        self.close_webdriver()

    #checking login with asserting home page and 'sent' page links.
    def test_mail_Login(self):
        with allure.MASTER_HELPER.step('Assert login and Sent page link'):
            home = LoginPage(self.driver)
            result = home.login(pf_classes.pf_input.email,pf_classes.pf_input.password)
            allure.MASTER_HELPER.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)

        assert pf_classes.pf_input.assert_homepage_item in result.to_be_sure_link()
        assert pf_classes.pf_input.assert_sentmailpage_item in result.sent_mail_page().sent_to_be_sure_link()

    #checking correct error message during login with empty email
    def test_login_func_empty_mail(self):
        with allure.MASTER_HELPER.step('Login with empty mail'):
            page = LoginPage(self.driver)
            result = page.login_error_mail(pf_classes.pf_input.empty_email)
            allure.MASTER_HELPER.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        assert pf_classes.pf_input.assert_empty_email_error in result

    #checking correct error message during login with incorrect email
    def test_login_func_incorrect_mail(self):
        with allure.MASTER_HELPER.step('Login with incorrect email'):
            page = LoginPage(self.driver)
            result = page.login_error_mail(pf_classes.pf_input.incorrect_email)
            allure.MASTER_HELPER.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        assert pf_classes.pf_input.assert_incorrect_email_error in result

    #checking correct error message during login with empty password
    def test_login_func_empty_password(self):
        with allure.MASTER_HELPER.step('Login with empty password'):
            page = LoginPage(self.driver)
            result = page.login_error_password(pf_classes.pf_input.email,pf_classes.pf_input.empty_password)
            allure.MASTER_HELPER.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        assert pf_classes.pf_input.assert_empty_password_error in result

    #checking correct error message during login with incorrect password
    def test_login_func_incorrect_password(self):
        with allure.MASTER_HELPER.step('Login with incorrect password'):
            page = LoginPage(self.driver)
            result = page.login_error_password(pf_classes.pf_input.email,pf_classes.pf_input.incorrect_password)
            allure.MASTER_HELPER.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        assert pf_classes.pf_input.assert_incorrect_password_error in result

    #checking menu 'Inbox' is active by default.
    def test_default_active_menu(self):
        with allure.MASTER_HELPER.step('Inbox is active by default'):
            home = LoginPage(self.driver)
            result = home.login(pf_classes.pf_input.email,pf_classes.pf_input.password)
            allure.MASTER_HELPER.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        assert int(result.default_active_menu_check()) == 0

    #checking menu 'Sent' becomes active after click and menu 'Inbox' becomes inactive.
    def test_menu_active_indication(self):
        with allure.MASTER_HELPER.step('menu Sent becomes active after click and menu Inbox becomes inactive'):
            home = LoginPage(self.driver)
            result = home.login(pf_classes.pf_input.email,pf_classes.pf_input.password)
            allure.MASTER_HELPER.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        assert int(result.active_menu_indication_check()) == 0
        assert int(result.default_active_menu_check()) == -1


if __name__ == '__main__':
    unittest.main()
