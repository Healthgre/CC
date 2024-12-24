import random

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pythonProject.src.authentication import authentication
from pythonProject.src.logout import logout
from pythonProject.src.variables import telegram_xpath, steam_xpath, cases_button_xpath, \
    banner_xpath, clear_case_inscription_xpath, replenishment_button_xpath, \
    avatar_icon_xpath, container_open_cases_button_xpath, upgrade_button_xpath, \
    contract_button_xpath, telegram_some_inscription_xpath, \
    steam_some_inscription_xpath, upgrade_container_xpath, contract_container_xpath, profile_content_xpath, \
    payment_block_xpath, agreement_link_xpath, agreement_inscription_xpath, questions_link_xpath, \
    questions_inscription_xpath, telegram_case_xpath, steam_case_xpath



# Из-за того что тут одна сессия при проверки кнопок захода в телегу или стим происходит авторизация.
# Надо if прописать. Из-за этого падают тесты: II, III, IV и VII с VIII упадут без if.
class Test_005_transfers_II:
    def test_005_transfers_II(self, driver, logout_after_test):
        driver.implicitly_wait(5)
        wait = WebDriverWait(driver, 5)

        """Проверка отображения Выбранного кейса."""
        driver.find_element(By.XPATH, clear_case_inscription_xpath).click()  # Вернулся на главную страницу.
        wait.until(
            EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.

        """Проверка перехода с главной страницы на страницу кейса."""
        i = random.randint(2, 3)  # Категория 1 или 2.
        j = random.randint(1, 10)  # Количество кейсов I категории.
        z = random.randint(1, 40)  # Количество кейсов II категории.
        if i == 2:
            pass
        else:
            j = z

        selected_case = f"//main[@class='page-content']/div[{i}]/div[2]/button[{j}]"
        driver.find_element(By.XPATH,
                            selected_case).click()  # Открыл выбранный кейс.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, container_open_cases_button_xpath)))  # Ждём кнопкИ открытия кейса.

        """Проверка перехода из открытого кейса  на главную страницу."""
        driver.find_element(By.XPATH, cases_button_xpath).click()  # Вернулся на главную страницу.
        wait.until(
            EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.
        driver.find_element(By.XPATH,
                            selected_case).click()  # Открыл выбранный кейс.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, container_open_cases_button_xpath)))  # Ждём кнопкИ открытия кейса.

        """Проверка перехода из открытого кейса  на страницу апгрейда."""
        driver.find_element(By.XPATH,
                            upgrade_button_xpath).click()  # Нажать на кнопку "Апгрейд".
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                     upgrade_container_xpath)))  # Ждём контейнер апгрейда.
        driver.find_element(By.XPATH, cases_button_xpath).click()  # Вернулся на главную страницу.
        wait.until(
            EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.
        driver.find_element(By.XPATH,
                            selected_case).click()  # Открыл выбранный кейс.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, container_open_cases_button_xpath)))  # Ждём кнопкИ открытия кейса.

        """Проверка перехода из открытого кейса  на страницу контракта."""
        driver.find_element(By.XPATH,
                            contract_button_xpath).click()  # Нажать на кнопку "Контракт".
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                     contract_container_xpath)))  # Ждём сетку-контейнер на странице контракта.
        driver.find_element(By.XPATH, clear_case_inscription_xpath).click()  # Вернулся на главную страницу.
        wait.until(
            EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.
        driver.find_element(By.XPATH,
                            selected_case).click()  # Открыл выбранный кейс.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, container_open_cases_button_xpath)))  # Ждём кнопкИ открытия кейса.

        """Проверка перехода из открытого кейса на страницу Телеграмм и Стим."""
        try:
            driver.find_element(By.XPATH, telegram_xpath).click()  # Нажал на кнопку Телеграм в хедере.
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, telegram_some_inscription_xpath)))  # Ждём отображения страницы Телеграма.
            driver.back()
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, container_open_cases_button_xpath)))  # Ждём кнопкИ открытия кейса.
        except NoSuchElementException:
            logout(driver)
            wait.until(
                EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.
            driver.find_element(By.XPATH,
                                selected_case).click()  # Открыл выбранный кейс.
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, container_open_cases_button_xpath)))  # Ждём кнопкИ открытия кейса.

        try:
            driver.find_element(By.XPATH, steam_xpath).click()  # Нажал на кнопку Стим в хедере.
            wait.until(
                EC.visibility_of_element_located((By.XPATH,
                                                  steam_some_inscription_xpath)))  # Ждём отображения страницы Стим.
            driver.back()
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, container_open_cases_button_xpath)))  # Ждём кнопкИ открытия кейса.
        except NoSuchElementException:
            logout(driver)
            wait.until(
                EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.
            driver.find_element(By.XPATH,
                                selected_case).click()  # Открыл выбранный кейс.
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, container_open_cases_button_xpath)))  # Ждём кнопкИ открытия кейса.
        try:
            driver.find_element(By.XPATH,
                                telegram_case_xpath).click()  # Нажал на кнопку входа в Телеграм со страницы кейса.
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, telegram_some_inscription_xpath)))  # Ждём отображения страницы Телеграма.
            driver.back()
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, container_open_cases_button_xpath)))  # Ждём кнопкИ открытия кейса.
        except NoSuchElementException:
            logout(driver)
            wait.until(
                EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.
            driver.find_element(By.XPATH,
                                selected_case).click()  # Открыл выбранный кейс.
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, container_open_cases_button_xpath)))  # Ждём кнопкИ открытия кейса.

        try:
            driver.find_element(By.XPATH, steam_case_xpath).click()  # Нажал на кнопку входа в Стим со страницы кейса.
            wait.until(
                EC.visibility_of_element_located((By.XPATH,
                                                  steam_some_inscription_xpath)))  # Ждём отображения страницы Стим.
            driver.back()
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, container_open_cases_button_xpath)))  # Ждём кнопкИ открытия кейса.
        except NoSuchElementException:
            logout(driver)
            wait.until(
                EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.
            driver.find_element(By.XPATH,
                                selected_case).click()  # Открыл выбранный кейс.
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, container_open_cases_button_xpath)))  # Ждём кнопкИ открытия кейса.

        """Авторизовался с помошью куки."""
        authentication(driver)

        """Проверка перехода из открытого кейса на страницу пользователя."""
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                     avatar_icon_xpath)))  # Дождался аватарку.
        driver.find_element(By.XPATH, avatar_icon_xpath).click()  # Аватарка профиля в хедере.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, profile_content_xpath)))  # Дождался появления контента профиля.
        driver.find_element(By.XPATH, clear_case_inscription_xpath).click()  # Вернулся на главную страницу.
        wait.until(
            EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.
        driver.find_element(By.XPATH,
                            selected_case).click()  # Открыл выбранный кейс.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, container_open_cases_button_xpath)))  # Ждём кнопкИ открытия кейса.

        """Проверка перехода из открытого кейса на страницу пополнения счёта."""
        driver.find_element(By.XPATH, replenishment_button_xpath).click()  # Перешёл на страницу пополнения счёта.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             payment_block_xpath)))  # Дождался появления, блока пополнения".
        driver.find_element(By.XPATH, clear_case_inscription_xpath).click()  # Вернулся на главную страницу.
        wait.until(
            EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.
        driver.find_element(By.XPATH,
                            selected_case).click()  # Открыл выбранный кейс.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, container_open_cases_button_xpath)))  # Ждём кнопкИ открытия кейса.

        """Проверка перехода из открытого кейса на страницу пользовательского соглашения."""
        driver.find_element(By.XPATH, agreement_link_xpath).click()  # Перешёл на страницу пользовательского соглашения.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             agreement_inscription_xpath)))  # Дождался надпись "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ".
        assert driver.find_element(By.XPATH,
                                   agreement_inscription_xpath).text == "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ"  # Выполнил проверку.
        driver.find_element(By.XPATH, clear_case_inscription_xpath).click()  # Вернулся на главную страницу.
        wait.until(
            EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.
        driver.find_element(By.XPATH,
                            selected_case).click()  # Открыл выбранный кейс.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, container_open_cases_button_xpath)))  # Ждём кнопкИ открытия кейса.

        """Проверка перехода из открытого кейса на страницу Вопрос - Ответ."""
        driver.find_element(By.XPATH, questions_link_xpath).click()  # Перешёл на страницу Вопрос - Ответ.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             questions_inscription_xpath)))  # Дождался надпись "Часто задаваемые вопросы".
        assert driver.find_element(By.XPATH,
                                   questions_inscription_xpath).text == "ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ"  # Выполнил проверку.