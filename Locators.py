from selenium.webdriver.common.by import By

class TaxiLocators:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    personal_mode = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[1]/div[3]')
    taxi_mode = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[2]/div[3]/img')
    request_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    comfort_tariff_option = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img')

    phone_input = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[1]/div/input')
    next_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    code_input = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[1]/div/input')
    confirm_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')

    add_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/div/img')
    card_number_input = (By.ID, 'number')
    card_cvv_input = (By.ID, 'code')
    link_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')

    message_input = (By.XPATH, '//*[@id="comment"]')

    blanket_option = (By.XPATH, '(//span[@class="slider round"])[1]')
    tissues_option = (By.XPATH, '(//span[@class="slider round"])[2]')

    ice_cream_add_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')

    submit_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button/span[2]')

    driver_info = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[1]/img')
