"""
Author: Avinash Sah
GitHub: https://github.com/git-avinash
Instagram: https://www.instagram.com/_avi.exe/
App Version: 1.0.0+1
"""
from Instanaut import Instanaut


class app:
    def __init__(self,
                 username,
                 password,
                 lk_status_hashtag,
                 hashtag,
                 lk_status_comment,
                 comments,
                 lk_status_location,
                 url,
                 st_status_hashtag,
                 st_status_location,
                 ):

        self.user_session = Instanaut(username, password)
        self.user_session.session(lk_status_hashtag,
                                  hashtag,
                                  lk_status_comment,
                                  comments,
                                  lk_status_location,
                                  url,
                                  st_status_hashtag,
                                  st_status_location,
                                  )
