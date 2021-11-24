from seleniumbase import BaseCase

class JSAlertsPage(BaseCase):
    js_alert_btn = '''button[onclick="jsAlert()"]'''
    js_confirm_btn = '''button[onclick="jsConfirm()"]'''
    js_prompt_btn = '''button[onclick="jsPrompt()"]'''
    result_message = "#result"


    def open_js_alerts_page(self):
        self.open("https://the-internet.herokuapp.com/javascript_alerts")

