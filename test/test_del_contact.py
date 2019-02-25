

def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.contact.submit_contact_creation()
    app.session.logout()
    app.contact.filling_in_fields()
