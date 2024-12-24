from pythonProject.src.variables import token


def authentication(driver):
    driver.add_cookie({"name": 'token',
                       "value": token})
