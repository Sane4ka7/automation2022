from selenium import webdriver

driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

email_address_field = driver.find_element_by_xpath("//input[@id='input-email']")
email_address_field_class = email_address_field.get_attribute("class")
email_address_input = driver.find_element_by_id("input-email")
email_address_input.clear()
email_address_input.send_keys ("lapo4ka_7@mail.ru")

password_field = driver.find_element_by_xpath("//input[@id='input-email']")
password_field_class = password_field.get_attribute("class")
password_input = driver.find_element_by_id("input-password")
password_input.clear()
password_input.send_keys ("windows11")

loginbtn = driver.find_element_by_xpath("//input[@value='Login']")
loginbtn.click()

driver.quit()