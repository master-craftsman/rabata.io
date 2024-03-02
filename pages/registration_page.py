from pages.base import Base
from data.constants import Constants
from Locators.main_page import MainPage
from Locators.singup_page import SingUpPage
from data.assertions import Assertions
from playwright.sync_api import Page

class Registration(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def user_registration(self):
        self.open("signup")
        # self.click(MainPage.SingUp_BTN)
        self.assertion.check_URL("signup", "Wrong URL")

    def input_registration_field(self):
        self.input(SingUpPage.FullName_INPUT, Constants.NAME)
        self.input(SingUpPage.Email_INPUT, Constants.generate_email())
        self.input(SingUpPage.Password_INPUT, Constants.NEW_PASS)
        self.input(SingUpPage.PasswordRepeate_INPUT, Constants.NEW_PASS)
        self.click(SingUpPage.Agree_CHECKBOX)
        self.click(SingUpPage.SingUp_BTN)
        # self.assertion.check_URL("signup", "Wrong URL")
        self.assertion.have_text(SingUpPage.VefityEmail_Label, "Verify your email", "This is not Verify Page")

    def open_privacy_policy(self, link):
        self.click(link)
        self.assertion.have_text(SingUpPage.PrivacyPolicy_TITLE,"Privacy Policy", "This is not Privacy Policy")
        # self.assertion.have_text(SingUpPage.PrivacyPolicyTop_TEXT, Constants.PrivacyPolicyTop_TEXT, "Wrong first part of Privacy Policy")
        # self.assertion.have_text(SingUpPage.PrivacyPolicyMiddle_TEXT, Constants.PrivacyPolicyMiddle_TEXT, "Wrong middle part of Privacy Policy")
        # self.assertion.have_text(SingUpPage.PrivacyPolicyBottom_TEXT, Constants.PrivacyPolicyBottom_TEXT, "Wrong bottom part of Privacy Policy")


