"""
All methods link to the ui
"""
import logging

from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright
from selenium import webdriver


def install_selenium_webdriver(remote_url, browser='chrome', headless=True):
    """
    Method to install selenium webdriver
    Parameters
    ------
        remote_url: str
            Either a string representing URL of the remote server or a custom
            remote_connection.RemoteConnection object. Defaults to 'http://127.0.0.1:4444/wd/hub'.
        browser: str
            Define which type of browser instantiate possible value chrome, firefox, edge
            Opera is not supported by selenium: https://github.com/robotframework/SeleniumLibrary/pull/1782
            by default chrome
        headless: bool
            Set headless option only available for chrome and firefox
            by default True
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


def initialize_sync_playwright(context):
    """
    Sync method to initialize context.browser with playwright
    Parameters
    ------
        context: behave context
    """
    logging.info(
        f"Initialize playwright - userdata browser: {context.config.userdata['browser']}")
    headless = bool(context.config.userdata['browser_headless'] == 'true')
    if context.config.userdata['browser'] not in ['chrome', 'firefox']:
        raise TypeError(
            f"The browser '{context.config.userdata['browser']}' is not handle. ")
    context.browser = __install_sync_playwright(
        browser=context.config.userdata['browser'], headless=headless)
    assert context.browser is not None, "Failed to initialize the sync driver"
    logging.info(f"Initialize playwright - Context browser: {context.browser}")


async def initialize_async_playwright(context):
    logging.info(
        f"Initialize playwright - userdata browser: {context.config.userdata['browser']}")
    headless = bool(context.config.userdata['browser_headless'] == 'true')
    if context.config.userdata['browser'] not in ['chrome', 'firefox']:
        raise TypeError(
            f"The browser '{context.config.userdata['browser']}' is not handle. ")
    context.browser = await __install_async_playwright(browser=context.config.userdata['browser'], headless=headless)
    assert context.browser is not None, "Failed to initialize the async driver"
    logging.info(f"Initialize playwright - Context browser: {context.browser}")


def __install_sync_playwright(browser='chrome', **kwargs):
    """
    Method to install sync playwright browser
    Parameters
        ----------
        browser :  str
            browser name chrome, firefox or webkit by default chrome
        executable_path : Union[pathlib.Path, str, NoneType]
            Path to a browser executable to run instead of the bundled one. If `executablePath` is a relative path, then it is
            resolved relative to the current working directory. Note that Playwright only works with the bundled Chromium, Firefox
            or WebKit, use at your own risk.
        channel : Union[str, NoneType]
            Browser distribution channel.  Supported values are "chrome", "chrome-beta", "chrome-dev", "chrome-canary", "msedge",
            "msedge-beta", "msedge-dev", "msedge-canary". Read more about using
            [Google Chrome and Microsoft Edge](../browsers.md#google-chrome--microsoft-edge).
        args : Union[List[str], NoneType]
            Additional arguments to pass to the browser instance. The list of Chromium flags can be found
            [here](http://peter.sh/experiments/chromium-command-line-switches/).
        ignore_default_args : Union[List[str], bool, NoneType]
            If `true`, Playwright does not pass its own configurations args and only uses the ones from `args`. If an array is
            given, then filters out the given default arguments. Dangerous option; use with care. Defaults to `false`.
        handle_sigint : Union[bool, NoneType]
            Close the browser process on Ctrl-C. Defaults to `true`.
        handle_sigterm : Union[bool, NoneType]
            Close the browser process on SIGTERM. Defaults to `true`.
        handle_sighup : Union[bool, NoneType]
            Close the browser process on SIGHUP. Defaults to `true`.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds to wait for the browser instance to start. Defaults to `30000` (30 seconds). Pass `0` to
            disable timeout.
        env : Union[Dict[str, Union[bool, float, str]], NoneType]
            Specify environment variables that will be visible to the browser. Defaults to `process.env`.
        headless : Union[bool, NoneType]
            Whether to run browser in headless mode. More details for
            [Chromium](https://developers.google.com/web/updates/2017/04/headless-chrome) and
            [Firefox](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Headless_mode). Defaults to `true` unless the
            `devtools` option is `true`.
        devtools : Union[bool, NoneType]
            **Chromium-only** Whether to auto-open a Developer Tools panel for each tab. If this option is `true`, the `headless`
            option will be set `false`.
        proxy : Union[{server: str, bypass: Union[str, NoneType], username: Union[str, NoneType], password: Union[str, NoneType]}, NoneType]
            Network proxy settings.
        downloads_path : Union[pathlib.Path, str, NoneType]
            If specified, accepted downloads are downloaded into this directory. Otherwise, temporary directory is created and is
            deleted when browser is closed. In either case, the downloads are deleted when the browser context they were created in
            is closed.
        slow_mo : Union[float, NoneType]
            Slows down Playwright operations by the specified amount of milliseconds. Useful so that you can see what is going on.
        traces_dir : Union[pathlib.Path, str, NoneType]
            If specified, traces are saved into this directory.
        chromium_sandbox : Union[bool, NoneType]
            Enable Chromium sandboxing. Defaults to `false`.
        firefox_user_prefs : Union[Dict[str, Union[bool, float, str]], NoneType]
            Firefox user preferences. Learn more about the Firefox user preferences at
            [`about:config`](https://support.mozilla.org/en-US/kb/about-config-editor-firefox).
    """
    playwright = sync_playwright().start()
    if browser == 'webkit':
        return playwright.webkit.launch(**kwargs)
    if browser == 'firefox':
        return playwright.firefox.launch(**kwargs)
    else:
        return playwright.chromium.launch(**kwargs)


async def __install_async_playwright(browser='chrome', **kwargs):
    """
   Method to install async playwright browser
   Parameters
       ----------
       browser :  str
           browser name chrome, firefox or webkit by default chrome
       executable_path : Union[pathlib.Path, str, NoneType]
           Path to a browser executable to run instead of the bundled one. If `executablePath` is a relative path, then it is
           resolved relative to the current working directory. Note that Playwright only works with the bundled Chromium, Firefox
           or WebKit, use at your own risk.
       channel : Union[str, NoneType]
           Browser distribution channel.  Supported values are "chrome", "chrome-beta", "chrome-dev", "chrome-canary", "msedge",
           "msedge-beta", "msedge-dev", "msedge-canary". Read more about using
           [Google Chrome and Microsoft Edge](../browsers.md#google-chrome--microsoft-edge).
       args : Union[List[str], NoneType]
           Additional arguments to pass to the browser instance. The list of Chromium flags can be found
           [here](http://peter.sh/experiments/chromium-command-line-switches/).
       ignore_default_args : Union[List[str], bool, NoneType]
           If `true`, Playwright does not pass its own configurations args and only uses the ones from `args`. If an array is
           given, then filters out the given default arguments. Dangerous option; use with care. Defaults to `false`.
       handle_sigint : Union[bool, NoneType]
           Close the browser process on Ctrl-C. Defaults to `true`.
       handle_sigterm : Union[bool, NoneType]
           Close the browser process on SIGTERM. Defaults to `true`.
       handle_sighup : Union[bool, NoneType]
           Close the browser process on SIGHUP. Defaults to `true`.
       timeout : Union[float, NoneType]
           Maximum time in milliseconds to wait for the browser instance to start. Defaults to `30000` (30 seconds). Pass `0` to
           disable timeout.
       env : Union[Dict[str, Union[bool, float, str]], NoneType]
           Specify environment variables that will be visible to the browser. Defaults to `process.env`.
       headless : Union[bool, NoneType]
           Whether to run browser in headless mode. More details for
           [Chromium](https://developers.google.com/web/updates/2017/04/headless-chrome) and
           [Firefox](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Headless_mode). Defaults to `true` unless the
           `devtools` option is `true`.
       devtools : Union[bool, NoneType]
           **Chromium-only** Whether to auto-open a Developer Tools panel for each tab. If this option is `true`, the `headless`
           option will be set `false`.
       proxy : Union[{server: str, bypass: Union[str, NoneType], username: Union[str, NoneType], password: Union[str, NoneType]}, NoneType]
           Network proxy settings.
       downloads_path : Union[pathlib.Path, str, NoneType]
           If specified, accepted downloads are downloaded into this directory. Otherwise, temporary directory is created and is
           deleted when browser is closed. In either case, the downloads are deleted when the browser context they were created in
           is closed.
       slow_mo : Union[float, NoneType]
           Slows down Playwright operations by the specified amount of milliseconds. Useful so that you can see what is going on.
       traces_dir : Union[pathlib.Path, str, NoneType]
           If specified, traces are saved into this directory.
       chromium_sandbox : Union[bool, NoneType]
           Enable Chromium sandboxing. Defaults to `false`.
       firefox_user_prefs : Union[Dict[str, Union[bool, float, str]], NoneType]
           Firefox user preferences. Learn more about the Firefox user preferences at
           [`about:config`](https://support.mozilla.org/en-US/kb/about-config-editor-firefox).
   """
    playwright = await async_playwright().start()
    if browser == 'webkit':
        return await playwright.webkit.launch(**kwargs)
    if browser == 'firefox':
        return await playwright.firefox.launch(**kwargs)
    else:
        return await playwright.chromium.launch(**kwargs)
