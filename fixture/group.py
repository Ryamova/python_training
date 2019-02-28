class GroupHelper:
    def __init__(self,app):
        self.app = app

    def open_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.open_group_create()
        wd.find_element_by_name("group_name").click()
        # fill group form
        self.filing_fields(group)
        # submit group creation (нажимаем кнопку сабмит)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def filing_fields(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd.find_element_by_name("selected[]").click()

    def modify(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[contains(@value,'Edit group')]").click()
        wd.find_element_by_xpath("//input[contains(@name,'group_name')]").click()
        self.filing_fields(group)
        wd.find_element_by_name("update").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        #open modification form
        wd.find_element_by_name("edit").click()
        #fill group form

        #submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()





    def open_groups_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/group.php")

    def open_group_create(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()
