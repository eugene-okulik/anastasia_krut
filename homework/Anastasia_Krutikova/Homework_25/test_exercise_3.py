import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.implicitly_wait(6)


def test_choose_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')

    choose_language = driver.find_element(By.ID, 'id_choose_language')
    choose_language.click()
    python_language = driver.find_element(By.XPATH, '//*[@value="1"]')
    expected_language = python_language.text
    python_language.click()

    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.submit()

    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == expected_language


def test_hello_world(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')

    start_button = driver.find_element(By.XPATH, '//*[@id="start"]/button')
    start_button.click()

    finish_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="finish"]/h4'))
    )

    assert finish_text.text == 'Hello World!'
