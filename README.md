# A1 Tasks

## Task 1

A list is provided of the values:
- "Xiaomi Redmi Note 10S";
- "Xiaomi Redmi Note 10 Pro Smartphone";
- "Apple iPhone 13";
- "Apple iPhone 11";
- "Huawei nova Y70";
- "Apple iPhone 13 Pro smartphone".
You need to create a new list containing Apple brand models.

## Task 2

You need to create an Animal class that has the attributes Name (type of animal), Color (its color) and Voice (sound emitted).
Write a function that returns a string like "It says <Voice>.", where <Voice> is a unique attribute of the Animal class.
Set three instances of the Cow, Cat, Dog class with unique attributes for each. For each instance, output a string like "<Name> is <Color>. It says <Voice>."

## Task 3

Using the Selenium WebDriver (from selenium import webdriver) and Pytest (import pytest) testing tools, you need to create a test that contains the steps and checks described below.

- Follow the link https://www.a1.by/ru/c/shop
- In the Promotional goods block, randomly select the block with a smartphone and click on the "Details" button
- On the right, from the drop-down list, select the payment option in installments for 6 months: “6 months for xxx rub/month”
- Press the "Login and buy" button
- Display a message with the name of the selected equipment and the text of the selected payment option, including the cost. (For example: "Choose Xiaomi 11T 128GB sky blue, payment option: 6 months at 229.82 rubles / month")
