
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
        fixture = Application()
        request.addfinalizer(fixture.destroy)
        return fixture

def test_new_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.filling_in_contact_creation(Contact(name="gdkfhnv", header="fhhjdkjc", footer="fhghjjss"))
        app.contact.submit_contact_creation()
        app.session.logout()
        app.contact.filling_in_fields()

def test_newempty_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.filling_in_contact_creation(Contact(name="1234509", header="0987666566", footer="5656789900"))
        app.contact.submit_contact_creation()
        app.session.logout()
        app.contact.filling_in_fields()


