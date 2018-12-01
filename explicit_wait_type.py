from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWaitType():

    def __init__(self, driver):
        self.driver = driver

    def wait_for_url_contain(self, text,
                         timeout=10, poll_frequency=0.5):
        is_contain = None
        try:
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for url contains", text)
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[
                                     NoSuchElementException,
                                     ElementNotVisibleException,
                                     ElementNotSelectableException
                                 ])
            is_contain = wait.until(EC.url_contains(text))
            print("url contains", text)
            return is_contain
        except:
            print("url doesn't contain", text)
            print_stack()

