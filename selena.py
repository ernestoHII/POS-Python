# Import necessary modules from the Selenium library
from selenium import webdriver  # Import the WebDriver class for browser automation
from selenium.webdriver.common.keys import Keys  # Import the Keys class for keyboard input
from selenium.webdriver.common.by import By  # Import the By class for locating elements by different strategies

# Import the time module to introduce a pause in the script
import time

# Specify the path to the ChromeDriver executable
chrome_driver_path = r'C:\hii\POS-Python\chromedriver-win64\chromedriver.exe'

# Create ChromeOptions and set the executable path
chrome_options = webdriver.ChromeOptions()  # Create an instance of ChromeOptions
chrome_options.add_argument(f"executable_path={chrome_driver_path}")  # Set the ChromeDriver executable path

# Create a WebDriver instance with ChromeOptions
driver = webdriver.Chrome(options=chrome_options)  # Create a Chrome WebDriver instance with the specified options

# Navigate to a web page (in this case, "https://www.example.com/")
driver.get("https://easyfis-ui-next.hiro-test.net/security")  # Open the specified URL in the Chrome browser

# Find and click a link with the text "More information..."
# link = driver.find_element(By.LINK_TEXT, "More information...")  # Locate the link by its text
# link.click()  # Click the located link

# Wait for X seconds (you can use WebDriverWait for more precise waiting)
# time.sleep(10)  # Pause the script execution for 3 seconds

username = driver.find_element(By.ID, "mat-input-0")  # Replace "your_input_field_id" with the actual ID
username.send_keys("Admin")

username = driver.find_element(By.ID, "mat-input-1")  # Replace "your_input_field_id" with the actual ID
username.send_keys("humanincubator_admin@1")
# <div class="mat-form-field-infix ng-tns-c128-1"><input _ngcontent-gbo-c138="" matinput="" type="password" class="mat-input-element mat-form-field-autofill-control ng-tns-c128-1 ng-pristine ng-valid cdk-text-field-autofill-monitored ng-touched" id="mat-input-1" aria-invalid="false" aria-required="false"><span class="mat-form-field-label-wrapper ng-tns-c128-1"><label class="mat-form-field-label ng-tns-c128-1 mat-empty mat-form-field-empty ng-star-inserted" id="mat-form-field-label-3" for="mat-input-1" aria-owns="mat-input-1"><!----><mat-label _ngcontent-gbo-c138="" class="ng-tns-c128-1 ng-star-inserted">Password</mat-label><!----><!----></label><!----></span></div>
# <button _ngcontent-gbo-c138="" mat-flat-button="" color="primary" type="submit" class="mat-focus-indicator btn-login mat-flat-button mat-button-base mat-primary" style="width: 100%; font-size: 18px; padding: 10px;"><span class="mat-button-wrapper"> Login </span><div matripple="" class="mat-ripple mat-button-ripple"></div><div class="mat-button-focus-overlay"></div></button>

# Method 1: By attributes (type="submit")
# submit_button = driver.find_element_by_css_selector("button[type='submit']")
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()


# <input _ngcontent-gbo-c138="" matinput="" class="mat-input-element mat-form-field-autofill-control 
# ng-tns-c128-0 ng-pristine ng-valid cdk-text-field-autofill-monitored ng-touched" id="mat-input-0" 
# aria-invalid="false" aria-required="false">

# Insert text into the input box
# input_element.send_keys("Human_Incubator_Inc.")

# Find an input field by its name and type "Selenium Python" into it
# search_box = driver.find_element(By.NAME, "q")  # Locate the input field by its name attribute
# search_box.send_keys("Selenium Python")  # Enter the text "Selenium Python" into the input field
# search_box.send_keys(Keys.RETURN)  # Simulate pressing the Enter key to submit the form

# Find and click the "IANA-managed Reserved Domains" link by its text
# link = driver.find_element(By.LINK_TEXT, "IANA-managed Reserved Domains")
# link.click()

# Wait for X seconds (you can use WebDriverWait for more precise waiting)
time.sleep(10)  # Pause the script execution for 3 seconds

# Close the browser and end the WebDriver session
driver.quit()  # Close the Chrome browser and release associated resources
