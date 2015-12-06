__author__ = 'dchekhonin'

from Page_factory.pf_classes import LoggerMixin


class Sent_mail_page(LoggerMixin):


    def __init__(self,driver):
        super(Sent_mail_page, self).__init__()
        self._driver = driver

    def sent_to_be_sure_link(self):
        return self._driver.current_url
