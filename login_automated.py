from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
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
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver
def clean_text(text):
    #Extract only the number
    output = int(text.split(": ")[1])
    return output

def main():
    driver = get_driver()


    driver.find_element(by="id", value="id_username").send_keys("automated")
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated") #+ Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/div[1]/div/div/div[3]/form/button").click()
    print(driver.current_url) #show current url
    time.sleep(3)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    time.sleep(10)
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name1 = f"file_{current_datetime}.txt"
    element =driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    element3 = str(clean_text(element.text))
    with open(file_name1, 'w') as f:
        f.write(element3)
    time.sleep(2)
    current_datetime2 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    element1 = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    element2 = str(clean_text(element1.text))
    file_name2 = f"file_{current_datetime2}.txt"
    with open(file_name2, 'w') as f1:
        f1.write(element2)

print(main())
