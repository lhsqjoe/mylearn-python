from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

# driver = webdriver.PhantomJS()
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
print('Title:{0}'.format(driver.title))
text = driver.find_element_by_id('wrapper').text
print(text)
print('--------------------------------------')
print(driver.title)
# 得到页面的快照
driver.save_screenshot('index.png')

print('--------------------------------------')
driver.find_element_by_id('kw').send_keys(u'大熊猫')
driver.find_element_by_id('su').click()  # 模拟click 提交
time.sleep(5)
driver.save_screenshot('demo.png')
print(driver.get_cookies())

driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')  # 模拟Ctrl+a
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')  # 模拟Ctrl+x
print('--------------------------------------')
driver.find_element_by_id('kw').send_keys(u'航空母舰')
driver.find_element_by_id('su').click()  # 模拟click 提交
time.sleep(5)
driver.save_screenshot('demo2.png')

driver.find_element_by_id('su').send_keys(Keys.RETURN)  # 模拟click 提交
time.sleep(5)
driver.save_screenshot('demo3.png')
driver.find_element_by_id('kw').clear()

driver.quit()