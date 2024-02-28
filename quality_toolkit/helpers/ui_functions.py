"""
All methods link to the ui
"""
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright
from selenium import webdriver


def install_selenium_webdriver(remote_url='http://127.0.0.1:4444/wd/hub', browser='chrome', headless=True):
    """ Method to install the Selenium WebDriver.

    Args:
        remote_url (str, optional): Either a string representing the URL of the remote server or a custom RemoteConnection object.
            Defaults to 'http://127.0.0.1:4444/wd/hub'.
        browser (str, optional): Define which type of browser to instantiate. Possible values are 'chrome', 'firefox', or 'edge'.
            Opera is not supported by Selenium: https://github.com/robotframework/SeleniumLibrary/pull/1782.
            Defaults to 'chrome'.
        headless (bool, optional): Set the headless option, which is only available for Chrome and Firefox.
            Defaults to True.
    """
    if browser == 'firefox':
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        return webdriver.Remote(remote_url, options=options)
    elif browser == 'edge':
        cap = {'browserName': 'MicrosoftEdge'}
        return webdriver.Remote(remote_url, desired_capabilities=cap)
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        if headless:
            options.add_argument("--headless")
        return webdriver.Remote(remote_url, options=options)


def install_sync_playwright(browser='chromium', **kwargs):
    """ Method to install the Sync Playwright browser.

        Args:
            browser (str, optional): The browser name, possible values are 'chrome', 'firefox', or 'webkit'. Defaults to 'chrome'.
            executable_path (Union[pathlib.Path, str, None], optional): Path to a browser executable to run instead of the bundled one,
                if `executable_path` is a relative path, then it is resolved relative to the current working directory.
                Note that Playwright only works with the bundled Chromium, Firefox, or WebKit, use at your own risk.
                Defaults to None.
            channel (Union[str, None], optional): Browser distribution channel, supported values are 'chrome', 'chrome-beta',
                'chrome-dev', 'chrome-canary', 'msedge', 'msedge-beta', 'msedge-dev', 'msedge-canary'.
                Read more about using [Google Chrome and Microsoft Edge](../browsers.md#google-chrome--microsoft-edge).
                Defaults to None.
            args (Union[List[str], None], optional): Additional arguments to pass to the browser instance,
                the list of Chromium flags can be found [here](http://peter.sh/experiments/chromium-command-line-switches/).
                Defaults to None.
            ignore_default_args (Union[List[str], bool, None], optional): If True, Playwright does not pass its own configuration args
                and only uses the ones from `args`. If a list is given, it filters out the given default arguments.
                Dangerous option; use with care. Defaults to False.
            handle_sigint (Union[bool, None], optional): Close the browser process on Ctrl-C. Defaults to True.
            handle_sigterm (Union[bool, None], optional): Close the browser process on SIGTERM. Defaults to True.
            handle_sighup (Union[bool, None], optional): Close the browser process on SIGHUP. Defaults to True.
            timeout (Union[float, None], optional): Maximum time in milliseconds to wait for the browser instance to start.
                Defaults to 30000 (30 seconds). Pass 0 to disable timeout.
            env (Union[Dict[str, Union[bool, float, str]], None], optional): Specify environment variables that will be visible to the browser.
                Defaults to `process.env`.
            headless (Union[bool, None], optional): Whether to run the browser in headless mode.
                Defaults to True unless the `devtools` option is True.
            devtools (Union[bool, None], optional): **Chromium-only** Whether to auto-open a Developer Tools panel for each tab.
                If True, the `headless` option will be set to False.
            proxy (Union[
                {'server': str, 'bypass': Union[str, None], 'username': Union[str, None], 'password': Union[str, None]}, None
            ], optional): Network proxy settings.
            downloads_path (Union[pathlib.Path, str, None], optional): If specified, accepted downloads are downloaded into this directory.
                Otherwise, a temporary directory is created and is deleted when the browser is closed.
                In either case, the downloads are deleted when the browser context they were created in is closed.
            slow_mo (Union[float, None], optional): Slows down Playwright operations by the specified amount of milliseconds.
                Useful for debugging. Defaults to None.
            traces_dir (Union[pathlib.Path, str, None], optional): If specified, traces are saved into this directory.
            chromium_sandbox (Union[bool, None], optional): Enable Chromium sandboxing. Defaults to None.
            firefox_user_prefs (Union[Dict[str, Union[bool, float, str]], None], optional): Firefox user preferences.
                Learn more about the Firefox user preferences at `about:config`.

        """
    playwright = sync_playwright().start()
    if browser == 'webkit':
        return playwright.webkit.launch(**kwargs)
    if browser == 'firefox':
        return playwright.firefox.launch(**kwargs)
    if browser == 'chrome':
        return playwright.chromium.launch(channel="chrome", **kwargs)
    if browser == 'msedge':
        return playwright.chromium.launch(channel="msedge", **kwargs)
    else:
        return playwright.chromium.launch(**kwargs)


