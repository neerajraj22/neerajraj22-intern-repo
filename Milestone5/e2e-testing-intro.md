Tasks:

What E2E testing is and how it differs from unit/integration testing?

E2E testing means end-to-end testing which validates the entire application from start to finish to check the complete workflow as expected. On the other hand, Unit testing focused only on individual component or single piece of logic to validate. The integration testing ensures the various components interact each other.

Benefits and limitations of automated E2E tests?

Immediate feedback on the system's behaviour.
Consistent and reliable.
E2E tests can be reused as the application evolves.
Improves test coverage for cross-platform applications.
Integration with CI/CD Pipelines.

Limitations:

E2E test requires a considerable time to write scripts and automate all the necessary actions.
Automated tests need to be maintained as the application changes.
Automated tests can be flaky due to unexpected delays in the system.
Running E2E tests can slow the testing process due to high resource consumption.
Limited to Functional Testing.

How Focus Bear uses E2E tests to maintain app stability?

Focus Bear ensures that E2E tests works from logging in to manage focus sessions.
The app should verify the app's stability across all other platforms.
E2E tests checks for any new features doesn't introducing bugs.
It ensures all the interactive elements such as navigating between tasks works properly.

How does automated testing help Focus Bear reduce regression bugs?
If we add a new feature, automated tests execute the same steps everytime to check if the previous feature is working properly. This consistency helps to identify the bugs in an early stage.