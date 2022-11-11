from pages.page import PromotionPage


class TestInstallmentOfferFlow:

    url = 'https://www.a1.by/ru/c/shop/'
 

    def test_installment_offer_flow(self, driver):

        promotion_page = PromotionPage(driver, self.url)
        promotion_page.open()
        current_url, promotion_area_label, promotion_button_label = promotion_page.choose_random_promotional_offer()
        assert current_url in self.url, 'Start page has been changed or did not load'
        assert promotion_area_label in 'Товары по акции', 'Label of promotion area has been changed or not found'
        assert promotion_button_label == 'Подробнее', 'Label of promotion button has been changed or not found'

        current_url, phone_model, installment_plan_duration, installment_plan_details = promotion_page.choose_installment_offer()
        print(f"\n\nPhone: {phone_model}\nInstallment: {installment_plan_duration}\nMore details: {installment_plan_details}\n")
        assert '/shop/phones/' in current_url, 'Phone page has been changed or did not load'
        assert '6 мес' in installment_plan_duration, 'Installment plan duration has been changed or not found'

        current_url = promotion_page.navigate_to_shopping_cart()
        assert "/asmp/" in current_url, 'Shopping cart page has been changed or did not load'


