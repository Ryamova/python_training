from model.contact import Contact

def test_modif_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify(Contact(firstname="s", middlename="", lastname="", nickname="", title="", company="", address="",
                    home="", mobile="", work="", fax="", email="",bday="15", bmonth="August", byear="1991", aday="14",
                    amonth="November", ayear="2302", address2="", phone2="", notes=""))
    app.session.logout()
