from model.group import Group

def test_modif_group(app):
 app.session.login(username="admin", password="secret")
 app.group.modify(Group(name="A", header="", footer=""))
 app.session.logout()

