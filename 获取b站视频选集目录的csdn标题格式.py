# -*- codeing = utf-8 -*-
# @Time :2021/10/20 15:19
# @Author:JeffreyLeal
# @File : 获取b站视频选集目录的csdn标题格式.py
# @Software: PyCharm

# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Item:
    page_num = ""
    part = ""
    duration = ""

    def __init__(self, page_num, part, duration):
        self.page_num = page_num
        self.part = part
        self.duration = duration

    def get_second(self):
        str_list = self.duration.split(":")
        sum = 0
        for i, item in enumerate(str_list):
            sum += pow(60, len(str_list) - i - 1) * int(item)

        return sum

    # def show_item_csdn_content_format(self):



def get_bilili_page_items(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 设置无界面
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2,
    #                                           "profile.managed_default_content_settings.flash": 0})

    browser = webdriver.Chrome(options=options)
    # browser = webdriver.PhantomJS()
    print("正在打开网页...")
    browser.get(url)

    print("等待网页响应...")
    # 需要等一下，直到页面加载完成
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="list-box"]/li/a')))

    print("正在获取网页数据...")
    list = browser.find_elements_by_xpath('//*[@class="list-box"]/li')
    # print(list)
    itemList = []

    second_sum = 0

    # 2.循环遍历出每一条搜索结果的标题
    for t in list:
        # print("t text:",t.text)
        element = t.find_element_by_tag_name('a')
        # print("a text:",element.text)
        arr = element.text.split('\n')

        # 以csdn目录的格式输出，把 'p1','p1的标题'，'视频长度' -> '#','p1','p1的标题'
        arr[0], arr[1], arr[2] = '#', arr[0], arr[1]

        print(" ".join(arr))

        item = Item(arr[0], arr[1], arr[2])
        # 计算时长
        # second_sum += item.get_second()

        itemList.append(item)

    # print("总数量:", len(itemList))
    # browser.page_source

    # 显示时长
    # print("总时长/分钟:", round(second_sum / 60, 2))
    # print("总时长/小时:", round(second_sum / 3600.0, 2))

    browser.close()

    return itemList

#此处输入b站视频地址，需要安装chrome浏览器
url = "https://www.bilibili.com/video/BV1hE411t7RN"
get_bilili_page_items(url)