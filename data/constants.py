import os
import random
import string

class Constants:
    def generate_email(length=10, domain="example.com"):
        """
        Генерирует случайный адрес электронной почты.

        :param length: Длина части имени пользователя (по умолчанию 10 символов).
        :param domain: Домен электронной почты (по умолчанию "example.com").
        :return: Сгенерированный адрес электронной почты.
        """
        # Генерация части имени пользователя
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

        # Создание адреса электронной почты
        email = f"{username}@{domain}"

        return email

    try:
        login = os.getenv('AUTH_LOGIN')
        password = os.getenv('AUTH_PASSWORD')
        NAME = os.getenv('NewUserName')
        EMAIL = os.getenv('NewEmail')
        NEW_PASS = os.getenv('NewPass')
    except KeyError:
        print("LOGIN OR PW WASN'T FOUND")

    PrivacyPolicyTop_TEXT = 'This Privacy Policy (the “Policy”) describes how the Rabata Technologies LLC (US) & Rabata Technologies LP (EU) (for more details, see “Contact Information” below) (“Rabata,” “we,” “our” or “us”) collect, use, and share information in connection with your use of our websites (the “Sites”), as well as any products, services, and/or applications available on or through the Sites (collectively, the “Services”). However, this Policy does not apply to information customers or users (“users”, “you,” or “your”) may process when using our Services.'
    PrivacyPolicyMiddle_TEXT = 'The information we collect includes “personal data,” which is any information about an identifiable individual, as further set forth in this Policy. Rabata is the sole owner of the information collected on the Sites or through your use of the Services. We will not sell, share, or rent this information to others in ways different from what is disclosed in this Policy.'
    PrivacyPolicyBottom_TEXT = 'Further, Rabata respects your privacy and is committed to protecting your personal data in line with the General Data Protection Regulation – Regulation (EU) 2016/679 (“GDPR”). This Policy will inform you as to how we will look after your personal data when you interact with us, including visiting our Sites. It also tells you about your rights in relation to your personal data. We recommend that you read this Policy in full to ensure you are fully informed regarding our privacy practices. If you have any questions about this Policy or Rabata’s data collection, use, and disclosure practices, please contact us at support@rabata.io.'