
def test_modif_group(app):
 app.session.login(username="admin", password="secret")
 app.group.create
 app.session.logout()

