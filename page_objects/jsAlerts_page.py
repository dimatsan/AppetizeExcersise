from seleniumbase import BaseCase

class JSAlertsPage(BaseCase):
    js_alert_btn = '''button[onclick="jsAlert()"]'''
    js_confirm_btn = '''button[onclick="jsConfirm()"]'''
    js_prompt_btn = '''button[onclick="jsPrompt()"]'''
    result_message = "#result"

    def alert_pop(self):
        self.find_element(JSAlertsPage.js_alert_btn).click()
        self.wait_for_and_accept_alert()
        # after accepting the alert "You successfully clicked an alert" message should appear
        self.assert_text("You successfully clicked an alert", JSAlertsPage.result_message)

    def alert_choose_confirm(self):
        self.find_element(JSAlertsPage.js_confirm_btn).click()
        # after confirming the alert "You clicked: Ok" message should appear
        self.wait_for_and_accept_alert()
        self.assert_text("You clicked: Ok", JSAlertsPage.result_message)

    def alert_choose_cancel(self):
        self.find_element(JSAlertsPage.js_confirm_btn).click()
        # after canceling the alert "You clicked: Cancel" message should appear
        self.wait_for_and_dismiss_alert()
        self.assert_text("You clicked: Cancel", JSAlertsPage.result_message)

    def alert_prompt_input(self):
        self.find_element(JSAlertsPage.js_prompt_btn).click()
        # after inputting text and confirming the alert "You entered: [your text]" message should appear or just
        # "You entered: " if you didn't input any text
        testInput = "some test input"
        self.switch_to_alert().send_keys(testInput)
        self.wait_for_and_accept_alert()
        self.assert_text("You entered: " + testInput, JSAlertsPage.result_message)

    def alert_prompt_cancel(self):
        self.find_element(JSAlertsPage.js_prompt_btn).click()
        # after canceling the alert "You entered: null" message should appear
        self.wait_for_and_dismiss_alert()
        self.assert_text("You entered: null", JSAlertsPage.result_message)