from seleniumbase import BaseCase

class DynamicControlsPage(BaseCase):
    checkbox_element = "#checkbox"
    checkbox_input = "input[type=checkbox]"
    checkbox_swap_btn = '''button[onclick="swapCheckbox()"]'''
    textbox_input = "input[type=text]"
    textbox_swap_btn = '''button[onclick="swapInput()"]'''
    result_message = "#message"

    def open_dynamic_controls_page(self):
        self.open("https://the-internet.herokuapp.com/dynamic_controls")

