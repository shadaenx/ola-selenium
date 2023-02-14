from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# variables for webdriver use
ser = Service(r"C:/Users/shada/Downloads/chromedriver_win32 (1)/chromedriver.exe")  # this will need to be changed ...
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)


def hudl_login():
    # navigate to hudl website
    driver.get("https://book.olacabs.com/login?pickup_name=106%2C%20Golf%20City%2C%20Lucknow&lat=26.7845632&lng=81.002496&pickup=")

    # account credentials
    number = "8854564564"

    # get element for the login button and click it
    login = driver.find_element(By.XPATH, "//*[@id="phone-number"]")
    login.click()

    # wait for the login page to load
    driver.implicitly_wait(10)

    # get text box element for the username and send username variable
    login_email = driver.find_element(By.ID, "email")
    login_email.send_keys(number)

    
    # get the login button and click
    submit = driver.find_element(By.XPATH, "//*[@id='logIn']")
    submit.click()

    # wait for a bit for the page to load/refresh
    driver.implicitly_wait(10)

    # verify login status by checking whether the main homepage is loaded or not
    if driver.find_element(By.ID, "koMain").is_displayed():
        print("Logged Into Hudl")
    else:
        print("Login Failed!")

    # sleep so program driver immediately close
    time.sleep(10)

    # close the driver
    driver.quit()

# run method

hudl_login()
