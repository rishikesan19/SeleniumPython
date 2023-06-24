import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def before_scenario(context,driver):

    browser_name = "chrome"
    service_obj = Service("Driver/chrome.exe")
    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome(service=service_obj)
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")

# def after_scenario(context,driver):
#     context.driver.quit()

def after_step(context,step):
    if step.status == 'passed':
        allure.attach(context.driver.get_screenshot_as_png()
                      ,name="passed_screenshot"
                      ,attachment_type=AttachmentType.PNG)