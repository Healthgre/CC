from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pythonProject.src.variables import avatar_icon_xpath, banner_xpath, inventory_is_empty_inscription_xpath, \
    cases_button_xpath, select_all_button_xpath, active_sale_button_xpath, any_skin_in_inventory_xpath


def clean(driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, avatar_icon_xpath)))  # Жду появления аватаркми в хедере.
        driver.find_element(By.XPATH,
                            avatar_icon_xpath).click()  # Перешёл на страницу пользователя.

        wait.until(EC.presence_of_element_located(
            (By.XPATH, any_skin_in_inventory_xpath)))  # Первый скин в инвентаре".
        wait_for_empty = WebDriverWait(driver, 2)
        wait_for_empty.until(
            EC.visibility_of_element_located((By.XPATH, select_all_button_xpath)))  # Жду кнопку Выделить всё".
        driver.find_element(By.XPATH, select_all_button_xpath).click()  # Нажал на кнопку Выделить всё".

        wait.until(
            EC.element_to_be_clickable((By.XPATH, active_sale_button_xpath)))  # Жду кликабельность кнопки "Продать".
        driver.find_element(By.XPATH, active_sale_button_xpath).click()  # Нажал активную кнопку "Продать".
        wait.until(EC.presence_of_element_located(
            (By.XPATH, inventory_is_empty_inscription_xpath)))  # Дождался надписи "Инвентарь пуст".

        driver.find_element(By.XPATH,
                            cases_button_xpath).click()  # Нажал кнопку "Кейсы" в хедере.
        wait.until(
            EC.visibility_of_element_located((By.XPATH, banner_xpath)))  # Жду баннер.

    except (NoSuchElementException, TimeoutException):
        driver.find_element(By.XPATH,
                            cases_button_xpath).click()  # Нажал кнопку "Кейсы" в хедере.
