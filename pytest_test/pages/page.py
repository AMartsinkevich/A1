import random
from pages.base_page import BasePage
from locators.page_locators import PageLocators
from selenium.webdriver.common.keys import Keys

class PromotionPage(BasePage):

    def choose_random_promotional_offer(self):

        current_url = self.driver.current_url

        promotion_area_label = self.element_is_visible(PageLocators.PROMOTION_AREA).get_attribute('innerHTML')
        promotion_button = random.choice(self.elements_are_visible(PageLocators.PROMOTION_BUTTON))
        promotion_button_label = promotion_button.find_element(*PageLocators.PROMOTION_BUTTONS_AREA).get_attribute('innerHTML')
        promotion_button.send_keys(Keys.ENTER)
        
        return current_url, promotion_area_label, promotion_button_label

    def choose_installment_offer(self):

        current_url = self.driver.current_url
        
        phone_model = self.element_is_visible(PageLocators.PHONE_MODEL_AREA).get_attribute('innerHTML')
        installment_list = self.element_is_visible(PageLocators.INSTALLMENT_LIST)
        installment_list.click()
        installment_plan = self.driver.find_element(*PageLocators.INSTALLMENT_PLAN)
        installment_plan_id = installment_plan.get_property('value')
        installment_plan_duration = installment_plan.get_attribute('innerHTML').strip().replace('&nbsp;', ' ')
        installment_plan_details = installment_plan.get_attribute('data-note').replace('<br/>', '\n')
        self.driver.find_element(PageLocators.INSTALLMENT_PLAN_ID[0], PageLocators.INSTALLMENT_PLAN_ID[1].replace('installment_plan_id', installment_plan_id)).click()
        installment_list.send_keys(Keys.TAB, Keys.ENTER)
        
        return current_url, phone_model, installment_plan_duration, installment_plan_details

    def navigate_to_shopping_cart(self):

        current_url = self.driver.current_url
        
        return current_url