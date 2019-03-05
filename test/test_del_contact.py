
from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.filling_in_contact_creation(Contact(firstname="aDA"))
        app.contact.submit_contact_creation()
    app.contact.delete_first_contact()


