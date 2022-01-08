import logging
import logging.config
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

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

    driver = webdriver.Chrome(ChromeDriverManager().install())

    try:
        driver.get("https://stackoverflow.com")

        driver.find_element(By.LINK_TEXT, "Log in").click()

        driver.find_element(By.ID, "email").send_keys(os.environ['STACK_OVERFLOW_EMAIL'])
        driver.find_element(By.ID, "password").send_keys(os.environ['STACK_OVERFLOW_PASSWORD'])
        driver.find_element(By.ID, "submit-button").submit()

        driver.find_element(By.CLASS_NAME, "my-profile").click()

        elem = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "grid--cell.ws-nowrap.fs-body3"))
        )
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
