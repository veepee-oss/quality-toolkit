"""
All methods link to the ui
"""
from selenium import webdriver
from selenium.webdriver.opera import options as opera_options


def install_chrome_driver(context):
    """
    Method to install webdriver for chrome
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    if context.config.userdata['browser_headless'] == 'true':
        options.add_argument("--headless")
    return webdriver.Remote(context.config.userdata['browser_url'], options=options)


def install_firefox_driver(context):
    """
    Method to install webdriver for firefox
    """
    options = webdriver.FirefoxOptions()
    if context.config.userdata['browser_headless'] == 'true':
        options.add_argument("--headless")
    return webdriver.Remote(context.config.userdata['browser_url'], options=options)


def install_opera_driver(context):
    """
    Method to install webdriver for Opera
    """
    options = opera_options.Options()
    return webdriver.Remote(context.config.userdata['browser_url'], options=options)


def install_edge_driver(context):
    """
    Method to install webdriver for Edge
    """
    cap = {'browserName': 'MicrosoftEdge'}
    return webdriver.Remote(context.config.userdata['browser_url'], desired_capabilities=cap)