async def install_async_playwright_browser( browser: str = 'chrome', **kwargs):
    """ Method to install the Async Playwright browser.

    Args:
        browser (str, optional): The browser name, possible values are 'chrome', 'firefox', or 'webkit'. Defaults to 'chrome'.
        executable_path (Union[pathlib.Path, str, None], optional): Path to a browser executable to run instead of the bundled one,
            if `executable_path` is a relative path, then it is resolved relative to the current working directory.
            Note that Playwright only works with the bundled Chromium, Firefox, or WebKit, use at your own risk.
            Defaults to None.
        channel (Union[str, None], optional): Browser distribution channel, supported values are 'chrome', 'chrome-beta',
            'chrome-dev', 'chrome-canary', 'msedge', 'msedge-beta', 'msedge-dev', 'msedge-canary'.
            Read more about using [Google Chrome and Microsoft Edge](../browsers.md#google-chrome--microsoft-edge).
            Defaults to None.
        args (Union[List[str], None], optional): Additional arguments to pass to the browser instance,
            the list of Chromium flags can be found [here](http://peter.sh/experiments/chromium-command-line-switches/).
            Defaults to None.
        ignore_default_args (Union[List[str], bool, None], optional): If True, Playwright does not pass its own configuration args
            and only uses the ones from `args`. If a list is given, it filters out the given default arguments.
            Dangerous option; use with care. Defaults to False.
        handle_sigint (Union[bool, None], optional): Close the browser process on Ctrl-C. Defaults to True.
        handle_sigterm (Union[bool, None], optional): Close the browser process on SIGTERM. Defaults to True.
        handle_sighup (Union[bool, None], optional): Close the browser process on SIGHUP. Defaults to True.
        timeout (Union[float, None], optional): Maximum time in milliseconds to wait for the browser instance to start.
            Defaults to 30000 (30 seconds). Pass 0 to disable timeout.
        env (Union[Dict[str, Union[bool, float, str]], None], optional): Specify environment variables that will be visible to the browser.
            Defaults to `process.env`.
        headless (Union[bool, None], optional): Whether to run the browser in headless mode.
            Defaults to True unless the `devtools` option is True.
        devtools (Union[bool, None], optional): **Chromium-only** Whether to auto-open a Developer Tools panel for each tab.
            If True, the `headless` option will be set to False.
        proxy (Union[
            {'server': str, 'bypass': Union[str, None], 'username': Union[str, None], 'password': Union[str, None]}, None
        ], optional): Network proxy settings.
        downloads_path (Union[pathlib.Path, str, None], optional): If specified, accepted downloads are downloaded into this directory.
            Otherwise, a temporary directory is created and is deleted when the browser is closed.
            In either case, the downloads are deleted when the browser context they were created in is closed.
        slow_mo (Union[float, None], optional): Slows down Playwright operations by the specified amount of milliseconds.
            Useful for debugging. Defaults to None.
        traces_dir (Union[pathlib.Path, str, None], optional): If specified, traces are saved into this directory.
        chromium_sandbox (Union[bool, None], optional): Enable Chromium sandboxing. Defaults to None.
        firefox_user_prefs (Union[Dict[str, Union[bool, float, str]], None], optional): Firefox user preferences.
            Learn more about the Firefox user preferences at `about:config`.

    """
    playwright = await async_playwright().start()
    if browser == 'webkit':
        return await playwright.webkit.launch(**kwargs)
    if browser == 'firefox':
        return await playwright.firefox.launch(**kwargs)
    if browser == 'chrome':
        return playwright.chromium.launch(channel="chrome", **kwargs)
    if browser == 'msedge':
        return playwright.chromium.launch(channel="msedge", **kwargs)
    else:
        return await playwright.chromium.launch(**kwargs)
