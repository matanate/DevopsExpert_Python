from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=chrome_options
)
driver.implicitly_wait(5)

# driver.get("https://rahulshettyacademy.com/angularpractice/")
# dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
# driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys("Matan")
# driver.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys("Matan@gmail.com")
# driver.find_element(By.ID, "exampleCheck1").click()
# driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
# driver.find_element(By.XPATH, '//input[@type="submit"]').click()
# message = driver.find_element(By.CSS_SELECTOR, ".alert-success").text
# print(message)

# driver.get("https://rahulshettyacademy.com/client")
# driver.find_element(By.CSS_SELECTOR, ".forgot-password-link").click()


# driver.find_element(By.XPATH, "//input[@type='email']").send_keys("matan@email.com")
# driver.find_element(By.ID, "userPassword").send_keys("123456")
# driver.find_element(By.ID, "confirmPassword").send_keys("123456")
# driver.find_element(By.XPATH, "//input[//button[@type='submit']]").click()
# message = driver.find_element(By.CSS_SELECTOR, ".toast-message").text
# print(message)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
# for checkbox in checkboxes:
#     check_val = checkbox.get_attribute("value")
#     if check_val == "option2" or check_val == "option3":
#         checkbox.click()
# for checkbox in checkboxes:
#     check_val = checkbox.get_attribute("value")
#     if check_val == "option2" or check_val == "option3":
#         assert checkbox.is_selected(), "Checkbox is not selected"
# print("Checkboxes Passed!")

# radios = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
# for radio in radios:
#     check_val = radio.get_attribute("value")
#     if check_val == "radio2" or check_val == "radio3":
#         radio.click()
# for radio in radios:
#     check_val = radio.get_attribute("value")
#     if check_val == "radio2" or check_val == "radio3":
#         assert radio.is_selected(), "Radio is not selected"
# print("Radios Passed!")


assert driver.find_element(
    By.ID, "displayed-text"
).is_displayed(), "Display Text is not displayed"

driver.find_element(By.ID, "hide-textbox").click()

assert not driver.find_element(
    By.ID, "displayed-text"
).is_displayed(), "Text is displayed"
print("Passed!")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.ID, ".promoInfo")))
