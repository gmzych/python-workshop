import support_funcs


# Xpaths
article_title_xpath = "//div[@class='post-body']//h1[@class='post-title']"
article_picture_xpath = "//article/img"


# Actions
def get_article_title_text(driver_instance):
    elem = support_funcs.wait_for_visibility_of_element(driver_instance, article_title_xpath)
    return elem.text

def check_article_picture_is_displayed(driver_instance):
    elem = support_funcs.wait_for_visibility_of_element(driver_instance, article_picture_xpath)
    return elem.is_displayed()