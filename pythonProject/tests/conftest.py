import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pythonProject.src.authentication import authentication
from pythonProject.src.clean import clean
from pythonProject.src.logout import logout
from pythonProject.src.variables import clear_case_inscription_xpath


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://clearcase.net")
    driver.maximize_window()
    yield driver
    # driver.close()


@pytest.fixture(scope="session")
def auth(driver):
    authentication(driver)
    # yield
    # authentication(driver)


@pytest.fixture(scope="session")
def clean_inventory_before_test(driver, auth):
    clean(driver)
    yield


@pytest.fixture(scope="session")
def logout_before_test(driver, auth):
    logout(driver)
    yield


@pytest.fixture(scope="session")
def clean_inventory_after_test(driver, auth):
    yield
    clean(driver)


@pytest.fixture(scope="session")
def logout_after_test(driver):
    yield
    logout(driver)


@pytest.fixture(scope="session")
def get_skin_to_the_inventory_1(driver, auth):
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, clear_case_inscription_xpath).click()  # Перешёл на главную страницу.
    driver.find_element(By.XPATH, f"//main[@class='page-content']/div[{2}]/div[2]/button[{1}]").click()  # Выбрал кейс.
    driver.find_element(By.XPATH,
                        f"//div[@class='count-boxes-container']/button[{1}]").click()  # Выбрал сколько скинов за раз открыть.
    driver.find_element(By.XPATH,
                        f"//div[@class='control-buttons-container']/button[{2}]").click()  # Кнопка открытия скина.
    # for i in range(0, 10):
    #     driver.implicitly_wait(3)
    #     driver.find_element(By.XPATH,
    #                         "//div[@class='control-buttons-container']/button[3]").click()


@pytest.fixture(scope="session")
def get_skin_to_the_inventory_10(driver, auth):
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH,
                        clear_case_inscription_xpath).click()  # Перешёл на главную страницу.
    driver.find_element(By.XPATH, f"//main[@class='page-content']/div[{2}]/div[2]/button[{1}]").click()  # Выбрал кейс.
    driver.find_element(By.XPATH,
                        f"//div[@class='count-boxes-container']/button[{10}]").click()  # Выбрал сколько скинов за раз открыть.
    driver.find_element(By.XPATH,
                        f"//div[@class='control-buttons-container']/button[{2}]").click()  # Кнопка открытия скина.
