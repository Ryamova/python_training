from model.contact import Contact


def test_modify_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Kati"))
    app.session.logout()

def test_modify_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(lastname="Ooo"))
    app.session.logout()