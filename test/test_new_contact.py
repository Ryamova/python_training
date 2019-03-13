
import pytest
from model.contact import Contact
from fixture.application import Application
from sys import maxsize

def test_new_contact(app):
        old_contacts = app.contact.get_contact_list()
        contact = Contact(firstname = "Ada", middlename = "dad", lastname = "Rad",
                 nickname = "Red", title = "hfkkfd", company = "fgdds", address = "shnat fjndj 8", home = "89253748",
                 mobile = "34567766", work = "44444", fax = "3324", email = "wweiehhc@kjdnd",bday = "15", bmonth = "August",
                 byear = "1991", aday = "14", amonth = "November", ayear = "2302", address2 = "jdskflvbm,c78",
                 phone2 = "jdsk48309", notes = "hfkdn")
        app.contact.filling_in_contact_creation(contact)
        app.contact.submit_contact_creation()
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts.append(contact)
        def id_or_max(ct):
            if ct.id:
                return int(ct.id)
            else:
                return maxsize
        assert sorted(old_contacts,key = id_or_max) == sorted(new_contacts,key = id_or_max)



#def test_newempty_contact(app):
        #old_contacts = app.contact.get_contact_list()
        #app.contact.filling_in_contact_creation(Contact(firstname = "", middlename = "", lastname = "",
                 #nickname = "", title = "", company = "", address = "", home = "",
                 #mobile = "", work = "", fax = "", email = "",bday = "15", bmonth = "August",
                 #byear = "1991", aday = "14", amonth = "November", ayear = "2302", address2 = "",
                 #phone2 = "", notes = ""))
        #app.contact.submit_contact_creation()
        #new_contacts = app.contact.get_contact_list()
        #assert len(old_contacts) + 1 == len(new_contacts)





