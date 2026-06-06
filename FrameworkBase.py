import json

## Framework import
import GlobalVariable

def ImportXpath(arg):
    '''
        ImportXpath: Import xpath.json and read specific dict based on file_name
            Args:
                file_name: Load specific dict in Json file
    '''
    ret = 1
    file_name = arg["file_name"]

    ## Load xpath from JSON file and store in global variables
    try:
        with open(f"Data\Xpath.json", "r") as file:
            xpath_data = json.load(file)
            return xpath_data[file_name]
    except Exception as e:
        ret = -1
        GlobalVariable._Logger_.exception(e)


def OK(actual_result, expect_result, message = ""):
    if actual_result == expect_result:
        print(f"[OK, {actual_result} == {expect_result}] {message}")
        GlobalVariable._Logger_.info(f"[OK, {actual_result} == {expect_result}] {message}")
        assert True
    else:
        print(f"[Fail, {actual_result} != {expect_result}] {message}")
        GlobalVariable._Logger_.error(f"[Fail, {actual_result} != {expect_result}] {message}")
        assert False

