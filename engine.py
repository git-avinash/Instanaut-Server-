"""
xenon_a => Engine dedicated towards mass liking and commenting on posts for both Hashtag and Location.
xenon_b => Engine dedicated towards Viewing Mass Stories for both Hashtag and Location.
"""

import random
import time

from interact import wait_for, quick_sleep, long_sleep, gen_number_big, gen_number_small, get_xpath, print_log_error, print_log
from database_manager import sessions


def xenon_a(self, key, lk_status_hashtag, hashtag, lk_status_comment, comment_content, lk_status_location, url):
    if lk_status_location:
        self.driver.get(url)
    if lk_status_hashtag:
        self.driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
    wait_for(self.driver, get_xpath("INTERACT", "HashTag_FirstPost"))
    self.driver.find_element_by_xpath(
        get_xpath("INTERACT", "HashTag_FirstPost")).click()

    while True:
        db = sessions()
        if db.session_data_by_key(key)[0][2] == 0:
            break
        print_log("Generating new mini session", "INFO")
        mini_session = gen_number_big()
        print_log(f"Mini session to last {mini_session} cycles", "INFO")

        for _ in range(mini_session):
            db = sessions()
            if db.session_data_by_key(key)[0][2] == 0:
                break
            message = comment_content[random.randrange(
                0, len(comment_content))]

            try:
                quick_sleep()
                wait_for(self.driver, get_xpath("POST_HASHTAG", "LikeButton"))
                self.driver.find_element_by_xpath(
                    get_xpath("POST_HASHTAG", "LikeButton")).click()
                quick_sleep()
                if lk_status_comment:
                    try:
                        chance = random.randrange(0, 10)

                        if chance == 1:
                            self.driver.find_element_by_xpath(
                                get_xpath("POST_HASHTAG", "CommentBox")).click()
                            quick_sleep()
                            self.driver.find_element_by_xpath(
                                get_xpath("POST_HASHTAG", "CommentBox")).send_keys(message.strip("'"))
                            quick_sleep()
                            self.driver.find_element_by_xpath(
                                (get_xpath("POST_HASHTAG", "PostButton"))).click()
                            quick_sleep()
                    except Exception as e:
                        print_log_error(e, "ERROR")
            except Exception as e:
                print_log_error(e, "ERROR")
            finally:
                try:
                    self.driver.find_element_by_xpath(get_xpath("POST_HASHTAG", "NextButton")).click() or \
                        self.driver.find_element_by_xpath(
                            get_xpath("POST_HASHTAG", "NextButton2")).click()
                    quick_sleep()
                except Exception as e:
                    print_log_error(e, "ERROR")
        db = sessions()
        if db.session_data_by_key(key)[0][2] == 1:
            long_sleep()


def xenon_b(self, key, st_status_hashtag, hashtag, st_status_location, url):
    while True:
        db = sessions()
        if db.session_data_by_key(key)[0][2] == 0:
            break
        print_log("Generating new mini session", "INFO")
        mini_session = gen_number_small()
        print_log(f"Mini session to last {mini_session} cycles", "INFO")
        for _ in range(mini_session):
            db = sessions()
            if db.session_data_by_key(key)[0][2] == 0:
                break
            if st_status_location:
                self.driver.get(url)
            if st_status_hashtag:
                self.driver.get(
                    f"https://www.instagram.com/explore/tags/{hashtag}/")
            wait_for(self.driver, get_xpath("INTERACT", "Enter_Story"))
            self.driver.find_element_by_xpath(
                get_xpath("INTERACT", "Enter_Story")).click()
            time.sleep(random.randrange(180, 200))
        db = sessions()
        if db.session_data_by_key(key)[0][2] == 1:
            long_sleep()
