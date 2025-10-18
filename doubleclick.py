import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_double_click(driver):
    driver.get("https://demo.guru99.com/test/simple_context_menu.html")

    action = ActionChains(driver)
    button = driver.find_element(By.XPATH, "//button[text()='Double-Click Me To See Alert']")
    action.double_click(button).perform()

    time.sleep(2)

    alert = driver.switch_to.alert
    assert alert.text == "You double clicked me.. Thank You.." 
    print("Alert text:", alert.text)
    alert.accept()