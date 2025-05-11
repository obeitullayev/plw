class RequestQuotePage:
    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url

    def open_page(self):
        self.page.goto(self.base_url)

    def scroll_to_form(self, scroll_target):
        self.page.evaluate(f"() => window.scrollTo(0, {scroll_target})")

    def fill_form_quote(self, name, email, service, message, purpose, withdrawal_options):
        self.page.fill("#name", name)
        self.page.fill("#email", email)
        self.page.select_option("select#service", service)
        self.page.fill("#message", message)
        self.page.check(f"input[value='{purpose}']")
        for option in withdrawal_options:
            self.page.check(f"input[value='{option}']")

    def submit(self):
        self.page.click("button:has-text('Request A Quote')")

    def is_success_message_visible(self):
        return self.page.wait_for_selector("#formStatus", state="visible")

    def get_field_value(self, selector):
        return self.page.input_value(selector)

    def get_error_visibility(self, selector):
        return self.page.wait_for_selector(selector, state="visible")
