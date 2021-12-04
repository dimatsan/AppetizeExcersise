from page_objects.dynamicControld_page import DynamicControlsPage

class DynamicControlsTest(DynamicControlsPage):

    # open url hook
    def setUp(self):
        super().setUp()
        self.open("https://the-internet.herokuapp.com/dynamic_controls")

    def test_dynamicCheckbox(self):
        self.check_box_and_remove()
        self.add_box_back()

    def test_dynamicInput(self):
        self.enable_input()
        self.disable_input()

