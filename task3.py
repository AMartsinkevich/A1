#!/usr/bin/env python3

#Задача 3.
#С помощью инструментов тестирования Selenium WebDriver (from selenium import webdriver) и Pytest (import pytest) необходимо создать тест, содержащий данные шаги и проверки, описанные ниже.
#1. Перейти по ссылке https://www.a1.by/ru/c/shop 
#2. В блоке Товары по акции выбрать случайным образом блок со смартфоном и нажать на кнопку «Подробнее»
#3. Справа из выпадающего списка выбрать вариант оплаты в рассрочку на 6 месяцев: «6 мес по ххх руб/мес»
#4. Нажать кнопку «Войти и купить»
#5. Вывести сообщение с названием выбранного оборудования и текст выбранного варианта оплаты, включая стоимость. (Например: «Выбран Xiaomi 11T 128GB небесный голубой, вариант оплаты: 6 мес по 229,82 руб/мес»)

print("\n")
print('#' * 80)
print("\n")
print("Aliaksandr Martsinkevich | 2022-10-21 | Stage 2 | Task 2 | Selenium")
print("\n")
print('#' * 80)
print("\n")

print("Задача 3.")
print("С помощью инструментов тестирования Selenium WebDriver (from selenium import")
print("webdriver) и Pytest (import pytest) необходимо создать тест, содержащий данные")
print("шаги и проверки, описанные ниже.")
print("1. Перейти по ссылке https://www.a1.by/ru/c/shop")
print("2. В блоке Товары по акции выбрать случайным образом блок со смартфоном")
print("и нажать на кнопку «Подробнее»")
print("3. Справа из выпадающего списка выбрать вариант оплаты в рассрочку")
print("на 6 месяцев: «6 мес по ххх руб/мес»")
print("4. Нажать кнопку «Войти и купить»")
print("5. Вывести сообщение с названием выбранного оборудования и текст")
print("выбранного варианта оплаты, включая стоимость. (Например: «Выбран")
print("Xiaomi 11T 128GB небесный голубой, вариант оплаты: 6 мес по 229,82 руб/мес»)")

print("\n")
print('-' * 80)
print("\n")

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

url = "https://www.a1.by/ru/c/shop/"

user_agents_list = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763"
]

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={random.choice(user_agents_list)}")

driver = webdriver.Chrome(
    executable_path="./webdriver/chromedriver",
    options=options
)
driver.maximize_window()


try:
    print("Opening URL...")
    driver.get(url=url)
    time.sleep(5)
    driver.save_screenshot("a1.png")
    print("Scrolling to 'Товары по акции'...")
    driver.execute_script("return arguments[0].scrollIntoView();", driver.find_element(By.XPATH, "//h2[text()='Товары по акции']"))
    time.sleep(5)
    driver.save_screenshot("a2.png")
    print("Collecting list of items...")
    installment_button = driver.find_elements(By.ID, "promo-product-button_0")
    print("Choosing random one...")
    random.choice(installment_button).click()
    time.sleep(5)
    driver.save_screenshot("a3.png")
    print("Closing...")
    time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

print("\n")
