from read_mail import read_mails
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome('./chromedriver')
driver.get("https://stars.bilkent.edu.tr/srs")
print(driver.title)

sleep(1)

username = driver.find_element(By.ID, 'LoginForm_username')

username.send_keys("21100999")

p = driver.find_elements_by_tag_name("input")
p[1].send_keys("c717343")
#p_word = driver.find_ele#ment(By.ID, 'LoginForm-p6fc250ddad')


driver.find_element_by_name("yt0").click()

#driver.close()

