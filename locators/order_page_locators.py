from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME = (By.XPATH, "//input[contains(@placeholder, '* Имя')]")  # Поле Имя
    SURNAME = (By.XPATH, "//input[contains(@placeholder, '* Фамилия')]")  # Поле Фамилия
    ADDRESS = (
        By.XPATH,
        "//input[contains(@placeholder, '* Адрес: куда привезти заказ')]",
    )  # Поле Адрес
    METRO_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder, '* Станция метро')]",
    )  # Поле Станция метро
    PHONE_NUMBER = (
        By.XPATH,
        "//input[contains(@placeholder, '* Телефон: на него позвонит курьер')]",
    )  # Поле Номер телефона

    BUTTON_NEXT = (
        By.XPATH,
        "//div[contains(@class, 'Order_NextButton__1_rCA')]/button[text()='Далее']",
    )  # Кнопка Далее

    RENTAL_DATE = (
        By.XPATH,
        "//input[contains(@placeholder, '* Когда привезти самокат')]",
    )  # Поле Когда привезти самокат

    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-placeholder")  # Поле Срок аренды
    RENTAL_PERIOD_OPTION = (
        By.XPATH,
        "//div[contains(@class, 'Dropdown-option')]",
    )  # Все варианты аренды
    COLOR_BLACK = (By.ID, "black")  # Чек-бокс цвет самоката черный жемчуг
    COLOR_GRAY = (By.ID, "grey")  # Чек-бокс цвет самоката серая безысходность
    COMMENTS = (
        By.XPATH,
        "//input[contains(@placeholder, 'Комментарий для курьера')]",
    )  # Комментарий для курьера
    ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Buttons__1xGrp')]/button[text()='Заказать']",
    )  # Кнопка Заказать
    ORDER_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")  # Окно подтверждения заказа
    BUTTON_YES = (
        By.XPATH,
        "//div[contains(@class, 'Order_Buttons__1xGrp')]/button[text() = 'Да']",
    )  # Кнопка Да в окне подтверждения заказа
    SUCCESS_MESSAGE = (
        By.XPATH,
        "//div[contains(text(), 'Номер заказа')]",
    )  # Сообщение с номером заказа

    @staticmethod
    def metro_locator(metro):  # Возвращает локатор для поля Станция метро
        return (By.XPATH, f"//div[text()='{metro}']")

    @staticmethod
    def period_locator(rental_period):
        return (By.XPATH, f"//div[text()='{rental_period}']")
