__author__ = 'dchekhonin'

import my_locators

class ResultPage(object):
    def __init__(self,driver):
        self.driver = driver

    def to_be_sure_link(self):
        return self.driver.find_element_by_id(my_locators.to_be_sure_id).text
