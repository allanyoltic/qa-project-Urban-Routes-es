from selenium import webdriver
from data import urban_routes_url, address_from, address_to, phone_number, card_number, card_code, message_for_driver
from sms_code_fetcher import get_sms_code
from methods import TaxiMethods

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(urban_routes_url)
        cls.driver.maximize_window()
        cls.methods = TaxiMethods(cls.driver)

    def test_1_enter_addresses(self):
        self.methods.enter_addresses(address_from, address_to)

    def test_2_select_comfort_tariff(self):
        self.methods.select_comfort_tariff()

    def test_3_enter_phone_number(self):
        self.methods.enter_phone_number(phone_number)

    def test_4_enter_sms_code(self):
        code = get_sms_code(phone_number)
        if code:
            self.methods.enter_sms_code(code)
        else:
            print("[ERROR] No se obtuvo un código válido. Abortando ejecución.")
            self.driver.quit()
            assert False

    def test_5_add_credit_card(self):
        self.methods.add_credit_card(card_number, card_code)

    def test_6_write_driver_message(self):
        self.methods.write_driver_message(message_for_driver)

    def test_7_toggle_blanket_and_tissues(self):
        self.methods.toggle_blanket_and_tissues()

    def test_8_add_ice_cream(self):
        self.methods.add_ice_cream()

    def test_9_confirm_trip_and_check_driver(self):
        self.methods.confirm_trip()
        assert self.methods.wait_for_driver_photo(timeout=40)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()