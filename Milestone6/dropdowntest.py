from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Define desired capabilities for Appium (adjust this according to your setup)
caps = {
    "platformName": "Windows",
    "deviceName": "WindowsPC",
    "app": "C:\\Windows\\System32\\notepad.exe"
}

# Set up the WebDriver
driver = webdriver.Remote("http://127.0.0.1:4723", caps)

# Create an explicit wait
wait = WebDriverWait(driver, 30)  # Increased timeout duration

try:
    # Locate the "Edit" menu and hover over it using ActionChains
    print("Waiting for Edit menu to appear...")
    edit_menu_item = wait.until(EC.presence_of_element_located((By.NAME, "Edit")))
    print("Found Edit menu, clicking on it...")
    actions = ActionChains(driver)
    actions.move_to_element(edit_menu_item).click().perform()  # Hover and click on Edit menu

    # Wait for the Font menu item to appear using a more reliable XPath
    print("Waiting for Font menu item to appear...")
    font_option = wait.until(EC.presence_of_element_located((By.XPATH, "//MenuItem[@LocalizedControlType='menu item'][contains(@Name, 'Font')]")))
    print("Clicking on Font option...")
    font_option.click()

    # Wait for the "Size" ComboBox to appear under the Font tab
    print("Waiting for 'Size' ComboBox to appear...")
    size_button = wait.until(EC.presence_of_element_located((By.XPATH, "//ComboBox[@Name='Size']")))
    print("Clicking on Size ComboBox to open the dropdown...")
    size_button.click()

    # Give the dropdown some time to open
    time.sleep(2)

    # Ensure the dropdown opened by sending a DOWN key press to open the list
    print("Simulating DOWN key press to open dropdown...")
    size_button.send_keys(Keys.DOWN)
    time.sleep(2)  # Add a small delay

    # Locate and click on the Font Size option "16"
    print("Clicking on Font Size 16...")
    font_size_option = wait.until(EC.presence_of_element_located((By.XPATH, "//ComboBoxItem[contains(text(), '16')]")))
    actions.move_to_element(font_size_option).click().perform()

    # Confirm the selection by clicking "OK" or applying the changes
    ok_button = wait.until(EC.presence_of_element_located((By.NAME, "OK")))
    print("Clicking OK to confirm...")
    ok_button.click()

    print("✅ Font size changed to 16")

finally:
    # Quit the driver
    driver.quit()
