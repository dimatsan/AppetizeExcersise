from seleniumbase import BaseCase

class LoginPage(BaseCase):
    login_btn = "button"
    login_result_message = "#flash"
    username_input = "#username"
    password_input = "#password"
    logout_btn = '''a[href="/logout"]'''
    login_page_label = "h2"

    def open_login_page(self):
        self.open("https://the-internet.herokuapp.com/login")

    #login helper method
    def login(self, username, password):
        self.set_value(self.username_input, username)
        self.set_value(self.password_input, password)
        self.click(self.login_btn)
