__author__ = 'dchekhonin'

from result_login_page import ResultPage
import my_locators

class Login(object):


    def __init__(self,driver):
        self.driver = driver

    def login(self,email,password):
        self.driver.find_element_by_id(my_locators.email_id).send_keys(email)
        self.driver.find_element_by_id(my_locators.email_confirm_next_id).click()
        self.driver.find_element_by_id(my_locators.email_password_id).send_keys(password)
        self.driver.find_element_by_id(my_locators.email_signin_id).click()
        self.driver.implicitly_wait(5)
        return ResultPage(self.driver)
