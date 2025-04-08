Tasks:

Installed WinAppDriver, Appium and required capabilities to run the calculatortest python code. The python script ran successfully. This script gives one error that is because of UI principle change. Installed inspect.exe to interact with UI elements. Due to version control, calculatortest python script was not running successfully.
Reflection:

WinAppDriver interact with windows desktop applications using UI automation API. API helps WinAppDriver to locate UI elements of windows application. If the provided script asks WinAppDriver to click or any button to use, the tool uses the API to interact with them and give the results.

Key steps for setting up an Appium test:
i) Install Appium server, WinAppDriver, Python, Appium-Python-Client, Inspect.exe and
required dependencies.
ii) Run Winappdriver and get the Automation ID or name through inspect.exe.
iii) Write and run the python code through terminal.

How do you identify UI elements for automation?
Using inspect.exe.

Challenges:
i) Inconsistent element ID.
ii) Limited custom UI elements.
iii) Accessibility.
iv) Unreliable Window Focus.
v) Synchronization and Timing Issues.