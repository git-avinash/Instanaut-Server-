xpath = {}

xpath["SIGNUP"] = {
    "Username_field": "//input[@name='username']",
    "Password_field": "//input[@name='password']",
    "Submit_button": "//button[@type='submit']",
}

xpath["INTERACT"] = {
    "HashTag_FirstPost": "//body/div/section/main/article/div[2]/div/div/div/a/div/div[2]",
    "Enter_Story": "//*[@aria-label='Open Stories']",
    "Pop_up": "//button[contains(text(), 'Not Now')]",
}

xpath["POST_HASHTAG"] = {
    "UserName": "//div/article/header/div/div/div/a",
    "LikeButton": "//section/span/button[*[local-name()='svg']/@aria-label='Like']",
    "UnLikeButton": "//section/span/button[*[local-name()='svg']/@aria-label='Unlike']",
    # "CommentButton": "//button[*[local-name()='svg']/@aria-label='Comment']",
    "CommentBox": "//textarea[@placeholder='Add a comment…']",
    "PostButton": "//button[@type='submit']",
    "PostLikesAmount": "//div/article/div/section//following-sibling::section/div/div/button/span",
    "NextButton": "//*[contains(text(),'Next')]",
    "NextButton2": "//body/div[4]//*[text()='Next']",
    "PreviousButton": "//*[contains(text(),'Previous')]",
}

xpath["STORY"] = {
    "Story_Info": "//body//header/div/div/div[2]/a",
}
