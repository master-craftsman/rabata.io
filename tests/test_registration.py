import pytest
from pages.registration_page import Registration
from pages.main_page import Main




@pytest.mark.smoke
class TestRegistration:
    def test_return_to_registration_page(self, browser):
        p = Main(browser)
        p.return_to_sing_up()

    def test_user_registration(self, browser):
        m = Registration(browser)
        m.user_registration()
        m.input_registration_field()