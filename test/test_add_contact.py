# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Ivani4",
                               company="Roga i kopita", address="Moscow", homephone="912313123123",
                               mobilephone="231231241231", email="asdasd@sdfasdasd", bday="1",
                               confirmbday="//option[@value='1']", bmonth="March",
                               confirmbmonth="//option[@value='March']", byear="1900"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
                               company="", address="", homephone="",
                               mobilephone="", email="", bday="",
                               confirmbday="//option[@value='']", bmonth="-",
                               confirmbmonth="//option[@value='-']", byear=""))
    app.session.logout()
