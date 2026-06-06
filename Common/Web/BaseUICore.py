## System imports
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

## Framework import
import GlobalVariable as GlobalVariable
import FrameworkBase as FrameworkBase

_Webdriver_ = ""
STANDARD_WAIT_TIME = 10
LONG_WAIT_TIME = 30


def InitWAPDriver(arg):
    '''
        InitWAPDriver: Initialize the WebDriver for WAP testing
            Args:
                mobile_emulator: Mobile device to emulate (e.g., "iPhone X", "Pixel 2")
    '''
    ret = 1
    global _Webdriver_
    mobile_emulator = arg["mobile_emulator"]
    mobile_emulation = {"deviceName": mobile_emulator}

    ## Initialize WebDriver with mobile emulation (incognito mode, disable cache, start maximized, disable web security, and set user agent)
    try:
        driver_path = ChromeDriverManager().install()
        service = Service(executable_path=driver_path)
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--diable-cache")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-web-security")
        options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 ")
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        _Webdriver_ = webdriver.Chrome(service=service,options = options)

    except WebDriverException:
        ret = 0
        GlobalVariable._Logger_.exception("Encounter webdriver exception")
    except Exception as e:
        ret = -1
        GlobalVariable._Logger_.exception(e)

    FrameworkBase.OK(ret, int(arg["result"]), "BaseUICore.InitWAPDriver")

def DeinitialWebDriver():
    '''
        DeinitialWebDriver: Quit the WebDriver
    '''
    ret = 1
    global _Webdriver_

    ## Quit WebDriver
    try:
        if _Webdriver_:
            _Webdriver_.quit()
            _Webdriver_ = ""
    except WebDriverException:
        ret = 0
        GlobalVariable._Logger_.exception("Encounter webdriver exception")
    except Exception as e:
        ret = -1
        GlobalVariable._Logger_.exception(e)

    FrameworkBase.OK(ret, 1, "BaseUICore.DeinitialWebDriver")

def SleepTime(arg):
    '''
        SleepTime: Sleep for a specified amount of time
            Args:
                seconds: The number of seconds to sleep
    '''
    ret = 1
    seconds = arg["seconds"]

    try:
        time.sleep(int(seconds))
    except Exception as e:
        ret = -1
        GlobalVariable._Logger_.exception(e)

    FrameworkBase.OK(ret, int(arg["result"]), "BaseUICore.SleepTime")

def RedirectToURL(arg):
    '''
        RedirectToURL: Redirect the WebDriver to a specified URL
            Args:
                url: The URL to redirect to
    '''
    ret = 1
    url = arg["url"]

    ## Redirect to specified URL
    try:
        _Webdriver_.get(url)
    except WebDriverException:
        ret = 0
        GlobalVariable._Logger_.exception("Encounter webdriver exception")
    except Exception as e:
        ret = -1
        GlobalVariable._Logger_.exception(e)

    FrameworkBase.OK(ret, int(arg["result"]), "BaseUICore.RedirectToURL")

def Click(arg):
    '''
        Click: Click an element specified by a locator
            Args:
                locate: The xpath of the element to click (e.g., "id=submit-button", "xpath=//button[@type='submit']")
    '''
    ret = 1
    locate = arg["locate"]

    ## Use xpath  as always
    try:
        WebDriverWait(_Webdriver_, STANDARD_WAIT_TIME).until(EC.presence_of_element_located((By.XPATH, locate))).click()
    except TimeoutException:
        ret = 0
        GlobalVariable._Logger_.exception("Element not found within the standard wait time")
    except WebDriverException:
        ret = 0
        GlobalVariable._Logger_.exception("Encounter webdriver exception")
    except Exception as e:
        ret = -1
        GlobalVariable._Logger_.exception(e)

    FrameworkBase.OK(ret, int(arg["result"]), "BaseUICore.Click")

def Input(arg):
    '''
        Input: Input text into an element specified by a locator.
            Args:
                locate: The xpath of the element to input text into
                text: The text to input
    '''
    ret = 1
    locate = arg["locate"]
    text = arg["text"]

    ## Use xpath  as always
    try:
        WebDriverWait(_Webdriver_, STANDARD_WAIT_TIME).until(EC.presence_of_element_located((By.XPATH, locate))).send_keys(text)
    except TimeoutException:
        ret = 0
        GlobalVariable._Logger_.exception("Element not found within the standard wait time")
    except WebDriverException:
        ret = 0
        GlobalVariable._Logger_.exception("Encounter webdriver exception")
    except Exception as e:
        ret = -1
        GlobalVariable._Logger_.exception(e)

    FrameworkBase.OK(ret, int(arg["result"]), "BaseUICore.Input")

