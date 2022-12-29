# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new(app):
    app.login(username="admin", password="secret")
    app.add_new_creating(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Ivani4",
                              company="Roga i kopita", address="Moscow", homephone="912313123123",
                              mobilephone="231231241231", email="asdasd@sdfasdasd", bday="1",
                              confirmbday="//option[@value='1']", bmonth="March",
                              confirmbmonth="//option[@value='March']", byear="1900"))
    app.logout()

def test_add_empty_new(app):
    app.login(username="admin", password="secret")
    app.add_new_creating(Contact(firstname="", middlename="", lastname="", nickname="",
                              company="", address="", homephone="",
                              mobilephone="", email="", bday="",
                              confirmbday="//option[@value='']", bmonth="-",
                              confirmbmonth="//option[@value='-']", byear=""))
    app.logout()
