#请在校园网环境使用，适用于研究生课程补退改选捡漏
from typing import Optional
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import datetime 
chrome_options = Options()
#使用此行取消gui
#chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

while True:
    try:
        
        browser.get("http://gsmis.yjsxk.buaa.edu.cn/")
        if browser.title=="统一身份认证":
            browser.switch_to_frame("loginIframe")
            username=browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div[2]/div[1]/div[1]/div/input')
            password=browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/input')
            username.send_keys("你的账号名")
            password.send_keys("你的密码")
            confirm=browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div[2]/div[1]/div[7]/input')
            confirm.click()
            browser.switch_to.default_content()
        while True:
            browser.get("http://gsmis.yjsxk.buaa.edu.cn/yjsxkapp/sys/xsxkappbuaa/index.html")
            time.sleep(0.2)
            browser.find_element_by_xpath('//*[@id="courseBtn"]').click()
            time.sleep(0.2)
            browser.find_element_by_xpath('/html/body/div/article[2]/div[2]/div/ul/li[2]').click()#这个地方换成你要选的那个课的类别的全路径xpath
            time.sleep(0.2)
            all=browser.find_elements_by_class_name("xkbtn")
            found=False
            for i in range(0,len(all)):
                if all[i].get_attribute('role-kcms')=="06112301-算法设计与分析（1）":#此处填要抢的课的名称
                    all[i].click()
                    time.sleep(0.2)
                    browser.find_element_by_xpath("/html/body/div[3]/div[6]/div/button[1]").click()
                    found=True
            if found:
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"tried")
            else:
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"class not found")
    except BaseException as e:
        print(e)

