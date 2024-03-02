class MainPage:
    SingUp_BTN = "//a[@href='signup' and text()='Sign Up']"
    TryItForFreeTop_BTN = '//div[@class="arrow-wrap"]//a[@href="signup" and @class="btn flex flex-center justify-center"]'
    TryItForFreeBottom_BTN = '//a[text()="Try it For Free"]'
    PrivacyPolicy_LINK = '//a[@onclick="modalPrivacy.show()"]'
    TotaDataStored_SLIDER = '//input[@id="dataApiStoredInput"]'
    TotaDataStored_VALUE = '//span[@id="tbApiStored"]'
    MonthlyDonwloadedData_SLIDER = '//input[@id="dataDownloadInput"]'
    MonthlyDonwloadedData_VALUE = '//span[@id="tbDownload"]'
    ShowedCalculadetData = {
        'Rabata Cloud Storage': '//p[@id="rabataMobileApi"]',
        'Microsoft Azure': '//p[@id="azureMobileApi"]',
        'Amazon S3': '//p[@id="amazonMobileApi"]',
        'Google Cloud': '//p[@id="googleMobileApi"]',
    }

