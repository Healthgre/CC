import time

from selenium.webdriver.common.by import By

from pythonProject.src.variables import cases_button_xpath


class Test_002_checking_the_number_of_skins_in_the_case:
    def test_002_checking_the_number_of_skins_in_the_case(self, driver):
        driver.implicitly_wait(10)

        assert driver.find_element(By.ID, "tg-auth")  # Проверка отсутствия авторизации.
        assert driver.find_element(By.ID, "steam-auth")

        for i in range(2, 4):  # У нас 2 категории, поэтому диапазон от 2 до 4.
            cases_count = len(driver.find_elements(By.XPATH,
                                                   f"//main[@class='page-content']/div[{i}]/div[2]/button"))  # Высчитал колличество кейсов в категории. "i" - категория кейсов.

            for j in range(1, cases_count + 1):
                case_name = driver.find_element(By.XPATH,
                                                f"//main[@class='page-content']/div[{i}]/div[2]/button[{j}]/div[3]").text  # Взял название кейса.
                skins_count = driver.find_element(By.XPATH,
                                                  f"//main[@class='page-content']/div[{i}]/div[2]/button[{j}]/div[1]/p").text  # Взял колличество скинов в кейсе с "шт.".
                skins_count = int(skins_count[:-4])  # Убрал "шт." и перевёл в инт.

                driver.find_element(By.XPATH,
                                    f"//main[@class='page-content']/div[{i}]/div[2]/button[{j}]").click()  # Нажал на выбранный кейс.  "i" - категория кейсов. "j" - номер кейса.

                center_skin_count = len(driver.find_elements(By.XPATH,
                                                             "//div[@class='skins-container ']/div/div/div[@class='flex flex-col text-center z-10 items-center gap-[10px]']"))  # Количество скинов которые один на айтем.
                end_skin_count = len(driver.find_elements(By.XPATH,
                                                          "//div[@class='skins-container ']/div/div/div[@class='flex flex-col text-center z-10 items-end gap-[10px]']"))  # Количество скинов которые 2 на айтем, (левый).
                start_skin_count = len(driver.find_elements(By.XPATH,
                                                            "//div[@class='skins-container ']/div/div/div[@class='flex flex-col text-center z-10 items-start gap-[10px]']"))  # Количество скинов которые 2 на айтем, (ghfdsq).

                # total_skins_count = center_skin_count + end_skin_count + start_skin_count  # Высчитал сколько всего скинов в кейсе.
                # assert skins_count == total_skins_count
                # try:
                #     assert skins_count == total_skins_count
                #     assert 3 == 1
                # except AssertionError:
                #     print(f"{case_name}         {skins_count} == {total_skins_count}")

                driver.find_element(By.XPATH, cases_button_xpath).click()  # Нажал на надпись "Кейсы" в шапке.
