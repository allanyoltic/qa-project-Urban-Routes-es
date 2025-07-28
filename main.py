from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import data
from data import urban_routes_url, address_from, address_to, phone_number, card_number, card_cvv, message_for_driver
from UrbanRoutesPage import UrbanRoutesPage


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get(urban_routes_url)
        cls.page = UrbanRoutesPage(cls.driver)

    def test_1_enter_addresses(self):
        self.page.enter_addresses(address_from, address_to)
        assert self.page.get_from_input_value() == address_from, "La dirección de origen no coincide"
        assert self.page.get_to_input_value() == address_to, "La dirección de destino no coincide"

    def test_2_select_comfort_tariff(self):
        #self.test_1_enter_addresses()
        self.page.select_comfort_tariff()
        assert self.page.is_comfort_tariff_selected(), "La tarifa Comfort no fue seleccionada correctamente"

    def test_3_enter_phone_number(self):
        #self.test_2_select_comfort_tariff()
        self.page.enter_phone_number()
        actual_number = data.phone_number
        phone_number_written = self.page.is_phone_input_filled_correctly()
        assert phone_number_written == actual_number
        WebDriverWait(self.driver, timeout=5)

    def test_4_add_credit_card(self):
        #self.test_2_select_comfort_tariff()
        self.page.add_credit_card(card_number, card_cvv)
        assert self.page.is_card_linked(), "La tarjeta no fue vinculada correctamente"

    def test_5_write_driver_message(self):
        #self.test_4_add_credit_card()
        self.page.write_driver_message(message_for_driver)
        assert self.page.is_message_sent(message_for_driver), "El mensaje no se ingresó correctamente"

    def test_6_toggle_blanket_and_tissues(self):
        #self.test_3_enter_phone_number()
        self.page.toggle_blanket_and_tissues()
        assert self.page.is_blanket_and_tissues_selected(), "La opción de manta y pañuelos no fue activada"

    def test_7_add_ice_cream(self):
        self.page.add_ice_cream()
        assert self.page.is_ice_cream_added(), "No se agregaron 2 helados"

    def test_8_taxi_seeker_appears(self):
        #self.test_7_add_ice_cream()
        self.page.confirm_trip()
        assert self.page.is_taxi_modal(), "No apareció el modal para buscar un taxi"

    def test_9_confirm_trip_and_check_driver(self):
        assert self.page.wait_for_driver_info(), "La información del conductor no apareció"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()