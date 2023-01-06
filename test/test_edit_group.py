from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="sdfsdfsdf", header="sdf234", footer="11111asdas123fg"))
    app.session.logout()
