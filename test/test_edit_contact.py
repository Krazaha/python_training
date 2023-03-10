from model.contact import Contact

def test_edit_first_contact(app):
    app.contact.edit_first(Contact(firstname="Petr", middlename="Petrovich", lastname="Petrov", nickname="Petruha",
                               company="777", address="SPb", homephone="984764532231",
                               mobilephone="82734723463", email="kldfkgjdf@ksjdfkjsjhfd", bday="5",
                               confirmbday="//option[@value='5']", bmonth="January",
                               confirmbmonth="//option[@value='January']", byear="2000"))

def test_edit_first_contact_name(app):
    app.contact.edit_first(Contact(firstname="NewPetr", middlename="NewPetrovich", lastname="NewPetrov"))

def test_edit_first_contact_phone(app):
    app.contact.edit_first(Contact(homephone="911"))
