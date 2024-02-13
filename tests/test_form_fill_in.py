import pytest
from selene import browser, be, have, by
import os


def test_registration_form(browser_conf):
    browser.open('/')
    # browser.driver.execute_script("document.querySelector('.body-height').style.transform='scale(.50)'")
    browser.element('#firstName').type('Danil')
    browser.element('#lastName').type('Reznikov')
    browser.element('#userEmail').type('test1@mail.ru')
    browser.all('.custom-radio').element_by(have.text('Male')).click()
    browser.element('#userNumber').type('7712836614')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('October')
    browser.element('.react-datepicker__year-select').type('1996')
    browser.element(f'.react-datepicker__day--0{14}').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/image_2024-02-08_19-42-48.png'))
    browser.element('#currentAddress').type('Almaty')
    browser.element('#state').click().element(by.text('NCR')).click()
    browser.element('#city').click().element(by.text('Delhi')).click()
    browser.element('#submit').click()

    # assert
    browser.element('.table-responsive').all('td').even.should(have.texts(
        'Danil Reznikov',
        'test1@mail.ru',
        'Male',
        '7712836614',
        '14 October,1996',
        'Computer Science',
        'Sports, Reading',
        'image_2024-02-08_19-42-48.png',
        'Almaty',
        'NCR Delhi'
    ))
