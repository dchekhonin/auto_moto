__author__ = 'dchekhonin'


import unittest
from selenium  import webdriver
from test_mail_classes.mail_login import Login
import test_mail_classes.mail_input
from test_mail_classes.mail_search_by_subject import SearchMail
from selenium.webdriver.common.by import By



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(test_mail_classes.mail_input.main_email_site)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()

    def test_DM_Login(self):
        home = Login(self.driver)
        result = home.login(test_mail_classes.mail_input.email,test_mail_classes.mail_input.password)
        assert test_mail_classes.mail_input.assert_item in result.to_be_sure_link()

        SearchMail(self.driver).search_new_mail(self.driver)
        count = SearchMail.search_new_mail(self.driver)
        assert count, 'We have no mails with subject "%s"' % test_mail_classes.mail_input.mail_subject
        print 'We have %s mails with subject "%s"' % (count,test_mail_classes.mail_input.mail_subject)

if __name__ == '__main__':
   unittest.main()
