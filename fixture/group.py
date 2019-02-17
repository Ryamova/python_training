class GroupHelper:
    def __init__(self,app):
        self.app = app

    def test_add_group(self):
        wd = self.app.wd
        self.app.login(username="admin", password="secret")
        self.create(Group(name="gdkfhnv", header="fhhjdkjc", footer="fhghjjss"))
        self.app.logout()

    def test_add_empty_group(self):
        wd = self.app.wd
        self.app.login(username="admin", password="secret")
        self.create(Group(name="", header="", footer=""))
        self.app.logout()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
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
        wd = self.app.wd
        wd.find_element_by_name("new").click()
