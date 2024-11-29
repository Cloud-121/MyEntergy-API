# Import required libraries for web automation and interaction
from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import sys
import os
import json

# Verify if username and password are provided as command-line arguments
if len(sys.argv) != 3:
    # If arguments are not provided, check for the presence of a login configuration file
    if os.path.exists('login.json'):
        with open('login.json', 'r') as f:
            login = json.load(f)
            username = login['username']
            password = login['password']
    else:
        # Prompt the user for correct usage and exit if no credentials are available
        print("Usage: python main.py <username> <password> or provide login.json")
        sys.exit(1)
else:
    # Assign username and password from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

# Define a function to verify the availability of an element on the page
def is_available(method, text):
    if method == 'ID':
        while True:
            try:
                driver.find_element(By.ID, text).text
                return True
            except:
                time.sleep(1)
    elif method == 'XPATH':
        while True:
            try:
                driver.find_element(By.XPATH, text).text
                return True
            except:
                time.sleep(1)

# Define the user agent string for the browser
test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'

# Configure Firefox browser options
options = Options()

# Uncomment the line below to enable headless mode (useful for running without a GUI)
options.headless = True
options.set_preference("general.useragent.override", test_ua)

# Disable content sandboxing and extensions for the browser
options.set_preference("security.sandbox.content.level", 0)
options.set_preference("extensions.enabled", False)

# Initialize the Firefox WebDriver instance
driver = webdriver.Firefox(options=options)

# Initialize the RecaptchaSolver for automated CAPTCHA solving
solver = RecaptchaSolver(driver=driver)

# Navigate to the target webpage
driver.get('https://myentergyadvisor.entergy.com/myenergy/usage-history')

# Wait for the login fields to become available
is_available('ID', 'input-3')

# Populate the username and password fields
driver.find_element(By.ID, 'input-3').send_keys(username)
driver.find_element(By.ID, 'input-4').send_keys(password)

# Switch to the iframe containing the CAPTCHA
driver.switch_to.frame('vfFrame')

# Wait for the reCAPTCHA iframe to become available
is_available('XPATH', '//iframe[@title="reCAPTCHA"]')


# Locate the reCAPTCHA iframe
recaptcha_iframe = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')


# Attempt to solve the reCAPTCHA
try:
    solver.click_recaptcha_v2(iframe=recaptcha_iframe)
except:
    pass

# Return to the main page content
driver.switch_to.default_content()

# Wait for the sign-in button to become available
is_available('XPATH', '/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/form/div[5]/button')

# Click the sign-in button to proceed
driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/form/div[5]/button').click()

# Wait for the main dashboard page to load
is_available('XPATH', '/html/body/div[2]/div/div[3]/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[4]/div[3]/div[1]/div[2]')

# Allow additional time for the page to stabilize after loading
time.sleep(5)

# Check if the "Get On Demand Read" button is available and functional
try:
    get_on_demand_read_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[4]/div[3]/div[5]/button[1]')
    if get_on_demand_read_button.is_enabled():
        print('Get On Demand Read is available')
        # Scroll to the button and click it
        driver.execute_script("arguments[0].scrollIntoView();", get_on_demand_read_button)
        get_on_demand_read_button.click()

        # Wait for the subsequent page elements to load
        time.sleep(20)

    else:
        print('Get On Demand Read is not available')
except Exception as e:
    print(e)

# Wait for the current month kWh usage to become available

while True:
            try:
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[4]/div[3]/div[1]/div[2]').text
                break
            except:
                time.sleep(1)
                
# Retrieve the current kWh usage information
try:
    current_kwh_usage_raw = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[4]/div[3]/div[1]/div[2]').text
    # Extract numerical data from the text
    current_kwh_usage_month = float(current_kwh_usage_raw.replace(',', '').split()[0])
    print("Current month kWh usage: ", current_kwh_usage_month)
except Exception as e:
    print(e)

# Terminate the WebDriver session
driver.quit()
