import unittest
from selenium  import webdriver
from pf_classes.pf_login import LoginPage
import pf_classes.pf_input


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._driver = webdriver.Chrome()
        self._driver.get(pf_classes.pf_input.main_email_site)
        self._driver.implicitly_wait(10)

    def tearDown(self):
        self._driver.close()

    #checking login with asserting home page and 'sent' page links.
    def test_mail_Login(self):
        home = LoginPage(self._driver)
        result = home.login(pf_classes.pf_input.email,pf_classes.pf_input.password)
        assert pf_classes.pf_input.assert_homepage_item in result.to_be_sure_link()

        assert pf_classes.pf_input.assert_sentmailpage_item in result.sent_mail_page().sent_to_be_sure_link()

    #checking correct error message during login with empty email
    def test_login_func_empty_mail(self):
        page = LoginPage(self._driver)
        result = page.login_error_mail(pf_classes.pf_input.empty_email)
        assert pf_classes.pf_input.assert_empty_email_error in result

    #checking correct error message during login with incorrect email
    def test_login_func_incorrect_mail(self):
        page = LoginPage(self._driver)
        result = page.login_error_mail(pf_classes.pf_input.incorrect_email)
        assert pf_classes.pf_input.assert_incorrect_email_error in result

    #checking correct error message during login with empty password
    def test_login_func_empty_password(self):
        page = LoginPage(self._driver)
        result = page.login_error_password(pf_classes.pf_input.email,pf_classes.pf_input.empty_password)
        print result
        assert pf_classes.pf_input.assert_empty_password_error in result

    #checking correct error message during login with incorrect password
    def test_login_func_incorrect_password(self):
        page = LoginPage(self._driver)
        result = page.login_error_password(pf_classes.pf_input.email,pf_classes.pf_input.incorrect_password)
        assert pf_classes.pf_input.assert_incorrect_password_error in result

    #checking menu 'Inbox' is active by default.
    def test_default_active_menu(self):
        home = LoginPage(self._driver)
        result = home.login(pf_classes.pf_input.email,pf_classes.pf_input.password)
        assert int(result.default_active_menu_check()) == 0

    #checking menu 'Sent' becomes active after click and menu 'Inbox' becomes inactive.
    def test_menu_active_indication(self):
        home = LoginPage(self._driver)
        result = home.login(pf_classes.pf_input.email,pf_classes.pf_input.password)
        assert int(result.active_menu_indication_check()) == 0
        assert int(result.default_active_menu_check()) == -1




if __name__ == '__main__':
    unittest.main()
