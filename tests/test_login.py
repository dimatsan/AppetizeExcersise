from page_objects.login_page import LoginPage

class LoginTest(LoginPage):
    # saving valid login and password in variables for convenience
    valid_username = "tomsmith"
    valid_password = "SuperSecretPassword!"

    # open url hook
    def setUp(self):
        super().setUp()
        self.open_login_page()

    # when trying to login with no input "Your username is invalid!" error pops up
    def test_login1(self):
        self.click(LoginPage.login_btn)
        self.assert_text("Your username is invalid!", LoginPage.login_result_message)

    # when trying to login with wrong username "Your username is invalid!" error pops up
    def test_login2(self):
        LoginPage.login(self, "wrong_username", self.valid_password)
        self.assert_text("Your username is invalid!", LoginPage.login_result_message)

    # when trying to login with wrong password "Your password is invalid!" error pops up
    def test_login3(self):
        LoginPage.login(self, self.valid_username, "wrong_password")
        self.assert_text("Your password is invalid!", LoginPage.login_result_message)

    # when trying to login with correct credentials "You logged into a secure area!" message pops up and you are taken to a correct page
    def test_login4(self):
        LoginPage.login(self, self.valid_username, self.valid_password)
        self.assert_text("You logged into a secure area!", LoginPage.login_result_message)
        self.assert_equal(self.get_current_url(), "https://the-internet.herokuapp.com/secure")

    # after successful Log In, user is able to log out by clicking Logout button. Verify by "You logged out of the secure area!" message and url
    def test_login5(self):
        LoginPage.login(self, self.valid_username, self.valid_password)
        self.assert_text("You logged into a secure area!", LoginPage.login_result_message)
        self.assert_equal(self.get_current_url(), "https://the-internet.herokuapp.com/secure")
        self.click(LoginPage.logout_btn)
        self.assert_text("Login Page", LoginPage.login_page_label)
        self.assert_equal(self.get_current_url(), "https://the-internet.herokuapp.com/login")
