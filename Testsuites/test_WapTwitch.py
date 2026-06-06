## System import
import pytest

## Framework import
import GlobalVariable as GlobalVariable
import Common.Web.BaseUICore as BaseUICore
import Features.WapTwitch as WapTwitch

CaseName = "WapTwitch"

@pytest.fixture()
def PrepareTest():
    print("\n[----Running case setup----]\n")
    BaseUICore.InitWAPDriver({"mobile_emulator": "Pixel 7", "result": "1"})
    print("\n[----Running case setup ended----]\n")

    yield

    print("\n[----Running case teardown----]\n")
    BaseUICore.DeinitialWebDriver()
    print("\n[----Running case teardown ended----]\n")

class TestWapTwitch:

    def test_SearchTwitch001(self, PrepareTest):
        ## Enter Twitch Homepage
        WapTwitch.EnterTwitchHomepage({"result": "1"})
        BaseUICore.SleepTime({"seconds": 3, "result": "1"})

        ## Continue with web
        WapTwitch.ClickChooseAppOptions({"option_type": "continue_with_web", "result": "1"})
        BaseUICore.SleepTime({"seconds": 2, "result": "1"})

        ##Go to search page, search for "StarCraft II", scroll down the page, and select the first live stream
        WapTwitch.ClickChooseBottomNav({"nav_type": "search", "result": "1"})
        WapTwitch.SearchTwitch({"keyword": "StarCraft II", "result": "1"})
        BaseUICore.ScrollPage({"scroll_times": 2, "direction": "down", "height": 200, "result": "1"})
        WapTwitch.SelectFirstLiveStream({"result": "1"})
        BaseUICore.PageHasLoaded({"result": "1"})
        BaseUICore.SleepTime({"seconds": 3, "result": "1"})

        ##Take screenshot of the live stream page
        BaseUICore.TakeScreenshot({"file_name": "SearchTwitch001.png", "result": "1"})