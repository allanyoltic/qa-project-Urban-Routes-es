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
        assert self.page.get_from_input_value() == address_from, "La dirección de origen no coincide"
        assert self.page.get_to_input_value() == address_to, "La dirección de destino no coincide"

    def test_2_select_comfort_tariff(self):
        self.page.select_comfort_tariff()
        assert self.page.is_comfort_tariff_selected(), "La tarifa Comfort no fue seleccionada correctamente"

    def test_3_enter_phone_number(self):
        self.page.enter_phone_number(phone_number)
        assert self.page.is_phone_input_filled_correctly(phone_number), "El número ingresado no coincide"

    def test_4_enter_sms_code(self):
        code = get_sms_code(phone_number)

        if not code:
            print("No se recibió el código SMS.")
            self.driver.quit()
            assert False, "No se recibió el código SMS"

        self.page.enter_sms_code(code)
        is_accepted = self.page.is_sms_code_accepted()

        if is_accepted:
            print("Prueba 4 superada")
        else:
            print("El código SMS no fue aceptado")
            assert False, "El código SMS no fue aceptado"

    def test_5_add_credit_card(self):
        self.page.add_credit_card(card_number, card_cvv)
        assert self.page.is_card_linked(), "La tarjeta no fue vinculada correctamente"

    def test_6_write_driver_message(self):
        self.page.write_driver_message(message_for_driver)
        assert self.page.is_message_sent(message_for_driver), "El mensaje no se ingresó correctamente"

    def test_7_toggle_blanket_and_tissues(self):
        self.page.toggle_blanket_and_tissues()
        assert self.page.is_blanket_and_tissues_selected(), "La opción de manta y pañuelos no fue activada"

    def test_8_add_ice_cream(self):
        self.page.add_ice_cream()
        assert self.page.is_ice_cream_added(), "No se agregaron 2 helados"

    def test_9_confirm_trip_and_check_driver(self):
        self.page.confirm_trip()
        assert self.page.wait_for_driver_info(), "La información del conductor no apareció"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
