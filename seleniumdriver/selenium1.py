#coding:utf-8
import time
from selenium import  webdriver


#driver=webdriver.Firefox()   #火狐浏览器
#firefox=webdriver.Ie()  IE浏览器
driver=webdriver.Chrome()   #谷歌浏览器

url='http://www.baidu.com'
driver.get(url)
html = driver.page_source
print('------访问页面获取到html内容如下:')
print(html)

time.sleep(3)

#关闭浏览器
driver.close()