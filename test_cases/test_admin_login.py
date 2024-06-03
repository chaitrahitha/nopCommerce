import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

from base_pages.Login_Admin_Page import Login_Admin_Page


class Test_01_Admin_Login:
    admin_page_url = "https://admin-demo.nopcommerce.com/login"
    username = "admin@yourstore.com"
    password = "admin"
    invalid_username = "admin123@yourstore.com"
    invalid_password = "addmin"

    def test_title_verification(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "Your store. Login"
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_valid_admin_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        #to pass user name, we can create object for login admin page class
        self.admin_lp = Login_Admin_Page(self.driver)
        #we have to use self keyword bcoz it is class variable, if we want to access the class variable inside the method we have to use self keyword

        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        act_msg = self.driver.find_element(By.XPATH,"//div[@class='content-header']/h1").text
        if act_msg == "Dashboard":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_invalid_admin_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        #to pass user name, we can create object for login admin page class
        self.admin_lp = Login_Admin_Page(self.driver)
        #we have to use self keyword bcoz it is class variable, if we want to access the class variable inside the method we have to use self keyword

        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        title = self.driver.find_element(By.XPATH,"//strong[text()='Welcome, please sign in!']")
        error_msg = self.driver.find_element((locate_with(By.TAG_NAME,"li")).above(title)).text
        if error_msg == "No customer account found":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False