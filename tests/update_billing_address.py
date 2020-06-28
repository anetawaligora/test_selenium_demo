from pages.billing_address_page import BillingAddressPage
from pages.my_account_page import MyAccountPage
import random
import pytest


@pytest.mark.usefixtures("setup")
class TestUpdateBillingAddress:
    def test_update_billing_address(self):
        email = str(random.randint(0, 1000)) + "testeroprogramowaniapython@gmail.com"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "testeroprogramowaniapython")
        billing_addresses_page = BillingAddressPage(self.driver)
        billing_addresses_page.open_edit_billing_address()
        billing_addresses_page.set_personal_data("Aneta", "Wa")
        billing_addresses_page.select_country("Poland")
        billing_addresses_page.set_address("Kwiatowa 1", "01-001", "Warsaw")
        billing_addresses_page.set_phone_number("61111111")
        billing_addresses_page.save_address()

        assert 'Address changed successfully.' in billing_addresses_page.get_message_text()
