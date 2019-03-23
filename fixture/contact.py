
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
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value_day("bday", contact.bday)
        self.change_field_value_day("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_value_day("aday", contact.aday)
        self.change_field_value_day("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.secondaryphone)
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
        self.contact_cache = None


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
        self.delete_contact_by_index(0)

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        self.edit_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.open_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify(self,contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[contains(@title,'Edit')]").click()
        self.filling_in_fields(contact)
        wd.find_element_by_xpath("//input[@name='update']").click()
        self.open_home_page()

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        #open modification form
        self.edit_contact_by_index(index)
        #fill contact form
        self.fill_contact_form(new_contact_data)
        #submit modification
        wd.find_element_by_xpath("//input[@name='update']").click()
        self.open_home_page()
        self.contact_cache = None

    def edit_contact_by_index(self,index):
        wd = self.app.wd
        c = 0
        for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
            if c == index:
                element.find_elements_by_tag_name("td")[7].find_element_by_tag_name("img").click()
            c = c + 1

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

    contact_cache = None


    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                tds = element.find_elements_by_tag_name("td")
                lastName = tds[1].text
                firstName = tds[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones=tds[5].text.splitlines()

                homephone = ''
                if len(all_phones) > 0: homephone = all_phones[0]
                mobilephone = ''
                if len(all_phones) > 1: mobilephone = all_phones[1]
                workphone = ''
                if len(all_phones) > 2: workphone = all_phones[2]
                secondaryphone = ''
                if len(all_phones) > 3: secondaryphone = all_phones[3]

                self.contact_cache.append(Contact(firstname=firstName, lastname=lastName, id=id,
                                                  homephone=homephone,mobilephone=mobilephone,
                                                  workphone=workphone,secondaryphone=secondaryphone))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.edit_contact_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact (firstname=firstname,lastname=lastname,id=id,
                        homephone=homephone,workphone=workphone,mobilephone=mobilephone,secondaryphone=secondaryphone)