def CheckElementExist(arg):
    '''
        CheckElementExist: Check if an element specified by a locator exists on the page
            Args:
                locate: The xpath of the element to check for existence
                passok: Whether to enter OK function or return the result (1 for OK function, 0 for return)
    '''
    ret = 1
    locate = arg["locate"]
    passok = arg["passok"]

    ## Use xpath  as always
    try:
        WebDriverWait(_Webdriver_, STANDARD_WAIT_TIME).until(EC.presence_of_element_located((By.XPATH, locate)))
    except TimeoutException:
        ret = 0
        GlobalVariable._Logger_.exception("Element not found within the standard wait time")
    except WebDriverException:
        ret = 0
        GlobalVariable._Logger_.exception("Encounter webdriver exception")
    except Exception as e:
        ret = -1
        GlobalVariable._Logger_.exception(e)
    
    if int(passok) == 1:
        FrameworkBase.OK(ret, int(arg["result"]), "BaseUICore.CheckElementExist")
    else:
        return ret


def ScrollPage(arg):
    '''
        ScrollPage: Scroll the page to a specific height and direction
            Args:
                scroll_times: The number of times to scroll
                direction: The direction to scroll ("up" or "down")
                height: The height to scroll to
    '''
    ret = 1
    scroll_times = arg["scroll_times"]
    direction = arg["direction"]
    height = arg["height"]

    try:
        for i in range(int(scroll_times)):
            if direction == "up":
                _Webdriver_.execute_script(f"window.scrollTo(0, {int(height) * -1});")
            elif direction == "down":
                _Webdriver_.execute_script(f"window.scrollTo(0, {height});")
    except WebDriverException:
        ret = 0
        GlobalVariable._Logger_.exception("Encounter webdriver exception")
    except Exception as e:
        ret = -1
        GlobalVariable._Logger_.exception(e)

    FrameworkBase.OK(ret, int(arg["result"]), "BaseUICore.ScrollPage")

def PageHasLoaded(arg):
    '''
        PageHasLoaded: Check if the page has fully loaded by waiting for the document.readyState to be "complete"
    '''
    ret = 1

    try:
        WebDriverWait(_Webdriver_, LONG_WAIT_TIME).until(lambda driver: driver.execute_script("return document.readyState") == "complete")
    except TimeoutException:
        ret = 0
        GlobalVariable._Logger_.exception("Page did not load within the long wait time")
    except WebDriverException:
        ret = 0
        GlobalVariable._Logger_.exception("Encounter webdriver exception")
    except Exception as e:
        ret = -1
        GlobalVariable._Logger_.exception(e)

    FrameworkBase.OK(ret, int(arg["result"]), "BaseUICore.PageHasLoaded")

def SendWindowKey(arg):
    '''
        SendWindowKey: Send a key press event to the window
            Args:
                key: The key to press
    '''
    ret = 1
    key = arg["key"]

    try:
        if key.lower() == "enter":
            ActionChains(_Webdriver_).send_keys(Keys.ENTER).perform()  # "\ue007" is the Unicode code for the Enter key
    except WebDriverException:
        ret = 0
        GlobalVariable._Logger_.exception("Encounter webdriver exception")
    except Exception as e:
        ret = -1
        GlobalVariable._Logger_.exception(e)

    FrameworkBase.OK(ret, int(arg["result"]), "BaseUICore.SendWindowKey")

def TakeScreenshot(arg):
    '''
        TakeScreenshot: Take a screenshot of the current page and save it to a specified path
            Args:
                file_name: The name of the file to save the screenshot (Default path is ..\..\..\Data\Output)
    '''
    ret = 1
    file_name = arg["file_name"]

    try:
        _Webdriver_.save_screenshot(f"./Data/Output/{file_name}")
    except WebDriverException:
        ret = 0
        GlobalVariable._Logger_.exception("Encounter webdriver exception")
    except Exception as e:
        ret = -1
        GlobalVariable._Logger_.exception(e)

    FrameworkBase.OK(ret, int(arg["result"]), "BaseUICore.TakeScreenshot")