Tasks:

How to switch between the native Windows context and WebView context:
To switch between native windows context to webview, we need to intercat with
UIAutomation or MSAA with Javascript injection.

How do you detect WebView components in a Windows app?
Using inspect.exe.

What is the difference between testing native Windows UI and WebViews?
Native elements built with Winforms whereas Webview built with HTML, Javascript etc.
For Native Windows UI, Winappdriver is used to test it but for Webview it can expect
extra tools like Javascript.

What challenges might arise when automating WebViews, and how can they be
resolved?
i) WebView elements are invisible to WinAppDriver.
ii) Timing issues.
iii) Hard to locate buttons/fields inside WebView.