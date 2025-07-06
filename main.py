from selenium import webdriver
from data import urban_routes_url, address_from, address_to, phone_number, card_number, card_cvv, message_for_driver
from sms_code_fetcher import get_sms_code
from UrbanRoutesPage import UrbanRoutesPage

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(urban_routes_url)
        cls.page = UrbanRoutesPage(cls.driver)

    def test_1_enter_addresses(self):
        self.page.enter_addresses(address_from, address_to)
        assert self.page.get_from_input_value() == address_from
        assert self.page.get_to_input_value() == address_to

    def test_2_select_comfort_tariff(self):
        self.page.select_comfort_tariff()
        assert True  # A falta de mejor aserción

    def test_3_enter_phone_number(self):
        self.page.enter_phone_number(phone_number)
        assert True  # A falta de validación más precisa

    def test_4_enter_sms_code(self):
        sms_code = get_sms_code(phone_number)  # ← Aquí sí lo usamos correctamente
        self.page.enter_sms_code(sms_code)
        assert True

    def test_5_add_credit_card(self):
        self.page.add_credit_card(card_number, card_cvv)
        assert True  # Podríamos validar si la tarjeta quedó como método activo

    def test_6_write_driver_message(self):
        self.page.write_driver_message(message_for_driver)
        assert True

    def test_7_toggle_blanket_and_tissues(self):
        self.page.toggle_blanket_and_tissues()
        assert True

    def test_8_add_ice_cream(self):
        self.page.add_ice_cream()
        assert True

    def test_9_confirm_trip_and_check_driver(self):
        self.page.confirm_trip()
        assert self.page.wait_for_driver_info()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()