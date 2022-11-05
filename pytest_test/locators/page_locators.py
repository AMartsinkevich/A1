from selenium.webdriver.common.by import By

class PageLocators:
    PROMOTION_AREA = (By.XPATH, "//h2[text()='Товары по акции']")
    PROMOTION_BUTTONS_AREA = (By.CLASS_NAME, "button-label")
    PROMOTION_BUTTON = (By.ID, "promo-product-button_0")

    PHONE_MODEL_AREA = (By.XPATH, "//h1[@class='h h--1 pdp-header-heading']")
    INSTALLMENT_LIST = (By.XPATH, "//span[@role='combobox']")
    INSTALLMENT_PLAN = (By.ID, "priceBlock_selector_2")
    INSTALLMENT_PLAN_ID = (By.XPATH, f"//li[contains(@id, 'installment_plan_id')]")
    
