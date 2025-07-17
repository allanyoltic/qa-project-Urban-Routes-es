from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.from_input = (By.ID, 'from')
        self.to_input = (By.ID, 'to')
        self.personal_mode = (By.CSS_SELECTOR, '.modes-container > div:nth-child(3)')
        self.taxi_type = (By.CSS_SELECTOR, '.types-container > div:nth-child(3) > img')
        self.request_taxi_button = (By.CSS_SELECTOR, '.results-text > button')
        self.comfort_tariff = (By.CSS_SELECTOR, '.tariff-cards > div:nth-child(5) > div.tcard-icon > img')

        self.phone_input = (By.CSS_SELECTOR, '.tariff-picker.shown > div.form > div.np-button > div')
        self.phone_field = (By.ID, 'phone')
        self.next_button = (By.CSS_SELECTOR, '.buttons > button')
        self.code_input = (By.CSS_SELECTOR, '.np-input > div.input-container')
        self.code_field = (By.ID, 'code')
        self.confirm_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')

        self.payment_method = (By.CSS_SELECTOR, '.tariff-picker.shown .pp-button.filled .pp-text')
        self.add_card_button = (By.CSS_SELECTOR, '.payment-picker.open .pp-selector .pp-row.disabled .pp-title')
        self.card_number_input = (By.ID, 'number')
        self.card_cvv_input = (By.ID, 'code')
        self.add_card_window = (By.CSS_SELECTOR, '.payment-picker.open .modal .section.active')
        self.link_card_button = (By.CSS_SELECTOR, '.pp-buttons > button:nth-child(1)')

        self.message_input = (By.ID, 'comment')
        self.blanket_and_tissues_option = (By.CSS_SELECTOR, '.reqs-body > div:nth-child(1) > div > div.r-sw > div > span')
        self.ice_cream_add_button = (By.CSS_SELECTOR, '.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus')
        self.ice_cream_counter = (By.CSS_SELECTOR, '.counter-value')
        self.submit_button = (By.CSS_SELECTOR, '.smart-button-wrapper > button')
        self.driver_info = (By.XPATH, '//*[@alt="close"]')

    def enter_addresses(self, from_address, to_address):
        from_elem = self.wait.until(EC.presence_of_element_located(self.from_input))
        from_elem.clear()
        from_elem.send_keys(from_address)

        to_elem = self.wait.until(EC.presence_of_element_located(self.to_input))
        to_elem.clear()
        to_elem.send_keys(to_address)

    def get_from_input_value(self):
        return self.driver.find_element(*self.from_input).get_attribute("value")

    def get_to_input_value(self):
        return self.driver.find_element(*self.to_input).get_attribute("value")

    def select_comfort_tariff(self):
        self.wait.until(EC.element_to_be_clickable(self.personal_mode)).click()
        self.wait.until(EC.element_to_be_clickable(self.taxi_type)).click()
        self.wait.until(EC.element_to_be_clickable(self.request_taxi_button)).click()

        comfort_elem = self.wait.until(EC.presence_of_element_located(self.comfort_tariff))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", comfort_elem)
        self.wait.until(EC.element_to_be_clickable(self.comfort_tariff)).click()

    def enter_phone_number(self, phone):
        try:
            self.wait.until(EC.element_to_be_clickable(self.phone_input)).click()
            input_field = self.wait.until(EC.element_to_be_clickable(self.phone_field))
            input_field.clear()
            input_field.send_keys(phone)
            self.wait.until(EC.element_to_be_clickable(self.next_button)).click()
        except Exception as e:
            print(f"[ERROR] Fallo al ingresar número de teléfono: {e}")

    def wait_for_sms_input(self):
        return self.wait.until(EC.presence_of_element_located(self.code_input))  # sin visibility, aún no lo escribimos

    def enter_sms_code(self, code):
        try:
            self.wait.until(EC.visibility_of_element_located(self.code_field)).send_keys(code)
            self.wait.until(EC.element_to_be_clickable(self.confirm_button)).click()
        except:
            print("[ERROR] El campo de código no está interactuable.")

    def add_credit_card(self, number, cvv):
        try:
            self.wait.until(EC.element_to_be_clickable(self.add_card_button)).click()
            self.wait.until(EC.visibility_of_element_located(self.card_number_input)).send_keys(number)
            self.wait.until(EC.visibility_of_element_located(self.card_cvv_input)).send_keys(cvv)
            self.wait.until(EC.element_to_be_clickable(self.add_card_window)).click()
            self.wait.until(EC.element_to_be_clickable(self.link_card_button)).click()
        except Exception as e:
            print(f"[ERROR] No se pudo agregar la tarjeta: {e}")

    def write_driver_message(self, message):
        try:
            message_box = self.wait.until(EC.presence_of_element_located(self.message_input))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", message_box)
            message_box.clear()
            message_box.send_keys(message)
        except Exception as e:
            print(f"[ERROR] No se pudo escribir el mensaje: {e}")

    def toggle_blanket_and_tissues(self):
        try:
            option = self.wait.until(EC.element_to_be_clickable(self.blanket_and_tissues_option))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
            option.click()
        except Exception as e:
            print(f"[ERROR] No se pudo alternar manta y pañuelos: {e}")

    def add_ice_cream(self, quantity=2):
        try:
            button = self.wait.until(EC.element_to_be_clickable(self.ice_cream_add_button))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
            for _ in range(quantity):
                button.click()
                self.wait.until(EC.element_to_be_clickable(self.ice_cream_add_button))
        except Exception as e:
            print(f"[ERROR] No se pudo agregar helado: {e}")

    def confirm_trip(self):
        try:
            button = self.wait.until(EC.presence_of_element_located(self.submit_button))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
            self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()
        except Exception as e:
            print(f"[ERROR] No se pudo confirmar el viaje: {e}")

    def wait_for_driver_info(self, timeout=20):
        try:
            driver_img = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.driver_info)
            )
            return driver_img.is_displayed()
        except:
            return False

    # --- Validadores (para asserts) ---

    def is_comfort_tariff_selected(self):
        try:
            tariffs = self.driver.find_elements(By.CLASS_NAME, "tcard")
            for tariff in tariffs:
                if "Comfort" in tariff.text and "active" in tariff.get_attribute("class"):
                    return True
            return False
        except:
            return False

    def is_phone_input_filled_correctly(self, expected_value):
        try:
            input_field = self.wait.until(EC.presence_of_element_located(self.phone_field))
            return input_field.get_attribute("value") == expected_value
        except:
            return False

    def is_sms_code_field_visible(self):
        try:
            code_input = self.wait.until(EC.visibility_of_element_located(self.code_field))
            return code_input.is_displayed() and code_input.is_enabled()
        except:
            return False

    def is_sms_code_accepted(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.confirm_button)).click()
        except:
            sms_form = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.number-picker.open > div.modal > div.section.active')))
            return sms_form.is_displayed()
            return False

    def is_card_linked(self):
        try:
            checkbox = self.driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"].checkbox')
            return checkbox.is_selected()
        except:
            return False

    def is_message_sent(self, expected_message):
        try:
            message_input = self.driver.find_element(*self.message_input)
            return expected_message in message_input.get_attribute("value")
        except:
            return False

    def is_blanket_and_tissues_selected(self):
        try:
            checkbox = self.driver.find_element(By.CSS_SELECTOR, 'input.switch-input')
            return checkbox.is_selected()
        except:
            return False

    def get_ice_cream_count(self):
        try:
            counter = self.driver.find_element(*self.ice_cream_counter)
            return int(counter.text.strip())
        except:
            return 0

    def is_ice_cream_added(self):
        return self.get_ice_cream_count() == 2


# helper dentro de la clase
def _send_keys_js(self, element, value):
    # escribe carácter a carácter para que dispare eventos
    for ch in value:
        element.send_keys(ch)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }))", element)
