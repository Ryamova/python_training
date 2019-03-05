
from selenium.webdriver.support.ui import Select
from model.contact import Contact



class ContactHelper:
    def __init__(self,app):
        self.app = app

    def filling_in_fields(self,contact):
        wd = self.app.wd
        self.fill_contact_form(contact)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value_day("bday", contact.bday)
        self.change_field_value_day("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_value_day("aday", contact.aday)
        self.change_field_value_day("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value_day(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_xpath("//option[@value='" + text + "']").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_add_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_link_text("groups").click()

    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        #self.return_to_add_new()
        self.open_contact_creation()


    def filling_in_contact_creation(self, contact):
        wd = self.app.wd
        self.open_contact_creation()
        self.filling_in_fields(contact)


    def filling_new_contact_creation(self, contact):
        wd = self.app.wd
        self.open_contact_creation()
        self.filling_in_fields()


    def open_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href='edit.php']").click()


    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//a[contains(@href,'edit.php?id=')]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.open_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify(self,contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[contains(@title,'Edit')]").click()
        self.filling_in_fields(contact)
        wd.find_element_by_xpath("//input[@name='update']").click()
        self.open_home_page()

    def modify_first_contact(self,new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        #open modification form
        wd.find_element_by_xpath("//img[contains(@title,'Edit')]").click()
        #fill contact form
        self.fill_contact_form(new_contact_data)
        #submit modification
        wd.find_element_by_xpath("//input[@name='update']").click()
        self.open_home_page()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))


    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php")):
            array = wd.find_elements_by_name("searchstring")
            if len(array) > 0:
                for element in array:
                    element.click()

        wd.get("http://localhost/addressbook")

    def destroy (self):
        self.app.wd.quit()

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements_by_name("selected[]"):
            text = element.text
            id = element.get_attribute("value")
            contacts.append(Contact(lastname = text, id = id))
        return contacts
