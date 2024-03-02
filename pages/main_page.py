from pages.base import Base
from data.constants import Constants
from Locators.main_page import MainPage
from data.assertions import Assertions
from playwright.sync_api import Page
from Locators.singup_page import SingUpPage
import re

class Main(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def return_to_sing_up(self):
        self.open("")
        self.click(MainPage.SingUp_BTN)
        self.assertion.check_URL("signup", "Wrong URL")

    def try_it_for_free(self, bnt):
        self.open("")
        self.click(bnt)
        self.assertion.check_URL("signup", "Wrong URL")

    def return_to_calculator(self):
        self.open("#calculator")
        self.assertion.check_URL("#calculator", "Wrong URL")

    def set_value_in_calculator(self, slider, set_value, showed_value):
        self.manipulate_slider(slider, set_value)
        self.assertion.have_text(showed_value, str(set_value*100 + 100), 'Set value != showed')


    def check_calculation(self, showed_value):
        showed_value = {
            'Rabata Cloud Storage': '//p[@id="rabataMobileApi"]',
            'Microsoft Azure': '//p[@id="azureMobileApi"]',
            'Amazon S3': '//p[@id="amazonMobileApi"]',
            'Google Cloud': '//p[@id="googleMobileApi"]',
        }
        dataStoredInput = 100  # Замените на фактическое значение

        k = {
            'rabataStored': 59,
            'azureStored': 208,
            'amazonStored': 260,
            'googleStored': 230,
        }

        # Вычисляем calculatedStored для каждого ключа в словаре k
        for key, value in k.items():
            calculatedStored = (int(dataStoredInput / 10 - 0.01) + 1) * value * 12
            # Получаем отображаемое значение для текущего ключа
            showed_value_text = self.page.text_content(showed_value[key])
            # Используем регулярное выражение для извлечения числового значения из текста
            showed_value_for_key = int(re.search(r'\d+', showed_value_text).group())

            # Сравниваем вычисленное значение с отображаемым

            self.assertion.have_text(calculatedStored, showed_value_for_key, f"Wrong value for {key}")

    def open_privacy_policy(self, link):
        self.open("")
        self.click(link)
        self.assertion.have_text(SingUpPage.PrivacyPolicy_TITLE,"Privacy Policy", "This is not Privacy Policy")

