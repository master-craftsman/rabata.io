import pytest
from pages.main_page import Main
from Locators.main_page import MainPage




@pytest.mark.smoke
class TestCalculator:
    def test_return_to_calculator(self, browser):
        p = Main(browser)
        p.return_to_calculator()
        p.set_value_in_calculator(MainPage.TotaDataStored_SLIDER, 4, MainPage.TotaDataStored_VALUE)
        p.set_value_in_calculator(MainPage.MonthlyDonwloadedData_SLIDER, 1, MainPage.MonthlyDonwloadedData_VALUE)
