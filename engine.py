"""
xenon_a => Engine dedicated towards mass liking and commenting on posts for both Hashtag and Location.
xenon_b => Engine dedicated towards Viewing Mass Stories for both Hashtag and Location.
"""

import random
import time

from interact import wait_for, quick_sleep, long_sleep, gen_number_big, gen_number_small, get_xpath
from trigger_engine_activity import TriggerEngineActivity


def xenon_a(self, lk_status_hashtag, hashtag, lk_status_comment, comment_content, lk_status_location, url):
    if lk_status_location:
        self.driver.get(url)
    if lk_status_hashtag:
        self.driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
    wait_for(self.driver, get_xpath("INTERACT", "HashTag_FirstPost"))
    self.driver.find_element_by_xpath(
        get_xpath("INTERACT", "HashTag_FirstPost")).click()

    while TriggerEngineActivity().running_status:
        for _ in range(gen_number_big()):
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
                        print(e)
            except Exception as e:
                print(e)
            finally:
                try:
                    self.driver.find_element_by_xpath(get_xpath("POST_HASHTAG", "NextButton")).click() or \
                        self.driver.find_element_by_xpath(
                            get_xpath("POST_HASHTAG", "NextButton2")).click()
                    quick_sleep()
                except Exception as e:
                    print(e)
        long_sleep()


def xenon_b(self, st_status_hashtag, hashtag, st_status_location, url):
    while TriggerEngineActivity().running_status:
        for _ in range(gen_number_small()):
            if st_status_location:
                self.driver.get(url)
            if st_status_hashtag:
                self.driver.get(
                    f"https://www.instagram.com/explore/tags/{hashtag}/")
            wait_for(self.driver, get_xpath("INTERACT", "Enter_Story"))
            self.driver.find_element_by_xpath(
                get_xpath("INTERACT", "Enter_Story")).click()
            time.sleep(random.randrange(180, 200))
        long_sleep()
