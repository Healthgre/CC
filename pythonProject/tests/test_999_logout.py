import time

from selenium.webdriver.common.by import By

from pythonProject.src.variables import login_through_inscription_xpath
from pythonProject.tests.conftest import logout


class Test_999_logout:
    def test_999_logout(self, driver, auth):

        time.sleep(1)
        logout(driver)

        login_inscription = driver.find_element(By.XPATH,
                                                login_through_inscription_xpath).text  # Проверка налиичя надписи "Войти через".
        assert login_inscription == "Войти через"  # и кнопок авторизации через Стим и Телеграмм.
        assert driver.find_element(By.ID, "tg-auth")
        assert driver.find_element(By.ID, "steam-auth")
