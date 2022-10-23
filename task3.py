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
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import random

url = "https://www.a1.by/ru/c/shop/"

user_agents_list = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763"
]

options = Options()
options.add_argument("start-maximized")
options.add_argument(f"user-agent={random.choice(user_agents_list)}")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


try:
    print("Opening URL...")
    driver.get(url=url)
    time.sleep(2)
    driver.save_screenshot("a1_opening_url.png")

    print("Scrolling to promotions...")
    driver.execute_script("return arguments[0].scrollIntoView();", driver.find_element(By.XPATH, "//h2[text()='Товары по акции']"))
    time.sleep(2)
    driver.save_screenshot("a2_scrolling_to_promotions.png")

    print("Collecting list of items...")
    installment_buttons = driver.find_elements(By.ID, "promo-product-button_0")

    print("Choosing random one...")
    driver.execute_script("return arguments[0].scrollIntoView();", driver.find_element(By.ID, "promo-product-button_0"))
    time.sleep(2)
    driver.save_screenshot("a3_scrolling_to_promotion_buttons.png")

    random.choice(installment_buttons).click()
    time.sleep(2)
    driver.save_screenshot("a4_choosing_random_promotion.png")

    print("Scrolling to price block...")
    driver.execute_script("return arguments[0].scrollIntoView();", driver.find_element(By.CLASS_NAME, "price-block"))
    time.sleep(2)
    driver.save_screenshot("a5_scrolling_to_price_block.png")
    
    print("Opening installment list...")
    driver.find_element(By.XPATH, "//span[@role='combobox']").click()
    time.sleep(2)
    driver.save_screenshot("a6_opening_installment_list.png")

    print("Selecting installment plan...")
    plan_selector = driver.find_element(By.ID, "priceBlock_selector_2")
    print("-" * 80)
    print(plan_selector.get_attribute("innerHTML").strip().replace("&nbsp;", " "))
    print("-" * 80)
    print(plan_selector.get_attribute("data-note").replace("<br/>", "\n"))
    print("-" * 80)
    plan_selector_value = plan_selector.get_property("value")
    driver.find_element(By.XPATH, f"//li[contains(@id, '{plan_selector_value}')]").click()
    time.sleep(2)
    driver.save_screenshot("a7_selecting_installment_plan.png")

    print("Navigating to shopping cart...")
    driver.find_element(By.XPATH, "//span[@role='combobox']").send_keys(Keys.TAB, Keys.ENTER)
    time.sleep(2)
    driver.save_screenshot("a8_navigating_to_shopping_cart.png")

    print("Closing...")


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

print("\n")
