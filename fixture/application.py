from selenium import webdriver
from fixture.session import SessionHelper
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def test_add_group(self):
        wd = self.wd
        self.login( username="admin", password="secret")
        self.create_group (Group(name="gdkfhnv", header="fhhjdkjc", footer="fhghjjss"))
        self.logout()

    def test_add_empty_group(self):
        wd = self.wd
        self.login( username="admin", password="secret")
        self.create_group(Group (name="", header="", footer=""))
        self.logout()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        wd.find_element_by_name("group_name").click()
        # fill group form
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation (нажимаем кнопку сабмит)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_name("new").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def destroy (self):
        self.wd.quit()