from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import random
import string
import colorama
import termcolor2

from database_manager import key_logger
from xpath_compile import xpath


def get_xpath(function_name, xpath_name):
    return xpath[function_name][xpath_name]


def wait_for(instance, xpath):
    delay = 30
    try:
        WebDriverWait(instance, delay).until(
            ec.presence_of_element_located((By.XPATH, xpath)))
    except TimeoutException as e:
        print_log_error(e, "ERROR")


def login_helper(self, username, password):
    try:
        self.driver.get("https://www.instagram.com/accounts/login/")
        quick_sleep()
        wait_for(self.driver, get_xpath("SIGNUP", "Username_field"))
        self.driver.find_element_by_xpath(
            get_xpath("SIGNUP", "Username_field")).send_keys(username)
        quick_sleep()
        self.driver.find_element_by_xpath(
            get_xpath("SIGNUP", "Password_field")).send_keys(password)
        self.driver.find_element_by_xpath(
            get_xpath("SIGNUP", "Submit_button")).click()
        try:
            wait_for(self.driver, get_xpath("INTERACT", "Pop_up"))
            quick_sleep()
            self.driver.find_element_by_xpath(
                get_xpath("INTERACT", "Pop_up")).click()
            quick_sleep()
        except Exception as e:
            print_log_error(e, "ERROR")
    except Exception as e:
        print_log_error(e, "ERROR")


def get_list_from_string(list_string):
    list_srt = list_string
    final_list = list_srt.strip('][').split(', ')
    return final_list


def gen_key():
    length = 7
    oldkey = True
    db = key_logger()
    unavailable_keys = db.all_keys()
    while oldkey:
        key = "".join(random.choice(
            string.ascii_uppercase + string.digits) for _ in range(length))

        for i in unavailable_keys:
            if i == key:
                break
        oldkey = False

    return key


def convert_tf(bool_arg):
    if bool_arg == True:
        return 1
    if bool_arg == False:
        return 0
    if bool_arg == 1:
        return True
    if bool_arg == 0:
        return False


def print_log_error(log, summary):
    colorama.init()
    print(termcolor2.colored(f"[{summary}] {log}", "red"))


def print_log(log, summary):
    colorama.init()
    print(termcolor2.colored(f"[{summary}] {log}", "green"))


def quick_sleep():
    time.sleep(random.randrange(2, 10))


def long_sleep():
    sleep_time = random.randrange(60, 120)
    print_log(f"Sleeping for {sleep_time} minutes", "INFO")
    time.sleep(sleep_time)


def gen_number_big():
    return random.randrange(40, 200)


def gen_number_small():
    return random.randrange(15, 25)
