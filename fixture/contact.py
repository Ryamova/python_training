from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper


class ContactHelper:
    def __init__(self,app):
        self.app = app

    def filling_in_fields(self):
        wd = self.app.wd
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        # заполнение информации о контакте
        wd.find_element_by_name("firstname").send_keys("Ada")
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("dad")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Rad")
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("Red")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("hfkkfd")
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("fgdds")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("shnat fjndj 8")
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("89253748")
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("34567766")
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("44444")
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("3324")
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("wweiehhc@kjdnd")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("15")
        wd.find_element_by_xpath("//option[@value='15']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("August")
        wd.find_element_by_xpath("//option[@value='August']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1991")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("14")
        wd.find_element_by_xpath("(//option[@value='14'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("November")
        wd.find_element_by_xpath("(//option[@value='November'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2302")
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("jdskflvbm,c78")
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("jdsk48309")
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("hfkdn")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home page").click()
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")

    def return_to_add_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_link_text("groups").click()

    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()
        self.return_to_add_new()

    def filling_in_contact_creation(self, contact):
        wd = self.app.wd
        self.open_contact_creation()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(contact.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(contact.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(contact.footer)

    def open_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//a[contains(@href,'edit.php?id=')]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.open_home_page()
        #self.return_to_add_new()

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook")

    def destroy (self):
        self.app.wd.quit()