from datetime import datetime

class Sent_mail_page(object):


    def __init__(self,driver):
        self._driver = driver

    def sent_to_be_sure_link(self):
        try:
            return self._driver.current_url
        except Exception as e:
            print e
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self._driver.get_screenshot_as_file('screenshot-%s in Sent_mail_sent_tbs_link.png' % now)
