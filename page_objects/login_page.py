from seleniumbase import BaseCase

class LoginPage(BaseCase):
    login_btn = "button"
    login_result_message = "#flash"
    username_input = "#username"
    password_input = "#password"
    logout_btn = '''a[href="/logout"]'''
    login_page_label = "h2"


    #login helper method
    def login(self, username, password):
        self.set_value(self.username_input, username)
        self.set_value(self.password_input, password)
        self.click(self.login_btn)

    def confirm_that_logged_in(self):
        self.assert_text("You logged into a secure area!", LoginPage.login_result_message)
        self.assert_equal(self.get_current_url(), "https://the-internet.herokuapp.com/secure")

    def log_out(self):
        self.click(LoginPage.logout_btn)
        self.assert_text("Login Page", LoginPage.login_page_label)
        self.assert_equal(self.get_current_url(), "https://the-internet.herokuapp.com/login")