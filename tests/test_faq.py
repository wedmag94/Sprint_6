import pytest
import allure

from data import DataFaq
from pages.main_page import MainPage


class TestImportantQuestions:
    @allure.title("Тест секции Вопросы о важном")
    @allure.description(
        "Проверяем, что при клике на вопрос отображается соответствующий ответ"
    )
    @pytest.mark.parametrize("faq_number, expected_text", DataFaq.answer)
    def test_faq_section(self, driver, faq_number, expected_text):
        main_page = MainPage(driver)
        main_page.wait_for_element_faq()
        main_page.click_on_faq_number(faq_number)
        assert main_page.check_the_answer_to_the_question(faq_number, expected_text)
