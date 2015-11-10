__author__ = 'dchekhonin'

from selenium  import webdriver
import mail_input
import my_locators

class SearchMail(object):

    def __init__(self,driver):
        self.driver = driver

    @staticmethod
    def search_new_mail(driver):

        all_mails = (driver.find_elements_by_xpath(my_locators.list_of_all_mails))
        count = 0
        for each in all_mails:

          result = unicode(each.text)
          if mail_input.mail_subject in result:
              count += 1

        return count
