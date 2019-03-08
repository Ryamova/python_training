from model.contact import Contact


def test_modify_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    contacts = Contact(firstname="Kati")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(Contact(firstname="Kati"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_contact_lastname(app):
    #if app.contact.count() == 0:
        #app.contact.filling_in_contact_creation(Contact(firstname="RITA"))
        #app.contact.submit_contact_creation()
    #old_contacts = app.contact.get_contact_list()
    #app.contact.modify_first_contact(Contact(lastname="Ooo"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)