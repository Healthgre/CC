import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pythonProject.src.authentication import authentication
from pythonProject.src.variables import telegram_xpath, steam_xpath, banner_xpath, clear_case_inscription_xpath, \
    replenishment_button_xpath, \
    avatar_icon_xpath, container_open_cases_button_xpath, upgrade_button_xpath, \
    contract_button_xpath, telegram_some_inscription_xpath, \
    steam_some_inscription_xpath, upgrade_container_xpath, contract_container_xpath, profile_content_xpath, \
    payment_block_xpath, agreement_link_xpath, agreement_inscription_xpath, questions_link_xpath, \
    questions_inscription_xpath


class Test_004_transfers_I:
    def test_004_transfers_I(self, driver, logout_after_test):
        driver.implicitly_wait(5)
        wait = WebDriverWait(driver, 5)
        # logout(driver)
        driver.find_element(By.XPATH, clear_case_inscription_xpath).click()  # Вернулся на главную страницу.

        """Проверка отображения главной страницы. Проверка отображения баннера."""
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
        time.sleep(2)
        driver.find_element(By.XPATH, clear_case_inscription_xpath).click()  # Вернулся на главную страницу.
        wait.until(
            EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.

        """Проверка перехода с главной страницы на страницу апгрейда."""
        driver.find_element(By.XPATH,
                            upgrade_button_xpath).click()  # Нажать на кнопку "Апгрейд".
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                     upgrade_container_xpath)))  # Ждём контейнер апгрейда.
        driver.find_element(By.XPATH, clear_case_inscription_xpath).click()  # Вернулся на главную страницу.
        wait.until(
            EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.

        """Проверка перехода с главной страницы на страницу контракта."""
        driver.find_element(By.XPATH,
                            contract_button_xpath).click()  # Нажать на кнопку "Контракт".
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                     contract_container_xpath)))  # Ждём сетку-контейнер на странице контракта.
        driver.find_element(By.XPATH, clear_case_inscription_xpath).click()  # Вернулся на главную страницу.
        wait.until(
            EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.

        """Проверка перехода с главной страницы на страницу Телеграмм и Стим."""
        driver.find_element(By.XPATH, telegram_xpath).click()  # Нажал на кнопку Телеграм в хедере.
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, telegram_some_inscription_xpath)))  # Ждём отображения страницы Телеграма.
        driver.back()
        wait.until(
            EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.
        driver.find_element(By.XPATH, steam_xpath).click()  # Нажал на кнопку Стим в хедере.
        wait.until(
            EC.visibility_of_element_located((By.XPATH,
                                              steam_some_inscription_xpath)))  # Ждём отображения страницы Стим.
        driver.back()
        wait.until(
            EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.

        """Авторизовался с помошью куки."""
        authentication(driver)

        """Проверка перехода c главной страницы на страницу пользователя."""
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                     avatar_icon_xpath)))  # Дождался аватарку.
        driver.find_element(By.XPATH, avatar_icon_xpath).click()  # Аватарка профиля в хедере.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, profile_content_xpath)))  # Дождался появления контента профиля.
        driver.find_element(By.XPATH, clear_case_inscription_xpath).click()  # Вернулся на главную страницу.
        wait.until(
            EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.

        """Проверка перехода с главной страницы на страницу пополнения счёта."""
        driver.find_element(By.XPATH, replenishment_button_xpath).click()  # Перешёл на страницу пополнения счёта.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             payment_block_xpath)))  # Дождался появления, блока пополнения".
        driver.find_element(By.XPATH, clear_case_inscription_xpath).click()  # Вернулся на главную страницу.
        wait.until(
            EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.

        """Проверка перехода с главной страницы на страницу пользовательского соглашения"""
        driver.find_element(By.XPATH, agreement_link_xpath).click()  # Перешёл на страницу пользовательского соглашения.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             agreement_inscription_xpath)))  # Дождался надпись "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ".
        assert driver.find_element(By.XPATH,
                                   agreement_inscription_xpath).text == "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ"  # Выполнил проверку.
        driver.find_element(By.XPATH, clear_case_inscription_xpath).click()  # Вернулся на главную страницу.
        wait.until(
            EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.

        """Проверка перехода с главной страницы на страницу Вопрос - Ответ."""
        driver.find_element(By.XPATH, questions_link_xpath).click()  # Перешёл на страницу Вопрос - Ответ.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             questions_inscription_xpath)))  # Дождался надпись "Часто задаваемые вопросы".
        assert driver.find_element(By.XPATH,
                                   questions_inscription_xpath).text == "ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ"  # Выполнил проверку.
