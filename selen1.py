from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class TestShowMyPets:

    def setup(self):
        # Инициализация пользовательских данных
        self.user = "dimon@mail.ru"
        self.password = "dimon@mail.ru33"
        self.open()

    def open(self):
        # Инициализация драйвера и открытие страницы входа
        self.driver = webdriver.Chrome('/Users/dmitrijparsin/webdriver/chromedriver_107')
        self.driver.get("https://petfriends.skillfactory.ru/login")
        time.sleep(2)

    def close(self):
        # Завершение работы драйвера
        self.driver.quit()

    def teardown(self):
        self.close()

    def login(self):
        # Вход в систему
        email_input = self.driver.find_element(By.XPATH, "//input[@id='email']")
        password_input = self.driver.find_element(By.XPATH, "//input[@id='pass']")
        email_input.send_keys(self.user)
        password_input.send_keys(self.password)
        time.sleep(2)
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        # Проверка наличия кнопки "Выйти"
        assert self.driver.find_element(By.XPATH, "//button[contains(text(),'Выйти')]")
        time.sleep(2)

    def test_show_my_pets(self):
        # Вход и переход на страницу "Мои питомцы"
        self.login()
        # Ожидание страницы
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Мои питомцы')]"))
        # Поиск элементов на странице
        images = self.driver.find_elements(By.CSS_SELECTOR, ('.card-deck .card-img-top'))
        names = self.driver.find_elements(By.CSS_SELECTOR, ('.card-deck .card-title'))
        descriptions = self.driver.find_elements(By.CSS_SELECTOR, ('.card-deck .card-text'))
        # Проверки для каждого элемента
        for i in range(len(names)):
            assert images[i].get_attribute('src') != ''
            assert names[i].text != ''
            assert descriptions[i].text != ''
            assert ', ' in descriptions[i].text
            parts = descriptions[i].text.split(", ")
            assert len(parts[0]) > 0
            assert len(parts[1]) > 0
