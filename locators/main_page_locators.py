from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGO_YANDEX = (
        By.XPATH,
        "//a[contains(@class, 'Header_LogoYandex')]/img[@alt='Yandex']",
    )  # Логотип Яндекс
    LOGO_SCOOTER = (
        By.XPATH,
        "//a[contains(@class, 'Header_LogoScooter__3lsAR')]/img[@alt='Scooter']",
    )  # Логотип Самокат
    BUTTON_ORDER_TOP = (
        By.XPATH,
        "//div[contains(@class, 'Header_Nav__AGCXC')]/button[text()='Заказать']",
    )  # Верхняя кнопка Заказать
    BUTTON_ORDER_BOTTOM = (
        By.XPATH,
        "//div[contains(@class, 'Home_FinishButton__1_cWm')]/button[text()='Заказать']",
    )  # Нижняя кнопка Заказать
    FAQ_CONTAINER = (By.CLASS_NAME, "accordion")  # Секция Вопросы о важном

    COOKIES_BUTTON_LOCATOR = (By.ID, "rcc-confirm-button")

    @staticmethod
    def faq_question(question):  # Возвращает локатор для вопроса FAQ по индексу
        return By.ID, f"accordion__heading-{question}"

    @staticmethod
    def answer_number(answer):  # Возвращает локатор для ответа FAQ по индексу
        return By.ID, f"accordion__panel-{answer}"
