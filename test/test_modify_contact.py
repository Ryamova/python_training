from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify(Contact( firstname = "Ada", middlename = "dad", lastname = "Rad",
    nickname = "Red", title = "hfkkfd", company = "fgdds", address = "shnat fjndj 8", home = "89253748",
    mobile = "34567766", work = "44444", fax = "3324", email = "wweiehhc@kjdnd" ,bday = "15", bmonth = "August",
    byear = "1991", aday = "14", amonth = "November", ayear = "2302", address2 = "jdskflvbm,c78",phone2 = "jdsk48309",
    notes = "hfkdn"))
    app.contact.submit_contact_creation()
    app.session.logout()