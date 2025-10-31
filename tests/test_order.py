import allure
import pytest

from data import DataOrder
from pages.order_page import OrderPage
from pages.main_page import MainPage


class TestOrderScooter:
    @pytest.mark.parametrize("order_data", DataOrder.test_data)
    @allure.title("Тест заказа самоката (данные: {order_data})")
    def test_order_scooter(self, driver, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.button_order_click(button=order_data["button"])
        order_page.check_order_scooter(
            name=order_data["name"],
            surname=order_data["surname"],
            address=order_data["address"],
            metro=order_data["metro"],
            phone=order_data["phone_number"],
            rental_date=order_data["date"],
            rental_period=order_data["period"],
            color=order_data["color"],
            comment=order_data["comment"],
        )
        # Проверяем сообщение об успехе
        success_message = order_page.get_success_message()
        assert "Номер заказа" in success_message
