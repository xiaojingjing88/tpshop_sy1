
class TestLogin:

    def setup(self):
        self.driver = init_driver()

    def teardown(self):
        self.driver.quit()

    def test_pytest1(self):
        print("test_login")
