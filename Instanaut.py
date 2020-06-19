from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from interact import login_helper
from engine import xenon_a, xenon_b


class Instanaut:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.options = Options()
        self.options.add_argument("--mute-audio")
        self.driver = webdriver.Chrome(
            "./WebDriver/chromedriver.exe", options=self.options)
        print(f"[SESSION ID] {self.driver.session_id}")
        # self.driver.set_window_size(1200, 1200)

    def session(self,
                lk_status_hashtag,
                hashtag,
                lk_status_comment,
                comments,
                lk_status_location,
                url,
                st_status_hashtag,
                st_status_location,
                ):

        if lk_status_hashtag or lk_status_location or st_status_hashtag or st_status_location:
            login_helper(self, self.username, self.password)

        if lk_status_hashtag or lk_status_location:
            xenon_a(
                self,
                lk_status_hashtag,
                hashtag,
                lk_status_comment,
                comments,
                lk_status_location,
                url,
            )

        if st_status_hashtag or st_status_location:
            xenon_b(
                self,
                st_status_hashtag,
                hashtag,
                st_status_location,
                url,
            )

        self.driver.close()
        self.driver.quit()
        self.driver.service.stop()
