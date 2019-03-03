from model.contact import Contact


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="Kati"))


def test_modify_contact_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="Ooo"))
