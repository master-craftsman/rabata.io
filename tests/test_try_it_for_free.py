import pytest
from pages.main_page import Main
from Locators.main_page import MainPage




@pytest.mark.smoke
class TestTryItForFree:
    def test_try_it_for_free_top(self, browser):
        m = Main(browser)
        m.try_it_for_free(MainPage.TryItForFreeTop_BTN)

    def test_try_it_for_free_bottom(self, browser):
        m = Main(browser)
        m.try_it_for_free(MainPage.TryItForFreeBottom_BTN)