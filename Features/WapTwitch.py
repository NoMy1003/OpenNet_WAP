## Framework import
import GlobalVariable as GlobalVariable
import FrameworkBase as FrameworkBase
import Common.Web.BaseUICore as BaseUICore

## Initialize json data used for this feature
file_name = "WapTwitch"
xpath_data = FrameworkBase.ImportXpath({"file_name": file_name, "result": 1})

def EnterTwitchHomepage(arg):
    '''
        EnterTwitchHomepage: Enter the Twitch homepage
            Args:
                N/A
    '''
    ret = 1
    url = "https://www.twitch.tv"

    ## Redirect to Twitch homepage
    BaseUICore.RedirectToURL({"url": url, "result": 1})
    BaseUICore.PageHasLoaded({"result": 1})

    FrameworkBase.OK(ret, int(arg["result"]), "WapTwitch.EnterTwitchHomepage")

def ClickChooseAppOptions(arg):
    '''
        ClickChooseAppOptions: Click choose app options
            Args:
                option_type - open_app / continue_with_web
    '''
    ret = 1
    option_type = arg["option_type"]

    ## Click choose app options
    if BaseUICore.CheckElementExist({"locate": xpath_data["ClickChooseAppOptions"]["option_layout"], "passok": 0, "result": 1}):
        BaseUICore.Click({"locate": xpath_data["ClickChooseAppOptions"][option_type], "result": 1})

    FrameworkBase.OK(ret, int(arg["result"]), "WapTwitch.ClickChooseAppOptions")

def ClickChooseBottomNav(arg):
    '''
        ClickChooseBottomNav: Click choose button in the bottom navigation bar
            Args:
                nav_type - homepage / search / activities / profile
    '''
    ret = 1
    nav_type = arg["nav_type"]

    ## Click choose button in the bottom navigation bar
    BaseUICore.Click({"locate": xpath_data["ClickChooseBottomNav"][nav_type], "result": 1})

    FrameworkBase.OK(ret, int(arg["result"]), "WapTwitch.ClickChooseBottomNav")

def SearchTwitch(arg):
    '''
        SearchTwitch: Search for a keyword on Twitch
            Args:
                keyword: The keyword to search for
    '''
    ret = 1
    keyword = arg["keyword"]

    ## Input keyword into search box and submit
    BaseUICore.Click({"locate": xpath_data["SearchTwitch"]["search_input"], "result": 1})
    BaseUICore.SleepTime({"seconds": 1, "result": 1})
    BaseUICore.Input({"locate": xpath_data["SearchTwitch"]["search_input"], "text": keyword, "result": 1})
    BaseUICore.SendWindowKey({"key": "enter", "result": 1})
    BaseUICore.PageHasLoaded({"result": 1})

    FrameworkBase.OK(ret, int(arg["result"]), "WapTwitch.SearchTwitch")

def SelectFirstLiveStream(arg):
    '''
        SelectFirstLiveStream: Select the first live stream from the search results
            Args:
                N/A
    '''
    ret = 1

    ## Click the first live stream in the search results
    BaseUICore.Click({"locate": xpath_data["SelectFirstLiveStream"]["first_result"], "result": 1})

    FrameworkBase.OK(ret, int(arg["result"]), "WapTwitch.SelectFirstLiveStream")