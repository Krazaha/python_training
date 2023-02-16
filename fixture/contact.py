from selenium.webdriver.support.ui import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_form(self, fill):
        wd = self.app.wd
        self.change_field_value("firstname", fill.firstname)
        self.change_field_value("middlename", fill.middlename)
        self.change_field_value("lastname", fill.lastname)
        self.change_field_value("nickname", fill.nickname)
        self.change_field_value("company", fill.company)
        self.change_field_value("address", fill.address)
        self.change_field_value("home", fill.homephone)
        self.change_field_value("mobile", fill.mobilephone)
        self.change_field_value("email", fill.email)
        # fill birthday
        if fill.bday is not None:
            wd.find_element_by_name("bday").click()
            Select(wd.find_element_by_name("bday")).select_by_visible_text(fill.bday)
            wd.find_element_by_xpath(fill.confirmbday).click()
        if fill.bmonth is not None:
            wd.find_element_by_name("bmonth").click()
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(fill.bmonth)
            wd.find_element_by_xpath(fill.confirmbmonth).click()
        self.change_field_value("byear", fill.byear)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, fill):
        wd = self.app.wd
        self.open_add_new_page()
        # fill contact form
        self.fill_form(fill)
        # press enter to submit adding
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_first(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        # wait home page opening
        wd.find_element_by_xpath("//input[@value='Delete']")

    def edit_first(self, fill):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contact form
        self.fill_form(fill)
        # submit edition
        wd.find_element_by_name("update").click()
        # return to home page
        wd.find_element_by_link_text("home page").click()
