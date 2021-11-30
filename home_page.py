import support_funcs


# Xpathsgit in
first_read_more_button_xpath = "(//div[@class='news-btn'])[1]"
first_article_title_xpath = "(//div[@class= 'news-title'])[1]"


# Actions
def click_first_read_more_button(driver_instance):
    elem = support_funcs.wait_for_visibility_of_element(driver_instance, first_read_more_button_xpath)
    elem.click()

def get_first_article_title_text(driver_instance):
    elem = support_funcs.wait_for_visibility_of_element(driver_instance, first_article_title_xpath)
    return elem.text
