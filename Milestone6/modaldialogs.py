from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

# Set up desired capabilities
caps = {
    "app": "C:\\Windows\\System32\\notepad.exe",  # Path to Notepad app
    "platformName": "Windows",
    "deviceName": "WindowsPC"
}

# Create a session with the app
driver = webdriver.Remote("http://127.0.0.1:4723", caps)

# Wait for the text area to become available (RichEditD2DPT is the text area)
try:
    # Use the class name "RichEditD2DPT" to locate the text area for typing
    text_area = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "RichEditD2DPT")  # The correct class name for the text area
        )
    )
    text_area.send_keys("Unsaved test")  # Type text into the text area
    print("✅ Text entered in Notepad.")

except Exception as e:
    print(f"❌ Error while interacting with text area: {e}")

# Wait for Save dialog to appear (Save dialog has "Save as" name)
time.sleep(2)

# Trying to locate the Save dialog by the class name "TextBlock"
try:
    save_dialog = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "TextBlock")  # Class name for the Save As dialog
        )
    )
    print("✅ Save dialog appeared by TextBlock class name.")
except Exception as e:
    print(f"❌ Save dialog not found: {e}")

# Attempting to close Notepad by using the 'Alt + F4' keys
try:
    # Find the Notepad window or send the Alt+F4 key to the body
    notepad_window = driver.find_element(By.CLASS_NAME, "Notepad")
    notepad_window.send_keys(Keys.ALT + Keys.F4)
    print("✅ Sent Alt+F4 to close Notepad.")
except Exception as e:
    print(f"❌ Error while closing Notepad using Alt+F4: {e}")

# Wait for the window to close and quit the driver
time.sleep(2)  # Wait to make sure the app closes
driver.quit()
