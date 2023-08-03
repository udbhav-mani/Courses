from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

WebDriverWait(self.browser, 10).until(
    expected_conditions.presence_of_element_located(By.CSS_SELECTOR, locator)
)

# by has various things like id etc
