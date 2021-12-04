from seleniumbase import BaseCase

class DynamicControlsPage(BaseCase):
    checkbox_element = "#checkbox"
    checkbox_input = "input[type=checkbox]"
    checkbox_swap_btn = '''button[onclick="swapCheckbox()"]'''
    textbox_input = "input[type=text]"
    textbox_swap_btn = '''button[onclick="swapInput()"]'''
    result_message = "#message"

    # after checking "A checkbox" and clicking Remove - a checkbox should disappear and "It's gone!" message should
    # be displayed
    def check_box_and_remove(self):
        self.assert_true(self.is_element_present(DynamicControlsPage.checkbox_element))
        self.click(DynamicControlsPage.checkbox_input)
        self.click(DynamicControlsPage.checkbox_swap_btn)
        self.wait_for_element_absent(DynamicControlsPage.checkbox_element)
        self.assert_text("It's gone!", DynamicControlsPage.result_message)

    # after clicking Add the checkbox should appear again with "It's back!" message
    def add_box_back(self):
        self.assert_false(self.is_element_present(DynamicControlsPage.checkbox_element))
        self.click(DynamicControlsPage.checkbox_swap_btn)
        self.wait_for_element_present(DynamicControlsPage.checkbox_element)
        self.assert_text("It's back!", DynamicControlsPage.result_message)

    # by default the input box should be disabled and after clicking Enable button - becomes enabled with "It's
    # enabled!"
    def enable_input(self):
        self.assert_false(self.is_element_enabled(DynamicControlsPage.textbox_input))
        self.click(DynamicControlsPage.textbox_swap_btn)
        self.wait_for_element_present(DynamicControlsPage.result_message)
        self.assert_text("It's enabled!", DynamicControlsPage.result_message)
        self.assert_true(self.is_element_enabled(DynamicControlsPage.textbox_input))

    # upon clicking Disable input becomes disabled again with "It's disabled!" message
    def disable_input(self):
        self.assert_true(self.is_element_enabled(DynamicControlsPage.textbox_input))
        self.click(DynamicControlsPage.textbox_swap_btn)
        self.wait_for_element_present(DynamicControlsPage.result_message)
        self.assert_text("It's disabled!", DynamicControlsPage.result_message)
        self.assert_false(self.is_element_enabled(DynamicControlsPage.textbox_input))
