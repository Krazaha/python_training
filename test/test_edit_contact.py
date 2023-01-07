from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(firstname="Petr", middlename="Petrovich", lastname="Petrov", nickname="Petruha",
                               company="777", address="SPb", homephone="984764532231",
                               mobilephone="82734723463", email="kldfkgjdf@ksjdfkjsjhfd", bday="5",
                               confirmbday="//option[@value='5']", bmonth="January",
                               confirmbmonth="//option[@value='January']", byear="2000"))
    app.session.logout()
