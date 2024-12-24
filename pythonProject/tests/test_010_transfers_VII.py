from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pythonProject.src.logout import logout
from pythonProject.src.variables import banner_xpath, clear_case_inscription_xpath, avatar_icon_xpath, \
    upgrade_button_xpath, \
    contract_button_xpath, upgrade_container_xpath, contract_container_xpath, profile_content_xpath, \
    agreement_link_xpath, agreement_inscription_xpath, questions_link_xpath, \
    questions_inscription_xpath, telegram_xpath, telegram_some_inscription_xpath, steam_xpath, \
    steam_some_inscription_xpath, replenishment_button_xpath, payment_block_xpath
from pythonProject.tests.conftest import authentication


class Test_010_transfers_VII:
    def test_010_transfers_VII(self, driver, logout_after_test):
        driver.implicitly_wait(5)
        wait = WebDriverWait(driver, 5)

        """Проверка отобажения страницы пользовательского соглашения."""
        driver.find_element(By.XPATH, agreement_link_xpath).click()  # Перешёл на страницу пользовательского соглашения.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             agreement_inscription_xpath)))  # Дождался надпись "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ".
        assert driver.find_element(By.XPATH,
                                   agreement_inscription_xpath).text == "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ"  # Выполнил проверку.

        """Проверка перехода со страницы пользовательского соглашения на главную страницу."""
        driver.find_element(By.XPATH, clear_case_inscription_xpath).click()  # Вернулся на главную страницу.
        wait.until(
            EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Ждём баннер.
        driver.find_element(By.XPATH, agreement_link_xpath).click()  # Перешёл на страницу пользовательского соглашения.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             agreement_inscription_xpath)))  # Дождался надпись "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ".
        assert driver.find_element(By.XPATH,
                                   agreement_inscription_xpath).text == "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ"  # Выполнил проверку.

        """Проверка перехода со страницы пользовательского соглашения на страницу апгрейда."""
        driver.find_element(By.XPATH,
                            upgrade_button_xpath).click()  # Нажать на кнопку "Апгрейд".
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                     upgrade_container_xpath)))  # Ждём контейнер апгрейда.
        driver.find_element(By.XPATH, agreement_link_xpath).click()  # Перешёл на страницу пользовательского соглашения.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             agreement_inscription_xpath)))  # Дождался надпись "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ".
        assert driver.find_element(By.XPATH,
                                   agreement_inscription_xpath).text == "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ"  # Выполнил проверку.

        """Проверка перехода со страницы пользовательского соглашения на страницу контракта."""
        driver.find_element(By.XPATH,
                            contract_button_xpath).click()  # Нажать на кнопку "Контракт".
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                     contract_container_xpath)))  # Ждём сетку-контейнер на странице контракта.
        driver.find_element(By.XPATH, agreement_link_xpath).click()  # Перешёл на страницу пользовательского соглашения.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             agreement_inscription_xpath)))  # Дождался надпись "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ".
        assert driver.find_element(By.XPATH,
                                   agreement_inscription_xpath).text == "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ"  # Выполнил проверку.

        """Проверка перехода со страницы пользовательского соглашения на страницу Телеграмм и Стим."""
        try:
            driver.find_element(By.XPATH, telegram_xpath).click()  # Нажал на кнопку Телеграм в хедере.
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, telegram_some_inscription_xpath)))  # Ждём отображения страницы Телеграма.
            driver.back()
            driver.find_element(By.XPATH, agreement_link_xpath).click()  # Перешёл на страницу пользовательского соглашения.
            wait.until(EC.visibility_of_element_located(
                (By.XPATH,
                 agreement_inscription_xpath)))  # Дождался надпись "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ".
            assert driver.find_element(By.XPATH,
                                       agreement_inscription_xpath).text == "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ"  # Выполнил проверку.
        except NoSuchElementException:
            logout(driver)
            driver.find_element(By.XPATH,
                                agreement_link_xpath).click()  # Перешёл на страницу пользовательского соглашения.
            wait.until(EC.visibility_of_element_located(
                (By.XPATH,
                 agreement_inscription_xpath)))  # Дождался надпись "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ".
            assert driver.find_element(By.XPATH,
                                       agreement_inscription_xpath).text == "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ"  # Выполнил проверку.
        try:
            driver.find_element(By.XPATH, steam_xpath).click()  # Нажал на кнопку Стим в хедере.
            wait.until(
                EC.visibility_of_element_located((By.XPATH,
                                                  steam_some_inscription_xpath)))  # Ждём отображения страницы Стим.
            driver.back()
            driver.find_element(By.XPATH, agreement_link_xpath).click()  # Перешёл на страницу пользовательского соглашения.
            wait.until(EC.visibility_of_element_located(
                (By.XPATH,
                 agreement_inscription_xpath)))  # Дождался надпись "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ".
            assert driver.find_element(By.XPATH,
                                       agreement_inscription_xpath).text == "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ"  # Выполнил проверку.
        except NoSuchElementException:
            logout(driver)
            driver.find_element(By.XPATH,
                                agreement_link_xpath).click()  # Перешёл на страницу пользовательского соглашения.
            wait.until(EC.visibility_of_element_located(
                (By.XPATH,
                 agreement_inscription_xpath)))  # Дождался надпись "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ".
            assert driver.find_element(By.XPATH,
                                       agreement_inscription_xpath).text == "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ"  # Выполнил проверку.

        """Авторизовался с помошью куки."""
        authentication(driver)

        """Проверка перехода со страницы пользовательского соглашения на страницу пользователя."""
        driver.find_element(By.XPATH, avatar_icon_xpath).click()  # Аватарка профиля в хедере.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, profile_content_xpath)))  # Дождался появления контента профиля.
        driver.find_element(By.XPATH, agreement_link_xpath).click()  # Перешёл на страницу пользовательского соглашения.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             agreement_inscription_xpath)))  # Дождался надпись "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ".
        assert driver.find_element(By.XPATH,
                                   agreement_inscription_xpath).text == "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ"  # Выполнил проверку.

        """Проверка перехода со страницы пользовательского соглашения на страницу пополнения счёта."""
        driver.find_element(By.XPATH, replenishment_button_xpath).click()  # Перешёл на страницу пополнения счёта.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             payment_block_xpath)))  # Дождался появления, блока пополнения".
        driver.find_element(By.XPATH, agreement_link_xpath).click()  # Перешёл на страницу пользовательского соглашения.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             agreement_inscription_xpath)))  # Дождался надпись "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ".
        assert driver.find_element(By.XPATH,
                                   agreement_inscription_xpath).text == "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ"  # Выполнил проверку.

        """Проверка перехода со пользовательского соглашения на страницу Вопрос - Ответ."""
        driver.find_element(By.XPATH, questions_link_xpath).click()  # Перешёл на страницу Вопрос - Ответ.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             questions_inscription_xpath)))  # Дождался надпись "Часто задаваемые вопросы".
        assert driver.find_element(By.XPATH,
                                   questions_inscription_xpath).text == "ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ"  # Выполнил проверку.
