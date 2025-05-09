from pages.request_quote_page import RequestQuotePage

def test_request_quote_form_happy_path(page):
    quote_page = RequestQuotePage(page)
    quote_page.scroll_to_form(4000)
    quote_page.fill_form(
        name="John Doe",
        email="john.doe@example.com",
        service="B Service",
        message="This is a test message with more than 5 characters.",
        purpose="Business",
        withdrawal_options=["Cash"]
    )

    assert quote_page.get_field_value("#name") == "John Doe"
    assert quote_page.get_field_value("#email") == "john.doe@example.com"
    assert quote_page.get_field_value("select#service") == "B Service"
    assert quote_page.get_field_value("#message") == "This is a test message with more than 5 characters."

    quote_page.submit()

    assert quote_page.is_success_message_visible()

def test_request_quote_form_validation_empty_submission(page):
    quote_page = RequestQuotePage(page)
    quote_page.scroll_to_form(4000)
    quote_page.submit()

    assert quote_page.get_error_visibility("input#name.is-invalid")
    assert quote_page.get_error_visibility("input#email.is-invalid")
    assert quote_page.get_error_visibility("select#service.is-invalid")
    assert quote_page.get_error_visibility("textarea#message.is-invalid")
