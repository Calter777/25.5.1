import pytest
from settings import valid_email, valid_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



def test_show_my_pets():
   '''Проверяем что мы оказались на странице "Мои питомцы"'''

   # Устанавливаем явное ожидание
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'html > body > nav > button > span')))
   # Нажимаем на ссылку "Меню "
   pytest.driver.find_element(By.CSS_SELECTOR,'html > body > nav > button > span').click()

   element = WebDriverWait(pytest.driver, 10).until( EC.presence_of_element_located((By.XPATH, '//*[@id="navbarNav"]/ul[1]/li[1]/a[1]')))
   # В открывшемся списке нажимаем на ссылку "Мои питомцы"
   pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul[1]/li[1]/a[1]').click()

   # Проверяем что мы оказались на странице "Мои питомцы"
   assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'