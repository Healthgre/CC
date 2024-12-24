import random
import time

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pythonProject.src.variables import balance_xpath, avatar_icon_xpath, clear_case_inscription_xpath, banner_xpath, \
    download_more_button_xpath, any_skin_in_inventory_xpath


class Test_022_case_fast_opening:
    def test_022_case_fast_opening(self, driver, auth, clean_inventory_before_test, clean_inventory_after_test):

        """Ожидания и счётчики"""
        wait = WebDriverWait(driver, 5)
        opened_items_count = 0
        driver.implicitly_wait(5)

        """Выбор кейсов, которые необходимо открыть."""
        first_category_cases_count = len(driver.find_elements(By.XPATH,
                                                              f"//main[@class='page-content']/div[2]/div[2]/button"))  # Высчитал колличество кейсов в первой категории.
        second_category_cases_count = len(driver.find_elements(By.XPATH,
                                                               f"//main[@class='page-content']/div[3]/div[2]/button"))  # Высчитал колличество кейсов во второй категории.

        case_1 = random.randint(1, first_category_cases_count)  # Рандомно выбрал кейс из первой категории.
        case_2 = random.randint(1, second_category_cases_count)  # Рандомно выбрал кейс из второй категории.

        categories = [2, 3]  # Список, который содержит перву и вторую категорию.
        cases = [case_1, case_2]  # Список, который содержит рандомное число из первой и второй категории.

        """Началось открытие кейсов. Внешний цикл."""
        for i, j in zip(categories, cases):
            price = driver.find_element(By.XPATH,
                                        f"//main[@class='page-content']/div[{i}]/div[2]/button[{j}]//div[2]").text  # Взял цену одного открытия кейса.
            price = float(price)

            driver.find_element(By.XPATH,
                                f"//main[@class='page-content']/div[{i}]/div[2]/button[{j}]").click()  # Выбрал кейс.
            wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='control-buttons-container']/button[1]")))

            """Внутренний цикл."""
            for z in range(1, 11):
                balance = float(driver.find_element(By.XPATH, balance_xpath).text)  # Взял баланс.

                """Непосредственно открытие кейсов."""
                time.sleep(1)  # Тупо, но кнопки движутся, надо подождать.
                wait.until(EC.visibility_of_element_located((By.XPATH,
                                                             f"//div[@class='count-boxes-container']/button[{z}]")))  # Дождался переключателя количества скинов.
                driver.find_element(By.XPATH,
                                    f"//div[@class='count-boxes-container']/button[{z}]").click()  # Выбрал сколько скинов открыть за раз.

                time.sleep(1)  # Тупо, но кнопки движутся, надо подождать.
                if z == 1:
                    wait.until(EC.visibility_of_element_located(
                        (By.XPATH,
                         "//div[@class='control-buttons-container']/button[2]")))  # Жду кнопку "Открыть быстро".
                    driver.find_element(By.XPATH,
                                        "//div[@class='control-buttons-container']/button[2]").click()  # Нажал на кнопку "открыть быстро ...".
                else:
                    wait.until(EC.visibility_of_element_located(
                        (By.XPATH,
                         "//div[@class='control-buttons-container']/button[3]")))  # Жду кнопку "Открыть быстро".
                    driver.find_element(By.XPATH,
                                        "//div[@class='control-buttons-container']/button[3]").click()  # Нажал на кнопку "открыть быстро ...".
                opened_items_count += z
                wait.until(EC.visibility_of_element_located(
                    (By.XPATH,
                     "//div[@class='control-buttons-container']/button[3]")))  # Жду кнопку "Открыть быстро".

                balance -= (price * z)  # На каждом круге отнимал от баланса денежку за открытие кейса.
                balance = round(balance, 2)
                assert balance == float(driver.find_element(By.XPATH, balance_xpath).text)

            wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         "//div[@class='control-buttons-container']/button[3]")))  # Жду пока не появится кнопка "открыть быстро".
            driver.find_element(By.XPATH, clear_case_inscription_xpath).click()  # Перешёл на главную страницу.
            wait.until(
                EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Жду баннер.

        """Переход на страницу пользователя."""
        driver.find_element(By.XPATH, avatar_icon_xpath).click()  # Перешёл на страницу пользователя.

        while True:
            try:
                xpath_more_button = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                                   download_more_button_xpath)))  # Нажимаю на кнопку "Загрузить ещё".
                xpath_more_button.click()
                wait.until(
                    EC.visibility_of_element_located((By.XPATH, download_more_button_xpath)))
                time.sleep(1)  # Но иначе крашится.
            except (NoSuchElementException, TimeoutException):
                break

        wait.until(EC.invisibility_of_element(
            (By.XPATH, download_more_button_xpath)))  # Дождался пока кнопка "Загрузить ещё" не исчезла.

        # time.sleep(3)  # Тупо. если не дать подождать, неправильно считает количество скинов.
        skins_in_inventory = len(driver.find_elements(By.XPATH, any_skin_in_inventory_xpath))

        assert skins_in_inventory == opened_items_count
