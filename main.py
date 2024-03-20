from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def get_driver():
    # Set Option to make Browsing Easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com/")
    return driver
def clean_text(text):
    #Extract only the number
    output = int(text.split(": ")[1])
    return output

def main():
    driver = get_driver()
    time.sleep(3)

    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)
print(main())
