import article_page
import home_page
from common_page import wait_for_visibility_of_element
import common_page
import unittest
from selenium import webdriver

class Tests(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444',
            options=options)
        self.driver.maximize_window()
        self.driver.get('https://news.ladbrokes.com/')

    def tearDown(self):
        self.driver.quit()

    def test_top_nav_bar_is_displayed(self):
        self.assertTrue(common_page.check_top_nav_bar(self.driver))


    def test_article_opens_correctly(self):
        home_article_title_text = home_page.get_first_article_title_text(self.driver)
        home_page.click_first_read_more_button(self.driver)
        child_article_title_text = article_page.get_article_title_text(self.driver)

        self.assertEqual(home_article_title_text,child_article_title_text)
        self.assertTrue(article_page.check_article_picture_is_displayed(self.driver))

    def test_search_functionality_displays_results(self):
        common_page.search_functionality_displays_results(self.driver,'Search')
        home_search_title_text = common_page.search_functionality_displays_correct_title_home(self.driver)
        child_search_title_text = common_page.search_functionality_displays_correct_title_child(self.driver)

        self.assertEqual(home_search_title_text,child_search_title_text)

    def test_search_functionality_displays_articles(self):
        common_page.search_functionality_displays_results(self.driver,'Search')
        self.assertTrue(common_page.search_functionality_displays_articles(self.driver))

# test sprawdzający kafelek z artykułem na drugiej stronie po frazie 'Search' w search engine

    def test_search_functionality_displays_articles_page(self):
        common_page.search_functionality_displays_results(self.driver,'Search')
        self.assertTrue(common_page.search_functionality_displays_articles(self.driver))
        common_page.search_functionality_displays_articles_pages(self.driver)
        self.assertTrue(common_page.search_functionality_displays_articles_page02)

# test sprawdzający czy wyświetlają się ikonki social-media na stronie głownej

    def test_social_media_footer_display(self):
            self.assertTrue(common_page.social_media_footer_display(self.driver))


# test sprawdzający czy artykuły sa posortowane wg najnowszego do najstarszego

    def test_search_functionality_displays_results_dates_validation(self):
        common_page.search_functionality_displays_results(self.driver,'football')
        self.assertTrue(common_page.search_functionality_displays_articles(self.driver))
        common_page.check_article_dates(self.driver)


if __name__== "__main__":
    unittest.main()
