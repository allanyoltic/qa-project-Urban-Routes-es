from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import data
from sms_code_fetcher import retrieve_code
from data import urban_routes_url, address_from, address_to, phone_number, card_number, card_cvv, message_for_driver
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
        self.phone_field = (By.ID, "phone")
        self.next_button = (By.CSS_SELECTOR, '.buttons > button')
        self.code_input = (By.CSS_SELECTOR, '.np-input > div.input-container')
        self.code_field = (By.ID, 'code')
        self.confirm_button = (By.XPATH, "//button[text()='Confirmar']")

        self.payment_method = (By.CSS_SELECTOR, '.pp-button')
        self.add_card_button = (By.CSS_SELECTOR, '.payment-picker.open .pp-selector .pp-row.disabled .pp-title')
        self.card_number_input = (By.ID, 'number')
        self.card_cvv_input = (By.XPATH, "//input[@placeholder='12']")
        self.add_card_window = (By.CSS_SELECTOR, '.payment-picker.open .modal .section.active')
        self.link_card_button = (By.CSS_SELECTOR, '.pp-buttons > button:nth-child(1)')
        self.close_button = (By.CSS_SELECTOR, '.payment-picker .close-button')
        self.pp_value = (By.CLASS_NAME, "pp-value-text")

        self.message_input = (By.ID, 'comment')
        self.blanket_and_tissues_option = (By.CSS_SELECTOR, '.reqs-body > div:nth-child(1) > div > div.r-sw > div > span')
        self.ice_cream_add_button = (By.CSS_SELECTOR, '.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus')
        self.ice_cream_counter = (By.CSS_SELECTOR, '.counter-value')
        self.submit_button = (By.CSS_SELECTOR, '.smart-button-wrapper > button')
        self.taxi_seeker_modal = (By.CSS_SELECTOR, '.order.shown > div.order-body')
        self.driver_info = (By.CSS_SELECTOR, '.order-subbody > div.order-buttons > div:nth-child(1) > div.order-button > img')

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

    def is_comfort_tariff_selected(self):
        tariffs = self.driver.find_elements(By.CLASS_NAME, "tcard")
        for tariff in tariffs:
            if "Comfort" in tariff.text and "active" in tariff.get_attribute("class"):
                return True

    def enter_phone_number(self):
        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(self.phone_input)).click()
        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(self.phone_field)).send_keys(data.phone_number)
        self.driver.find_element(*self.next_button).click()
        phone_code_helper = retrieve_code(self.driver)
        code = phone_code_helper.get_sms_code(self.driver)
        #WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.code_field)).send_keys(code)
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self.code_field))
        self.driver.find_element(*self.code_field).send_keys(code)
        self.driver.find_element(*self.confirm_button).click()

    def is_phone_input_filled_correctly(self):
        return self.driver.find_element(*self.phone_field).get_property('value')

    def add_credit_card(self, number, cvv):
        try:
            WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self.payment_method)).click()
            # self.wait.until(EC.element_to_be_clickable(*self.add_card_button)).click()
            WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self.add_card_button)).click()
            self.wait.until(EC.visibility_of_element_located(self.card_number_input)).send_keys(number)
            self.wait.until(EC.visibility_of_element_located(self.card_cvv_input)).send_keys(cvv)
            #self.wait.until(EC.element_to_be_clickable(self.add_card_window)).click()
            WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self.add_card_window)).click()
            self.wait.until(EC.element_to_be_clickable(self.link_card_button)).click()
            WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self.close_button)).click()

        except Exception as e:
            print(f"[ERROR] No se pudo agregar la tarjeta: {e}")

    def is_card_linked(self):
        return self.driver.find_element(*self.pp_value).text

    def write_driver_message(self, message):
        message_box = self.wait.until(EC.presence_of_element_located(self.message_input))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", message_box)
        message_box.clear()
        message_box.send_keys(message)

    def is_message_sent(self, expected_message):
        message_input = self.driver.find_element(*self.message_input)
        return expected_message in message_input.get_attribute("value")

    def toggle_blanket_and_tissues(self):
        option = self.wait.until(EC.element_to_be_clickable(self.blanket_and_tissues_option))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
        option.click()

    def is_blanket_and_tissues_selected(self):
        checkbox = self.driver.find_element(By.CSS_SELECTOR, 'input.switch-input')
        return checkbox.is_selected()

    def add_ice_cream(self, quantity=2):
        button = self.wait.until(EC.element_to_be_clickable(self.ice_cream_add_button))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        for _ in range(quantity):
            button.click()
            self.wait.until(EC.element_to_be_clickable(self.ice_cream_add_button))

    def get_ice_cream_count(self):
        counter = self.driver.find_element(*self.ice_cream_counter)
        return int(counter.text.strip())

    def is_ice_cream_added(self):
        return self.get_ice_cream_count() == 2

    def confirm_trip(self):
        button = self.wait.until(EC.presence_of_element_located(self.submit_button))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()

    def is_taxi_modal(self, timeout=3):
        driver_img = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.taxi_seeker_modal))
        return driver_img.is_displayed()

    def wait_for_driver_info(self, timeout=20):
        driver_img = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.driver_info)
        )
        return driver_img.is_displayed()