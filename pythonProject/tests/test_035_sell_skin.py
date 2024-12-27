import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pythonProject.src.variables import avatar_icon_xpath, balance_xpath, select_all_button_xpath, button_history_xpath, \
    any_skin_in_inventory_xpath, head_message_xpath


class Test_035_sell_skin:
    def test_035_sell_skin(self, driver, auth, clean_inventory_before_test, get_skin_to_the_inventory_1):
        """Дождался элементов страницы пользователя и взял данные со страницы пользователя."""
        driver.find_element(By.XPATH, avatar_icon_xpath).click()  # Перешёл на страницу пользователя.

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                     any_skin_in_inventory_xpath)))  # Дождался появления скина в инвентаре.
        balance = float(driver.find_element(By.XPATH, balance_xpath).text)  # Взял баланс.
        price = float(driver.find_element(By.XPATH,
                                          "//div[@class='default-inventory-container']/div[1]/div/div/div/div[2]/div").text)  # Взял цену первого скина.
        name = driver.find_element(By.XPATH,
                                   "//div[@class='default-inventory-container']/div[1]/div/div/div[2]/div/div").text  # Взял имя первого скина.
        bal_pl_pri = round(balance + price, 2)  # Посчитал сумму баланся и цены скина.

        driver.find_element(By.XPATH,
                            "//div[@class='action-panel-container z-50']/button[2]").click()  # Выполнил продажу.

        # """Продажа скина и проверки."""
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                     head_message_xpath)))  # Дождался заголовок всплывающего сообщения.
        assert driver.find_element(By.XPATH,
                                   "//div[@class=' w-full h-full  px-[10px] pb-[6px] pt-[4px]']/div[1]/h3").text == "Успешная продажа"  # Проверка уведомления об успешной продаже скина.
        price = str(price)
        if price[-2] == ".":
            price = f"{price}0"

        assert driver.find_element(By.XPATH,
                                   "//div[@class=' w-full h-full  px-[10px] pb-[6px] pt-[4px]']/div[2]/p").text == f"Предмет продан за {price}"  # Проверка уведомления о том что предмет был продан за определённую цену.
        wait.until(EC.invisibility_of_element((By.XPATH,
                                               head_message_xpath)))  # Дождался исчезовения заголова всплывающего сообщения.
        assert float(driver.find_element(By.XPATH,
                                         balance_xpath).text) == bal_pl_pri  # Проверил, что баланс в хедере равен Старому балансу + цена скина, который продаем.

        """Переход в раздел истории и проверка."""
        driver.find_element(By.XPATH, button_history_xpath).click()  # Перешёл в раздел истории.
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             "//div[@class='default-inventory-container']/div[1]/div/div/div[1]/div[2]/div[1]")))  # Дождался появления цены первого проданного скина в истории.

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='default-inventory-container']/div[1]/div/div/div[2]/div[1]/div[1]")))
        name_in_inventory = driver.find_element(By.XPATH,
                                                "//div[@class='default-inventory-container']/div[1]/div/div/div[2]/div[1]/div[1]").text
        assert name_in_inventory == name

        # Не могу затестить если закомменченое, если цена скина заканчивается на нолик (копейки).
