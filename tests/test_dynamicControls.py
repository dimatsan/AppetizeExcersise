from page_objects.dynamicControld_page import DynamicControlsPage

class DynamicControlsTest(DynamicControlsPage):

    # open url hook
    def setUp(self):
        super().setUp()
        self.open_dynamic_controls_page()

    # after checking "A chackbox" and clicking Remove - a checkbox should disappear and "It's gone!" message should
    # be displayed and after clicking Add the checkbox should appear again with "It's back!" message
    def test_dynamicCheckbox(self):
        self.assert_true(self.is_element_present(DynamicControlsPage.checkbox_element))
        self.click(DynamicControlsPage.checkbox_input)
        self.click(DynamicControlsPage.checkbox_swap_btn)
        self.wait_for_element_absent(DynamicControlsPage.checkbox_element)
        self.assert_text("It's gone!", DynamicControlsPage.result_message)
        self.click(DynamicControlsPage.checkbox_swap_btn)
        self.wait_for_element_present(DynamicControlsPage.checkbox_element)
        self.assert_text("It's back!", DynamicControlsPage.result_message)

    # by default the input box should be disabled and after clicking Enable button - becomes enabled with "It's
    # enabled!" and upon clicking Disable input becomes disabled again with "It's disabled!" message
    def test_dynamicInput(self):
        self.assert_false(self.is_element_enabled(DynamicControlsPage.textbox_input))
        self.click(DynamicControlsPage.textbox_swap_btn)
        self.wait_for_element_present(DynamicControlsPage.result_message)
        self.assert_text("It's enabled!", DynamicControlsPage.result_message)
        self.assert_true(self.is_element_enabled(DynamicControlsPage.textbox_input))
        self.click(DynamicControlsPage.textbox_swap_btn)
        self.wait_for_element_present(DynamicControlsPage.result_message)
        self.assert_text("It's disabled!", DynamicControlsPage.result_message)
        self.assert_false(self.is_element_enabled(DynamicControlsPage.textbox_input))

