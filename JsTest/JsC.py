from selenium import webdriver
from selenium.webdriver.support.ui import Select
import bs4

driver = webdriver.PhantomJS(executable_path=r'C:\Users\rexc\Desktop\Py\GitHub\Web\phantomjs-2.1.1-windows\bin\phantomjs.exe')  # PhantomJs
targetUrl = 'http://www.tse.com.tw/zh/page/trading/indices/MI_5MINS_HIST.html'
#targetUrl = 'http://www.tse.com.tw/indicesReport/MI_5MINS_HIST?response=json&date=20170101&_=1495807136988'
#targetUrl = "http://www.cnyes.com/twfutures/option/option_realtime_sc.asp"
#targetUrl = "https://www.google.com.tw/"
driver.get(targetUrl)  # 輸入範例網址，交給瀏覽器 
'''
element = driver.find_element_by_xpath("//select[@name='yy']")
all_options = element.find_elements_by_tag_name("option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("value"))
    '''
select = Select(driver.find_element_by_name('yy'))
'''
for o in select.options:
    print(o.get_attribute("value"))
'''
select.select_by_value("2012")    
target = driver.find_element_by_class_name("main")
target.click()
#print(select.options)
#print("Value is: %s" % select.get_attribute("value"))
#select.select_by_value(1)
'''
inputElement = driver.find_element_by_name("q")
inputElement.send_keys("cheese!")
inputElement.submit() # 提交
'''
#select.select_by_index(1)
pageSource = driver.page_source  # 取得網頁原始碼
#print(pageSource)
soup = bs4.BeautifulSoup(pageSource, 'html.parser')
tb = soup.select('#report-table > tbody > tr > td')
#print(soup.prettify('utf-8'))
for element in tb:
    #print(element.get_text())
    target = element.get_text()
    print(target)

driver.close()  # 關閉瀏覽器

