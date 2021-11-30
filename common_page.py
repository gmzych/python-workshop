# klasa dla funkcji/elementow które wystepuja na wiekszosci stron
from selenium.webdriver import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import support_funcs
from support_funcs import wait_for_visibility_of_element
#Xpaths
top_nav_bar_xpath = "//nav[@class='nav']"
search_btn = "//form/input[@class='search-input']"
search_result = "//div[@class='main-wrapper']/section/h1"
search_input = "//input[@class='search-input']"
first_article_search_result = "//main/div/section/article"
pagination_element_page02 = "//div[@class='pagination']/a[1]"
page_result_page02 = "//section/article[@id='post-209652']"
social_media_footer = "//div[@class='soc-med-wrapper']"
date_value_in_search_query = "//span[@class='cat-item-date']"
#Actions

# wehdz na główna strone, i znajdz nav bar
def check_top_nav_bar(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance,top_nav_bar_xpath)
    return elem.is_displayed()

# wejdz na głowna strone i wpisz fraze search, nacisnij enter

def search_functionality_displays_results(driver_instance,search_value):
    elem = wait_for_visibility_of_element(driver_instance,search_btn)
    elem.send_keys(search_value)
    elem.send_keys(Keys.ENTER)
    return elem

def search_functionality_displays_correct_title_home(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance,search_input)
    return elem.is_displayed()

#  sprawdz czy wynik po searchu został wyświetlony
def search_functionality_displays_correct_title_child(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance,search_result)
    return elem.is_displayed()



# Po searchu 1 kafelek z artykułem sie wyświetla

def search_functionality_displays_articles_page(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance,first_article_search_result)
    return elem.is_displayed()

# Po searchu przy frazie 'Search' zeskroluj na dół strony i kliknij na 2 strone, sprawdz czy została wyświetlona

def search_functionality_displays_articles_pages(drive_instance):
    elem = wait_for_visibility_of_element(drive_instance,pagination_element_page02)
    elem.click()
    return elem

def search_functionality_displays_articles(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance,first_article_search_result)
    return elem.is_displayed()


def search_functionality_displays_articles_page02(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance,page_result_page02)
    return elem.is_displayed()

def social_media_footer_display(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance,social_media_footer)
    return elem.is_displayed()

def check_article_dates(driver_instance):

    elems_list = support_funcs.wait_for_visibility_of_elements(driver_instance,date_value_in_search_query)
    for i in elems_list:
        return i.text

    #zebrac daty do listy
    # zrobić kopie listy i posortować ta liste wg daty
    # porownac te dwie listy z datami do siebie



#stworzyc liste z elementow xpath - ( wszystkie daty z artykułu )
#uzyc waitforvisibilityofelements
#sciagnac text z tej listy i wyciagnac text z tych elementow
#





