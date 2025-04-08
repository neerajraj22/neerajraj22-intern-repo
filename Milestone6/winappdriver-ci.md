Tasks:

How E2E tests are integrated into CI/CD workflows:

CI/CD workflows follow build, test and deploy stages. Firstly, the app is built and all the dependencies should be installed properly. Next, it ensures that Unit, Integration and E2E tests checks the core functionalities and successful testing. Then, if all the test passes, it can proceed to deployment stage.

How Appium-based tests (WinAppDriver) can run in a CI/CD pipeline?

First, install all the required dependencies.
Write a python script.
Install pipeline tool and dependencies.
Start WinAppDriver.
Run the Appium tests.
Save the results in XML file.
When the code is committed, the pipeline tool will run. When the pipeline tool will run, WinAppDriver starts and Apppium will interact with the application. The tests will execute, and Jenkins will provide feedback on whether the tests passed or failed.The logs can be reviewed to investigate if the test fails.

How test failures impact the deployment process?

It prevents the deployment process as the CI/CD pipelines will not allow to proceed with the deployment until all the issues are fixed.
Delays in deployment.
Additional work for the development team.

Run a test locally in "headless" mode to simulate CI execution?

Headless mode means running tests without any graphical user interface (GUI). This isn't supported due to restrictions on the Windows OS in handling input injection. I am not sure about this. I have to check on it again.

How does running tests in CI/CD help maintain application stability?

Automated Tests are identified automatically whenever new code is pushed to the repository. It detects the bugs early in the deployment phase.
Consistent testing.
Faster feedback.
Minimize human errors.

What are the challenges of running GUI-based tests in CI/CD pipelines?

GUI-based tests requires more intensive resources.
GUI tests rely on elements like buttons, forms, and inputs that might change frequently during development (due to design changes).
In CI/CD pipelines, flaky tests lead to false failures.

How can flaky tests be handled in a CI/CD environment?

Identify flaky tests.
Re-run the test automatically on failure.
Add explicit waits which ensures that the test waits for elements to load before interacting.