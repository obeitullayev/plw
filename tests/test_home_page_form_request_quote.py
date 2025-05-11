from pages.home_page import RequestQuotePage

class TestRequestQuoteForm():
    def test_request_quote_form_happy_path(self, page, base_url):
        home_page = RequestQuotePage(page, base_url)
        home_page.open_page()
        home_page.scroll_to_form(4000)
        home_page.fill_form_quote(
            name="John Doe",
            email="john.doe@example.com",
            service="B Service",
            message="This is a test message with more than 5 characters.",
            purpose="Business",
            withdrawal_options=["Cash"]
        )

        assert home_page.get_field_value("#name") == "John Doe"
        assert home_page.get_field_value("#email") == "john.doe@example.com"
        assert home_page.get_field_value("select#service") == "B Service"
        assert home_page.get_field_value("#message") == "This is a test message with more than 5 characters."
        assert home_page.is_element_checked("input[value='Business']"), 'Element "Business" is not checked'
        assert home_page.is_element_checked("input[value='Cash']"), 'Element "Cash" is not checked'

        home_page.submit()

        assert home_page.is_success_message_visible()

    def test_request_quote_form_validation_empty_submission(self, page, base_url):
        home_page = RequestQuotePage(page, base_url)
        home_page.open_page()
        home_page.scroll_to_form(4000)
        home_page.submit()

        assert home_page.get_error_visibility("input#name.is-invalid"), "Ошибка: поле 'Name' не содержит сообщение об ошибке"
        assert home_page.get_error_visibility("input#email.is-invalid"), "Ошибка: поле 'Email' не содержит сообщение об ошибке"
        assert home_page.get_error_visibility("select#service.is-invalid"), "Ошибка: поле 'Service' не содержит сообщение об ошибке"
        assert home_page.get_error_visibility("textarea#message.is-invalid"), "Ошибка: поле 'Message' не содержит сообщение об ошибке"
