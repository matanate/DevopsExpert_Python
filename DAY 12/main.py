import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(
#     service=ChromeService(ChromeDriverManager().install()), options=chrome_options
# )
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# action = ActionChains(driver)
# action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# action.move_to_element(driver.find_element(By.LINK_TEXT, "Top")).click().perform()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=chrome_options
)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/shop")
items = driver.find_elements(By.CSS_SELECTOR, ".zmdi")
items[0].click()
items[3].click()
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
driver.find_element(By.CSS_SELECTOR, "#country").send_keys("Ind")
wait = WebDriverWait(driver, 10)
wait.until(
    expected_conditions.presence_of_element_located((By.LINK_TEXT, "India"))
).click()
driver.find_element(By.CSS_SELECTOR, ".checkbox-primary").click()
driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
message = driver.find_element(By.CSS_SELECTOR, ".alert").text)
assert "Success!" in message, "Test failed"
print("Passed")