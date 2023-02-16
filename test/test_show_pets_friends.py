from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_show_all_pets():
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys('a@bk.ru')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys('12345')

   # Настраиваем неявные ожидания:
   pytest.driver.implicitly_wait(10)

   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

   # Ищем на странице все фотографии, имена, породу (вид) и возраст питомцев:
   images = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody[1]/tr[1]/th[1]/img[1]')
   names = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody[1]/tr[1]/td[1]')
   descriptions = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody[1]/tr[1]/td[2]')

   # Проверяем, что на странице есть фотографии питомцев, имена, порода (вид) и возраст питомцев не пустые строки:
   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0
