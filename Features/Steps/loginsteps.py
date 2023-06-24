from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I have navigated to webpage')
def step_impl(context):
    pass


@when('I have enter the product name')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name='search']").send_keys('HP')


@then('I have click on search')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[@id='search']//button[@type='button']").click()
