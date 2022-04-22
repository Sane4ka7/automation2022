from selenium import webdriver

driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()

logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

newregistrantbtn = driver.find_element_by_xpath("//a[contains(text(), 'Continue')]")
newregistrantbtn.click()

firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class

firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.clear()
firstname_input.send_keys ("Alexandra")

lastname_field = driver.find_element_by_xpath("//fieldset/div[2]")
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class
lastname_input = driver.find_element_by_id("input-lastname")
lastname_input.clear()
lastname_input.send_keys ("Dereveaschin")

email_field = driver.find_element_by_xpath("//fieldset/div[2]")
email_field_class = email_field.get_attribute("class")
assert "required" in email_field_class
email_input = driver.find_element_by_id("input-email")
email_input.clear()
email_input.send_keys ("lapo4ka_7@mail.ru")

telephone_field = driver.find_element_by_xpath("//fieldset/div[2]")
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class
telephone_input = driver.find_element_by_id("input-telephone")
telephone_input.clear()
telephone_input.send_keys ("2315220020")

address_1_field = driver.find_element_by_xpath("//fieldset/div[2]")
address_1_field_class = address_1_field.get_attribute("class")
assert "required" in address_1_field_class
address_1_input = driver.find_element_by_id("input-address-1")
address_1_input.clear()
address_1_input.send_keys ("25 Blue Avenue")

city_field = driver.find_element_by_xpath("//fieldset/div[2]")
city_field_class = city_field.get_attribute("class")
assert "required" in city_field_class
city_input = driver.find_element_by_id("input-city")
city_input.clear()
city_input.send_keys ("Lancaster")

password_field = driver.find_element_by_xpath("//fieldset/div[2]")
password_field_class = password_field.get_attribute("class")
assert "required" in password_field_class
password_input = driver.find_element_by_id("input-password")
password_input.clear()
password_input.send_keys ("pirojok777")

password_confirm_field = driver.find_element_by_xpath("//fieldset/div[2]")
password_confirm_field_class = password_confirm_field.get_attribute("class")
assert "required" in password_confirm_field_class
password_confirm_input = driver.find_element_by_id("input-confirm")
password_confirm_input.clear()
password_confirm_input.send_keys ("pirojok777")

driver.quit()

