from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Specify the path to the ChromeDriver executable
chrome_driver_path = r'C:\hii\POS-Python\chromedriver-win64\chromedriver.exe'

# Create a WebDriver instance with the specified path
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open the local HTML file containing the example.com content
driver.get("https://www.example.com/")

# Find and click a link (in this case, a link with the text "More information...")
link = driver.find_element(By.LINK_TEXT, "More information...")
link.click()

# Find an input field and type something into it
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)  # Simulate pressing the Enter key

# Wait for a few seconds (you can use WebDriverWait for more precise waiting)
import time
time.sleep(3)

# Capture a screenshot (you can customize the file name and format)
driver.save_screenshot("screenshot.png")

# Close the browser
driver.quit()

