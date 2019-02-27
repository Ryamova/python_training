

def test_modif_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modif_contact
    app.session.logout()
