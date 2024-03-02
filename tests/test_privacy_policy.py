import pytest
from pages.registration_page import Registration
from Locators.singup_page import SingUpPage
from Locators.main_page import MainPage
from pages.main_page import Main





@pytest.mark.smoke
class TestPrivacyPolicy:
    def test_privacy_policy_top(self, browser):
        m = Registration(browser)
        m.user_registration()
        m.open_privacy_policy(SingUpPage.PrivacyPolicy_LINK)

    def test_privacy_policy_bottom(self, browser):
        m = Main(browser)
        m.open_privacy_policy(MainPage.PrivacyPolicy_LINK)



