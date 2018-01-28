import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def login():
    print("Logging into stackoverflow.com")
    chrome_options = Options()
    chrome_location = os.environ['GOOGLE_CHROME_BIN']
    print(chrome_location)
    chrome_options.binary_location = chrome_location
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--remote-debugging-port=9222')
    driver = webdriver.Chrome(executable_path=os.environ['CHROMEDRIVER_PATH'], chrome_options=chrome_options)
    # driver = webdriver.Chrome()
    try:
        driver.get("https://stackoverflow.com")

        driver.find_element_by_link_text("Log In").click()

        driver.find_element_by_id("email").send_keys(os.environ['STACK_OVERFLOW_EMAIL'])
        driver.find_element_by_id("password").send_keys(os.environ['STACK_OVERFLOW_PASSWORD'])
        driver.find_element_by_id("submit-button").submit()

        driver.find_element_by_class_name("my-profile").click()

        elem = driver.find_element_by_class_name("mini-avatar")
        assert os.environ['STACK_OVERFLOW_DISPLAY_NAME'] in elem.text
        print("Logged into stackoverflow.com and accessed profile page.")

    except Exception as e:
        print("An error occurred while trying to access stackoverflow.com", e)

    finally:
        driver.close()


login()
