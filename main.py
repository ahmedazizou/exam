from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")

driver.find_element_by_id("file-upload").send_keys("C://Users/theze/OneDrive/Bureau/olux/pic.jpg")
driver.find_element_by_id("file-submit").click()