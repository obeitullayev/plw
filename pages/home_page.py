class RequestQuotePage:
    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url

    def open_page(self):
        self.page.goto(self.base_url)

    def scroll_to_form(self, scroll_target):
        self.page.evaluate(f"() => window.scrollTo(0, {scroll_target})")

    def fill_form_quote(self, name, email, service, message, purpose, withdrawal_options):
        self.page.locator("#name").fill(name)
        self.page.locator("#email").fill(email)
        self.page.locator("select#service").select_option(service)
        self.page.locator("#message").fill(message)
        self.page.locator(f"input[value='{purpose}']").check()
        for option in withdrawal_options:
            self.page.locator(f"input[value='{option}']").check()

    def submit(self):
        self.page.locator("button:has-text('Request A Quote')").click()

    def is_success_message_visible(self):
        return self.page.locator("#formStatus").is_visible()

    def get_field_value(self, selector):
        return self.page.locator(selector).input_value()

    def is_element_checked(self, selector):
        return self.page.locator(selector).is_checked()

    def get_error_visibility(self, selector):
        return self.page.locator(selector).is_visible()
