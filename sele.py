from read_mail import read_mails
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from credits import id, moddle_p, mail_adr, mail_p
driver = webdriver.Chrome('/home/omergenc/TEST_BOARD/forSelenium/folder1/chromedriver')
driver.get("https://stars.bilkent.edu.tr/srs")
print(driver.title)

sleep(1)


username = driver.find_element(By.ID, 'LoginForm_username')

username.send_keys(id)

p = driver.find_elements_by_tag_name("input")
p[1].send_keys(moddle_p)
#p_word = driver.find_ele#ment(By.ID, 'LoginForm-p6fc250ddad')


driver.find_element_by_name("yt0").click()
sleep(1)

confirmation_code = driver.find_element_by_id("EmailVerifyForm_verifyCode")

confirmation_code.send_keys(read_mails(mail_adr,mail_p)[1])

driver.find_element_by_name("yt0").click()# confirmation code submit








#driver.close()

