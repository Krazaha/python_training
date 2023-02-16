from model.group import Group

def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="sdfsdfsdf", header="sdf234", footer="11111asdas123fg"))

def test_edit_first_group_name(app):
    app.group.edit_first_group(Group(name="New name"))

def test_edit_first_group_header(app):
    app.group.edit_first_group(Group(name="New header"))
