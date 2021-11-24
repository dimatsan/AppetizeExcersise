from page_objects.jsAlerts_page import JSAlertsPage

class JSAlertsTest(JSAlertsPage):

    # open url hook
    def setUp(self):
        super().setUp()
        self.open_js_alerts_page()

    # when clicking "Click for JS alert" alert should pop up with only option to accept.
    # after accepting the alert "You successfully clicked an alert" message should appear
    def test_alert1(self):
        self.find_element(JSAlertsPage.js_alert_btn).click()
        self.wait_for_and_accept_alert()
        self.assert_text("You successfully clicked an alert", JSAlertsPage.result_message)

    # when clicking "Click for JS Confirm" alert should pop up with confirm/cancel options
    # after confirming the alert "You clicked: Ok" message should appear
    # after canceling the alert "You clicked: Cancel" message should appear
    def test_alert2(self):
        self.find_element(JSAlertsPage.js_confirm_btn).click()
        self.wait_for_and_accept_alert()
        self.assert_text("You clicked: Ok", JSAlertsPage.result_message)
        self.find_element(JSAlertsPage.js_confirm_btn).click()
        self.wait_for_and_dismiss_alert()
        self.assert_text("You clicked: Cancel", JSAlertsPage.result_message)

    # when clicking "Click for JS Prompt" alert should pop up with text input and confirm/cancel options
    # after confirming the alert "You entered: [your text]" message should appear or just "You entered: " if you
    # didn't input any text
    # after canceling the alert "You entered: null" message should appear
    def test_alert3(self):
        self.find_element(JSAlertsPage.js_prompt_btn).click()
        testInput = "some test input"
        self.switch_to_alert().send_keys(testInput)
        self.wait_for_and_accept_alert()
        self.assert_text("You entered: " + testInput, JSAlertsPage.result_message)
        self.find_element(JSAlertsPage.js_prompt_btn).click()
        self.wait_for_and_dismiss_alert()
        self.assert_text("You entered: null", JSAlertsPage.result_message)



