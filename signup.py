from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from interact import wait_for
from interact import quick_sleep, get_xpath, print_log_error


class SignUp:
    def __init__(self, user_name, passw):
        self.username = user_name
        self.password = passw
        self.options = Options()
        self.driver = webdriver.Chrome(
            "./WebDriver/chromedriver.exe", options=self.options)
        self.driver.get("https://www.instagram.com/accounts/login/")

    def signup(self):
        try:
            quick_sleep()
            wait_for(self.driver, get_xpath("SIGNUP", "Username_field"))
            self.driver.find_element_by_xpath(
                get_xpath("SIGNUP", "Username_field")).send_keys(self.username)
            quick_sleep()
            self.driver.find_element_by_xpath(
                get_xpath("SIGNUP", "Password_field")).send_keys(self.password)
            self.driver.find_element_by_xpath(
                get_xpath("SIGNUP", "Submit_button")).click()
            wait_for(self.driver, get_xpath("INTERACT", "Pop_up"))
            quick_sleep()
            self.driver.find_element_by_xpath(
                get_xpath("INTERACT", "Pop_up")).click()
            quick_sleep()
            return 'accountCreated'
        except Exception as e:
            print_log_error(e, "ERROR")
            return 'failedToCreateAccount'
        finally:
            self.driver.close()
            self.driver.quit()
            self.driver.service.stop()
