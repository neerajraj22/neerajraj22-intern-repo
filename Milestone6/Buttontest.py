from appium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up desired capabilities
desired_caps = {
    "app": "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App",  # Launch Calculator
    "platformName": "Windows",
    "deviceName": "WindowsPC"
}

# Connect to WinAppDriver
driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
time.sleep(2)

# Find buttons and click them
driver.find_element(By.ACCESSIBILITY_ID, "num1Button").click()
driver.find_element(By.ACCESSIBILITY_ID, "plusButton").click()
driver.find_element(By.ACCESSIBILITY_ID, "num2Button").click()
driver.find_element(By.ACCESSIBILITY_ID, "equalButton").click()

# Verify result
result = driver.find_element(By.ACCESSIBILITY_ID, "CalculatorResults").text
print("Calculation result:", result)

assert "3" in result, "Test Failed: Expected result to contain 3"

print("✅ Test Passed!")

# Close the app
driver.quit()
