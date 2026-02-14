from playwright.sync_api import Page, expect
from datetime import datetime


def test_first(page: Page):
    page.goto('https://the-internet.herokuapp.com/')

    form_authentication = page.get_by_role('link', name='Form Authentication')
    form_authentication.click()

    username = page.get_by_role('textbox', name='Username')
    username.fill('Anastasia')

    password = page.get_by_role('textbox', name='Password')
    password.fill('Test')

    login_button = page.get_by_role('button', name='Login')
    login_button.click()


def test_second(page: Page):
    #   page.goto('https://demoqa.com/automation-practice-form')
    page.goto('https://demoqa.com/')
    page.get_by_text("Forms").click()
    page.get_by_role("link", name="Practice Form").click()

    data_of_birth = datetime.strptime('01.01.1995', '%d.%m.%Y').strftime('%d %b %Y')
    first_name_data = 'Anastasia'
    last_name_data = 'Lastname'
    email_data = 'name@example.com'
    current_address_data = 'test_current_address'
    mobile_data = '1234567907'

    first_name = page.locator('//*[@id="firstName"]')
    last_name = page.locator('//*[@id="lastName"]')
    email_field = page.get_by_placeholder("name@example.com")
    gender_radiobutton_female = page.locator('//*[@for="gender-radio-2"]')
    mobile_field = page.get_by_placeholder("Mobile Number")
    date_field = page.locator('//*[@id="dateOfBirthInput"]')
    subjects_field = page.locator('//*[@id="subjectsInput"]')

    hobbies_checkbox_sport = page.locator('//*[@for="hobbies-checkbox-1"]')
    current_address_field = page.get_by_placeholder("Current Address")

    first_name.fill(first_name_data)
    last_name.fill(last_name_data)
    email_field.fill(email_data)
    gender_radiobutton_female.click()
    mobile_field.fill(mobile_data)

    date_field.click()
    date_field.press('Backspace')
    date_field.fill(data_of_birth)
    date_field.press('Enter')

    subjects_field.click()
    subjects_field.fill('m')

    page.get_by_text("Maths").click()

    hobbies_checkbox_sport.click()
    current_address_field.fill(current_address_data)

    state = page.locator('//*[@id="state"]')
    state.click()
    page.get_by_text("NCR").click()

    page.locator('//*[@id="city"]').click()
    page.get_by_text("Noida").click()

    submit_button = page.locator('//*[@id="submit"]')
    submit_button.press('Enter')
