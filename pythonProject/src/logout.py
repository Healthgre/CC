import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pythonProject.src.variables import logout_button_xpath, avatar_icon_xpath, login_through_inscription_xpath


def logout(driver):
    wait = WebDriverWait(driver, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, avatar_icon_xpath)))
        driver.get("https://clearcase.net/profile")
        time.sleep(1)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, logout_button_xpath)))  # Дождался кнопку выхода из аккаунта.
        driver.find_element(By.XPATH, logout_button_xpath).click()  # Разлогинились.
        time.sleep(1)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, login_through_inscription_xpath)))  # Ждём надпись "Войти через".
    except Exception:
        pass