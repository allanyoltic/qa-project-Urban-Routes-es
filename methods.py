from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import TaxiLocators

class TaxiMethods:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def enter_addresses(self, from_address, to_address):
        self.wait.until(EC.element_to_be_clickable(TaxiLocators.from_field)).send_keys(from_address)
        self.wait.until(EC.element_to_be_clickable(TaxiLocators.to_field)).send_keys(to_address)

    def select_comfort_tariff(self):
        self.wait.until(EC.element_to_be_clickable(TaxiLocators.personal_mode)).click()
        self.wait.until(EC.element_to_be_clickable(TaxiLocators.taxi_mode)).click()
        self.wait.until(EC.element_to_be_clickable(TaxiLocators.request_taxi_button)).click()
        self.wait.until(EC.element_to_be_clickable(TaxiLocators.comfort_tariff_option)).click()

    def enter_phone_number(self, phone):
        print("[DEBUG] Esperando campo de teléfono...")
        try:
            self.wait.until(EC.element_to_be_clickable(TaxiLocators.phone_input)).send_keys(phone)
            self.wait.until(EC.element_to_be_clickable(TaxiLocators.next_button)).click()
        except:
            print("[ERROR] El campo de teléfono no apareció a tiempo.")

    def enter_sms_code(self, code):
        try:
            self.wait.until(EC.presence_of_element_located(TaxiLocators.code_input)).send_keys(code)
            self.wait.until(EC.element_to_be_clickable(TaxiLocators.confirm_button)).click()
        except:
            print("[ERROR] El campo de código no está interactuable.")

    def add_credit_card(self, number, cvv):
        try:
            self.wait.until(EC.element_to_be_clickable(TaxiLocators.add_card_button)).click()
        except:
            print("[ERROR] No se pudo hacer clic en el botón para agregar tarjeta.")
            return

        self.wait.until(EC.visibility_of_element_located(TaxiLocators.card_number_input)).send_keys(number)
        self.wait.until(EC.visibility_of_element_located(TaxiLocators.card_cvv_input)).send_keys(cvv)
        self.wait.until(EC.element_to_be_clickable(TaxiLocators.link_card_button)).click()

    def write_driver_message(self, message):
        self.wait.until(EC.element_to_be_clickable(TaxiLocators.message_input)).send_keys(message)

    def toggle_blanket_and_tissues(self):
        self.wait.until(EC.element_to_be_clickable(TaxiLocators.blanket_option)).click()
        self.wait.until(EC.element_to_be_clickable(TaxiLocators.tissues_option)).click()

    def add_ice_cream(self):
        self.wait.until(EC.element_to_be_clickable(TaxiLocators.ice_cream_add_button)).click()
        self.wait.until(EC.element_to_be_clickable(TaxiLocators.ice_cream_add_button)).click()

    def confirm_trip(self):
        self.wait.until(EC.element_to_be_clickable(TaxiLocators.submit_button)).click()

    def wait_for_driver_photo(self, timeout=40):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(TaxiLocators.driver_info)
            )
            return True
        except:
            return False