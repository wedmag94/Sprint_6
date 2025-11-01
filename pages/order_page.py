import allure


from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):

    @allure.step("Заполнить поле Имя")
    def set_field_name(self, name):
        self.send_keys_to_input(OrderPageLocators.NAME, name)

    @allure.step("Заполнить поле Фамилия")
    def set_field_surname(self, surname):
        self.send_keys_to_input(OrderPageLocators.SURNAME, surname)

    @allure.step("Заполнить поле Адрес")
    def set_field_address(self, address):
        self.send_keys_to_input(OrderPageLocators.ADDRESS, address)

    @allure.step("Заполнить поле Станция метро")
    def select_metro(self, metro):
        self.click_to_element(OrderPageLocators.METRO_INPUT)
        metro_locator = OrderPageLocators.metro_locator(metro)
        self.click_to_element(metro_locator)

    @allure.step("Заполнить поле Телефон")
    def set_phone(self, phone):
        self.send_keys_to_input(OrderPageLocators.PHONE_NUMBER, phone)

    @allure.step("Нажать кнопку Далее")
    def click_next_button(self):
        self.click_to_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step("Заполнить поле Когда привезти самокат")
    def set_field_rental_date(self, date):
        self.send_keys_to_input(OrderPageLocators.RENTAL_DATE, date)
        element = self.wait_for_element(OrderPageLocators.RENTAL_DATE)
        element.send_keys(Keys.ENTER)

    @allure.step("Заполнить поле Срок аренды")
    def set_field_rental_period(self, period):
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD)
        period_locator = OrderPageLocators.period_locator(period)
        self.click_to_element(period_locator)

    @allure.step("Выбрать цвет самоката")
    def select_color(self, color):
        if color == "черный":
            self.click_to_element(OrderPageLocators.COLOR_BLACK)
        elif color == "серый":
            self.click_to_element(OrderPageLocators.COLOR_GRAY)

    @allure.step("Заполнить поле комментарий для курьера")
    def add_comment(self, comment):
        self.send_keys_to_input(OrderPageLocators.COMMENTS, comment)

    @allure.step("Нажать кнопку Заказать в форме")
    def click_to_button_order(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ (кнопка Да)")
    def confirm_order(self):
        self.click_to_element(OrderPageLocators.BUTTON_YES)

    @allure.step("Получить текст сообщения об успешном заказе")
    def get_success_message(self):
        success_message = self.get_text_on_element(OrderPageLocators.SUCCESS_MESSAGE)
        return success_message

    @allure.step("Полный сценарий заказа самоката")
    def check_order_scooter(
        self,
        name,
        surname,
        address,
        metro,
        phone,
        rental_date,
        rental_period,
        color,
        comment,
    ):

        self.set_field_name(name)
        self.set_field_surname(surname)
        self.set_field_address(address)
        self.select_metro(metro)
        self.set_phone(phone)
        self.click_next_button()
        self.set_field_rental_date(rental_date)
        self.set_field_rental_period(rental_period)
        self.select_color(color)
        self.add_comment(comment)
        self.click_to_button_order()
        self.confirm_order()
        return self.get_success_message()
