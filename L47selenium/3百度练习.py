from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
driver.get('https://passport.baidu.com/v2/?login')
kw = driver.find_element_by_id('TANGRAM__PSP_3__footerULoginBtn')
kw.click()
time.sleep(3)