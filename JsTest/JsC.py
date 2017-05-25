from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r'C:\Users\itzhacs\Desktop\python\phantomjs-2.1.1-windows\bin\phantomjs.exe')  # PhantomJs
targetUrl = "http://www.tse.com.tw/ch/trading/indices/MI_5MINS_HIST/MI_5MINS_HIST.php"
driver.get('http://www.tse.com.tw/zh/page/trading/indices/MI_5MINS_HIST.html')  # 輸入範例網址，交給瀏覽器 
pageSource = driver.page_source  # 取得網頁原始碼
print(pageSource)

driver.close()  # 關閉瀏覽器

