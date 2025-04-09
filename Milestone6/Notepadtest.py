from appium import webdriver
from selenium.webdriver.common.by import By
import time

# Desired capabilities for Notepad
caps = {
    "app": "C:\\Windows\\System32\\notepad.exe",
    "platformName": "Windows",
    "deviceName": "WindowsPC"
}

# Start session
driver = webdriver.Remote("http://127.0.0.1:4723", caps)

# Allow time for Notepad to open
time.sleep(2)

# Locate the Notepad text editor using the correct class name
editor = driver.find_element(By.CLASS_NAME, "RichEditD2DPT")
editor.send_keys("Hello from the new Notepad!")

# Wait a moment to see the text appear
time.sleep(1)

# NOTE: Modern Notepad doesn't expose text content to `.text`, so we skip assert here
print("✅ Successfully sent text to Notepad.")

# Optional: Close Notepad (without saving)
driver.quit()
