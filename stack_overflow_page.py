import logging
import logging.config
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from sendgrid_helper import send_mail

logging.config.fileConfig('logging.conf')


def login():
    logging.info("Logging into stackoverflow.com")

    email = os.environ.get('STACK_OVERFLOW_EMAIL')
    password = os.environ.get('STACK_OVERFLOW_PASSWORD')
    display_name = os.environ.get('STACK_OVERFLOW_DISPLAY_NAME')

    if None in (email, password, display_name):
        logging.error("Set 'STACK_OVERFLOW_EMAIL' 'STACK_OVERFLOW_PASSWORD' 'STACK_OVERFLOW_DISPLAY_NAME' env "
                      "variables to successfully log into Stack Overflow")
        return

    chrome_options = Options()
    chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_SHIM')
    driver = webdriver.Chrome(chrome_options=chrome_options)

    try:
        driver.get("https://stackoverflow.com")

        driver.find_element_by_link_text("Log in").click()

        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id("submit-button").submit()

        driver.find_element_by_class_name("my-profile").click()

        elem = driver.find_element_by_class_name("mini-avatar")
        assert display_name in elem.text
        logging.info("Logged into stackoverflow.com and accessed profile page.")

    except Exception as e:
        message = "An error occurred while trying to access stackoverflow.com!"
        logging.error(message, e)
        send_mail("Error at login!", message + str(e))

    finally:
        driver.close()


if __name__ == "__main__":
    login()
