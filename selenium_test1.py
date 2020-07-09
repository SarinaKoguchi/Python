from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://a-force.biz/index.aspx")

show = driver.find_element_by_id("show")
show.click()

driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
form = driver.find_element_by_id("tweet")
form.send_keys("こんにちは" + Keys.ENTER)

time.sleep(5)
form.send_keys("新卒採用" + Keys.ENTER)

time.sleep(5)
answer = driver.find_element_by_xpath("//*[@id='field']/div[5]/div[2]/div[2]/div").text
print(answer)

driver.close()