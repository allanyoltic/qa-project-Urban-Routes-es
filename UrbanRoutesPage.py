from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 25)

    from_input = (By.ID, 'from')
    to_input = (By.ID, 'to')
    personal_mode = (By.CSS_SELECTOR, '.modes-container > div:nth-child(3)')
    taxi_type = (By.CSS_SELECTOR, '.types-container > div:nth-child(3) > img')
    request_taxi_button = (By.CSS_SELECTOR, '.results-text > button')
    comfort_tariff = (By.CSS_SELECTOR, '.tariff-cards > div:nth-child(5) > div.tcard-icon > img')

    phone_input = (By.CSS_SELECTOR, '.tariff-picker.shown > div.form > div.np-button > div')
    next_button = (By.CSS_SELECTOR, '.buttons > button')
    code_input = (By.CSS_SELECTOR, '.np-input > div.input-container.error > label')
    confirm_button = (By.CSS_SELECTOR, '.modal > div.section.active > form > div.buttons > button:nth-child(1)')

    payment_method = (By.CSS_SELECTOR, '.tariff-picker.shown .pp-button.filled .pp-text')
    add_card_button = (By.CSS_SELECTOR, '.payment-picker.open .pp-selector .pp-row.disabled .pp-title')
    card_number_input = (By.ID, 'number')
    card_cvv_input = (By.ID, 'code')
    add_card_window = (By.CSS_SELECTOR, '.payment-picker.open .modal .section.active')
    link_card_button = (By.CSS_SELECTOR, '.pp-buttons > button:nth-child(1)')
    close_payment_method = (By.CSS_SELECTOR, '.payment-picker.open .modal .section.active .pp-selector .pp-row.disabled .pp-title')

    message_input = (By.ID, 'comment')
    blanket_and_tissues_option = (By.CSS_SELECTOR, '.reqs-body > div:nth-child(1) > div > div.r-sw > div > span')
    ice_cream_add_button = (By.CSS_SELECTOR, '.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus')
    submit_button = (By.CSS_SELECTOR, '.smart-button-wrapper > button')
    driver_info = (By.CSS_SELECTOR, '.order-buttons > div:nth-child(1) > div.order-button > img')

    def enter_addresses(self, from_address, to_address):
        self.wait.until(EC.element_to_be_clickable(self.from_input)).send_keys(from_address)
        self.wait.until(EC.element_to_be_clickable(self.to_input)).send_keys(to_address)

    def get_from_input_value(self):
        return self.driver.find_element(*self.from_input).get_attribute("value")

    def get_to_input_value(self):
        return self.driver.find_element(*self.to_input).get_attribute("value")

    def select_comfort_tariff(self):
        self.wait.until(EC.element_to_be_clickable(self.personal_mode)).click()
        self.wait.until(EC.element_to_be_clickable(self.taxi_type)).click()
        self.wait.until(EC.element_to_be_clickable(self.request_taxi_button)).click()
        self.wait.until(EC.element_to_be_clickable(self.comfort_tariff)).click()

    def enter_phone_number(self, phone):
        print("[DEBUG] Esperando campo de teléfono...")
        try:
            self.wait.until(EC.element_to_be_clickable(self.phone_input)).send_keys(phone)
            self.wait.until(EC.element_to_be_clickable(self.next_button)).click()
        except:
            print("[ERROR] El campo de teléfono no apareció a tiempo.")

    def enter_sms_code(self, code):
        try:
            self.wait.until(EC.presence_of_element_located(self.code_input)).send_keys(code)
            self.wait.until(EC.element_to_be_clickable(self.confirm_button)).click()
        except:
            print("[ERROR] El campo de código no está interactuable.")

    def add_credit_card(self, number, cvv):
        try:
            self.wait.until(EC.element_to_be_clickable(self.add_card_button)).click()
        except:
            print("[ERROR] No se pudo hacer clic en el botón para agregar tarjeta.")
            return

        self.wait.until(EC.visibility_of_element_located(self.card_number_input)).send_keys(number)
        self.wait.until(EC.visibility_of_element_located(self.card_cvv_input)).send_keys(cvv)
        self.wait.until(EC.element_to_be_clickable(self.add_card_window)).click()
        self.wait.until(EC.element_to_be_clickable(self.link_card_button)).click()

    def write_driver_message(self, message):
        self.wait.until(EC.element_to_be_clickable(self.message_input)).send_keys(message)

    def toggle_blanket_and_tissues(self):
        self.wait.until(EC.element_to_be_clickable(self.blanket_and_tissues_option)).click()

    def add_ice_cream(self):
        self.wait.until(EC.element_to_be_clickable(self.ice_cream_add_button)).click()
        self.wait.until(EC.element_to_be_clickable(self.ice_cream_add_button)).click()

    def confirm_trip(self):
        try:
            # Esperamos a que esté presente en el DOM
            button = self.wait.until(EC.presence_of_element_located(self.submit_button))

            # Lo hacemos visible con scroll (evita errores por botón fuera de vista)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)

            # Esperamos a que sea clickeable y luego hacemos clic
            self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()
        except:
            print("[ERROR] No se pudo confirmar el viaje.")

    def wait_for_driver_info(self, timeout=40):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.driver_info)
            )
            return True
        except:
            return False
