#!/usr/bin/env python3

# Задача 1.
# Представлен список из значений "Xiaomi Redmi Note 10S", "Смартфон Xiaomi Redmi Note 10 Pro", "Apple iPhone 13",
# "Apple iPhone 11", "Huawei nova Y70", "Смартфон Apple iPhone 13 Pro".
# Необходимо создать новый список, содержащий модели бренда Apple.

print("\n")
print('#' * 80)
print("\n")
print("Aliaksandr Martsinkevich | 2022-10-21 | Stage 2 | Task 1 | Lists")
print("\n")
print('#' * 80)
print("\n")

print("Задача 1.")
print("Представлен список из значений \"Xiaomi Redmi Note 10S\",")
print("\"Смартфон Xiaomi Redmi Note 10 Pro\", \"Apple iPhone 13\",")
print("\"Apple iPhone 11\", \"Huawei nova Y70\", \"Смартфон Apple iPhone 13 Pro\".")
print("Необходимо создать новый список, содержащий модели бренда Apple.")

print("\n")
print('-' * 80)
print("\n")

phones_all = ["Xiaomi Redmi Note 10S", "Смартфон Xiaomi Redmi Note 10 Pro", "Apple iPhone 13", "Apple iPhone 11", "Huawei nova Y70", "Смартфон Apple iPhone 13 Pro"]
phones_list = []
phone_brand = "Apple"

print("List of all phones:", phones_all)

print("\nSearching", phone_brand, "phones...")

for phone_model in phones_all:
    if phone_model.find(phone_brand) != -1:
        phones_list.append(phone_model)
        print(phone_brand, "phone found:", phone_model)

print("\n")
print("List of", phone_brand, "phones:", phones_list)
print("\n")
