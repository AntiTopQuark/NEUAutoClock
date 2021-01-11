# 东北大学 自动健康信息上报

from selenium import webdriver
import time
from selenium.webdriver import ActionChains


from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument('--no-sandbox')
option.add_argument('--headless')

def run(username ,userpwd):
    browser = webdriver.Chrome(chrome_options=option)
    browser.get(
        'https://webvpn.neu.edu.cn/https/77726476706e69737468656265737421f5ba5399373f7a4430068cb9d6502720645809/notes/create')
    time.sleep(5)
    # 登录
    browser.find_element_by_id("un").send_keys(username)
    browser.find_element_by_id("pd").send_keys(userpwd)
    browser.find_element_by_id("index_login_btn").click()
    print("登录成功")
    # 跳转后 打卡
    browser.implicitly_wait(3)
    # 是本人
    element = browser.find_element_by_name("jibenxinxi_shifoubenrenshangbao")
    ActionChains(browser).move_to_element(element).click().perform()  # 使用鼠标点击的方式
    time.sleep(1)
    # 目前身体健康正常
    element = browser.find_element_by_name("jiankangxinxi_muqianshentizhuangkuang")
    ActionChains(browser).move_to_element(element).click().perform()  # 使用鼠标点击的方式
    time.sleep(1)
    # 当前位置无变化
    element = browser.find_element_by_xpath('//*[@id="app"]/main/div/form/div[4]/div[2]/table/tbody/tr[1]/td/div/div/div/label[1]')
    ActionChains(browser).move_to_element(element).click().perform()  # 使用鼠标点击的方式
    time.sleep(1)

    # 提交
    element = browser.find_element_by_css_selector(".el-button.el-button--primary")
    ActionChains(browser).move_to_element(element).click().perform()  # 使用鼠标点击的方式
    # 完成
    time.sleep(3)
    print("打卡成功")

if __name__ == '__main__':

    username = "20XX****"
    userpwd = "*********"
    run(username,userpwd)
