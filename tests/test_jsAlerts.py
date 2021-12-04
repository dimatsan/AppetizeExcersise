from page_objects.jsAlerts_page import JSAlertsPage

class JSAlertsTest(JSAlertsPage):

    # open url hook
    def setUp(self):
        super().setUp()
        self.open("https://the-internet.herokuapp.com/javascript_alerts")

    # when clicking "Click for JS alert" alert should pop up with only option to accept.
    def test_alert1(self):
        self.alert_pop()


    # when clicking "Click for JS Confirm" alert should pop up with confirm/cancel options
    def test_alert2(self):
        self.alert_choose_confirm()
        self.alert_choose_cancel()


    # when clicking "Click for JS Prompt" alert should pop up with text input and confirm/cancel options
    def test_alert3(self):
        self.alert_prompt_input()
        self.alert_prompt_cancel()



