import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pythonProject.src.variables import balance_xpath, clear_case_inscription_xpath, \
    avatar_icon_xpath, banner_xpath


class Test_021_case_opening:
    def test_021_case_opening(self, driver, auth, clean_inventory_before_test, clean_inventory_after_test):

        """Ожидание и флаги."""
        driver.implicitly_wait(5)
        wait = WebDriverWait(driver, 5)
        animation_wait = WebDriverWait(driver, 20)

        opened_items_count = 0

        """Высчет количества кейсов"""
        first_category_cases_count = len(driver.find_elements(By.XPATH,
                                                              f"//main[@class='page-content']/div[2]/div[2]/button"))  # Высчитал колличество кейсов в первой категории.
        second_category_cases_count = len(driver.find_elements(By.XPATH,
                                                               f"//main[@class='page-content']/div[3]/div[2]/button"))  # Высчитал колличество кейсов во второй категории.

        case_1 = random.randint(1, first_category_cases_count)  # Рандомно выбрал кейс из первой категории.
        case_2 = random.randint(1, second_category_cases_count)  # Рандомно выбрал кейс из второй категории.

        categories = [2, 3]  # Список, который содержит перву и вторую категорию.
        cases = [case_1, case_2]  # Список, который содержит рандомное число из первой и второй категории.

        """Внешний цикл. Кейс."""
        for i, j in zip(categories, cases):
            driver.find_element(By.XPATH,
                                f"//main[@class='page-content']/div[{i}]/div[2]/button[{j}]").click()  # Выбрал кейс.
            price = driver.find_element(By.XPATH, f"//main[@class='page-content']/div[{i}]/div[2]/button[{j}]//div[2]").text  # Взял цену одного открытия кейса.
            price = float(price)


            """Внутренний цикл."""
            for z in range(1, 4):

                balance = float(driver.find_element(By.XPATH, balance_xpath).text)  # Взял баланс.
                time.sleep(1)

                """Выбор количества открыйий."""
                wait.until(EC.visibility_of_element_located((By.XPATH,
                                                             "//div[@class='count-boxes-container']")))  # Дождался переключателя количства открытий.
                driver.find_element(By.XPATH,
                                    f"//div[@class='count-boxes-container']/button[{z}]").click()  # Выбрал сколько скинов открыть за раз.
                if z == 1:
                    animation_wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                           "//div[@class='control-buttons-container']/button[1]")))  # Жду кнопку "открыть за ...".
                    driver.find_element(By.XPATH,
                                        "//div[@class='control-buttons-container']/button[1]").click()  # Нажал на кнопку "открыть за ...".
                else:
                    animation_wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                           "//div[@class='control-buttons-container']/button[2]")))  # Жду кнопку "открыть за ...".
                    driver.find_element(By.XPATH,
                                        "//div[@class='control-buttons-container']/button[2]").click()  # Нажал на кнопку "открыть за ...".

                """Подсчёт круток и новый баланс."""
                animation_wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                       "//div[@class='control-buttons-container']/button[2]")))  # Жду кнопку "открыть за ...".
                opened_items_count += z  # Веду подсчёт открытий кейсов.
                animation_wait.until(EC.visibility_of_element_located(
                    (By.XPATH,
                     "//div[@class='control-buttons-container']/button[2]")))  # Жду кнопку "открыть за ...".
                new_balance = float(driver.find_element(By.XPATH, balance_xpath).text)  # Взял новый баланс.

                """Сравнение баланса после каждой крутки."""
                animation_wait.until(EC.visibility_of_element_located(
                    (By.XPATH,
                     "//div[@class='control-buttons-container']/button[2]")))  # Жду кнопку "открыть за ...".
                assert new_balance == (balance - (price * z))  # Сравнение балансов.

            animation_wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                   "//div[@class='control-buttons-container']/button[2]")))  # Жду кнопку "открыть за ...".
            driver.find_element(By.XPATH, clear_case_inscription_xpath).click()  # Перешёл на главную страницу.
        wait.until(
            EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.
        driver.find_element(By.XPATH, avatar_icon_xpath).click()  # Перешёл на страницу пользователя.

        count_skins_in_inventory = len(
            driver.find_elements(By.XPATH,
                                 "//div[@class= 'default-inventory-container']/div"))  # Взял колличество скинов в инвентаре.

        assert opened_items_count == count_skins_in_inventory
