import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.implicitly_wait(6)


def test_input_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')

    data_of_birth = datetime.strptime('01.01.1995', '%d.%m.%Y').strftime('%d %b %Y')
    first_name_data = 'Anastasia'
    last_name_data = 'Lastname'
    email_data = 'name@example.com'
    current_address_data = 'test_current_address'
    mobile_data = '1234567907'

    first_name = driver.find_element(By.ID, 'firstName')
    last_name = driver.find_element(By.ID, 'lastName')
    email_field = driver.find_element(By.XPATH, '//*[@placeholder="name@example.com"]')
    gender_radiobutton_female = driver.find_element(By.XPATH, '//*[@for="gender-radio-1"]')
    mobile_field = driver.find_element(By.XPATH, '//*[@placeholder="Mobile Number"]')
    date_field = driver.find_element(By.ID, 'dateOfBirthInput')
    subjects_field = driver.find_element(By.ID, "subjectsInput")

    hobbies_checkbox_sport = driver.find_element(By.XPATH, '//*[@for="hobbies-checkbox-1"]')
    current_address_field = driver.find_element(By.XPATH, '//*[@placeholder="Current Address"]')

    first_name.send_keys(first_name_data)
    last_name.send_keys(last_name_data)
    email_field.send_keys(email_data)
    gender_radiobutton_female.click()
    mobile_field.send_keys(mobile_data)

    date_field.click()
    date_field.send_keys(Keys.BACKSPACE * 10)
    date_field.send_keys(data_of_birth)
    date_field.send_keys(Keys.ENTER)

    subjects_field.click()
    subjects_field.send_keys('m')

    maths_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Maths']"))
    )
    maths_option.click()

    hobbies_checkbox_sport.click()
    current_address_field.send_keys(current_address_data)

    driver.execute_script('window.scroll(0,600)')
    state = driver.find_element(By.ID, 'state')
    state.click()
    driver.find_element(By.XPATH, "//div[text()='NCR']").click()

    state = driver.find_element(By.ID, 'city')
    state.click()
    driver.find_element(By.XPATH, "//div[text()='Noida']").click()

    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.submit()
