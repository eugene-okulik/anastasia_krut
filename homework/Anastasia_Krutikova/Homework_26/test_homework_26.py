from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()

    yield chrome_driver

def test_1(driver):
    driver.get('http://testshop.qa-practice.com/')

    customizable_desk = driver.find_element(By.XPATH, '//*[@alt="Customizable Desk"]')

    ActionChains(driver).key_down(Keys.CONTROL).click(customizable_desk).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    text_desk = driver.find_element(By.TAG_NAME, 'h1').text

    add_to_cart = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'add_to_cart')))

    add_to_cart.click()

    continue_shopping = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'footer.modal-footer button.btn-secondary'))
    )
    continue_shopping.click()

    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.my_cart_quantity.badge'),
        '1'))

    driver.switch_to.window(tabs[0])

    cart_main = driver.find_element(By.XPATH, '//*[@aria-label="eCommerce cart"]')
    cart_main.click()

    text_desk_cart = driver.find_element(By.TAG_NAME, 'h6').text

    assert text_desk in text_desk_cart

def test_2(driver):
    driver.get('http://testshop.qa-practice.com/')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'oe_product')))

    all_products = driver.find_elements(By.CLASS_NAME, 'oe_product')
    first_product = all_products[0]

    text_first_product = first_product.text.split('\n')[0]

    actions = ActionChains(driver)
    actions.move_to_element(first_product)

    shopping_cart = driver.find_element(By.XPATH, '//*[@title="Shopping cart"]')

    actions.click(shopping_cart)
    actions.perform()

    text_product_cart = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'strong.product-name'))
    ).text

    assert text_first_product in text_product_cart
