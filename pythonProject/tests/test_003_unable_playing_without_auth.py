import random

from selenium.webdriver.common.by import By

from pythonProject.src.variables import clear_case_inscription_xpath, upgrade_button_xpath, contract_button_xpath


class Test_004_unable_playing_without_auth:
    def test_004_unable_playing_without_auth(self, driver):
        driver.implicitly_wait(3)

        first_category_cases_count = len(driver.find_elements(By.XPATH,
                                                              f"//main[@class='page-content']/div[2]/div[2]/button"))  # Высчитал колличество кейсов в первой категории.
        second_category_cases_count = len(driver.find_elements(By.XPATH,
                                                               f"//main[@class='page-content']/div[3]/div[2]/button"))  # Высчитал колличество кейсов во второй категории.

        case_1 = random.randint(1, first_category_cases_count)
        case_2 = random.randint(1, second_category_cases_count)
        categories = [2, 3]
        cases = [case_1, case_2]

        for i, j in zip(categories, cases):
            driver.find_element(By.XPATH,
                                f"//main[@class='page-content']/div[{i}]/div[2]/button[{j}]").click()
            assert driver.find_element(By.XPATH,
                                       "//div[@class='control-buttons-container']/button[1]").text == "Telegram"
            assert driver.find_element(By.XPATH, "//div[@class='control-buttons-container']/button[2]").text == "Steam"

            driver.find_element(By.XPATH, clear_case_inscription_xpath).click()  # Перешёл на главную страницу

        driver.find_element(By.XPATH, upgrade_button_xpath).click()  # Перешёл на страницу апгрейда

        assert driver.find_element(By.XPATH,
                                   "//div[@class='upgrade-inventories-container']/div[1]/div[3]/div/p").text == "Требуется авторизация".upper()
        assert driver.find_element(By.XPATH,
                                   "//div[@class='upgrade-inventories-container']/div[2]/div[3]/div/p").text == "Требуется авторизация".upper()

        driver.find_element(By.XPATH, contract_button_xpath).click()  # Перешёл на страницу контракта

        assert driver.find_element(By.XPATH,
                                   "//p[@class='__className_86079f informer-text h-[170px]']").text == "Требуется авторизация".upper()