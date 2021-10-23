# -*- codeing = utf-8 -*-
# @Time :2021/10/20 15:19
# @Author:JeffreyLeal
# @File : 获取某站视频选集目录的csdn标题格式.py
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

def get_bilili_page_items(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 设置无界面
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    browser = webdriver.Chrome(options=options)

    print("正在打开网页...")
    browser.get(url)

    print("等待网页响应...")
    # 需要等一下，直到页面加载完成
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="list-box"]/li/a')))

    print("正在获取网页数据...\n")

    # 获取视频总集标题.
    title = browser.find_element(by=By.XPATH, value='//*[@class="tit tr-fix"]').text # 获取该页面所有标题跟视频链接
    print('@[TOC]('+title+' 笔记)')
    print('# 教程与代码地址')
    print('笔记中，图片和代码基本源自up主的视频和代码\n')
    print('视频地址: [' + title + ']('+ url + ')')
    print('代码地址: []()')
    print('讲义地址：[]()')
    print('如果想要爬虫视频网站一样的csdn目录，可以去这里下载代码：[https://github.com/JeffreyLeal/MyUtils/tree/%E7%88%AC%E8%99%AB%E5%B7%A5%E5%85%B71](https://github.com/JeffreyLeal/MyUtils/tree/%E7%88%AC%E8%99%AB%E5%B7%A5%E5%85%B71)')


    # 获取视频分集标题列表
    list = browser.find_elements(by=By.XPATH, value='//*[@class="list-box"]/li')
    # print(list)
    itemList = []

    second_sum = 0

    # 2.循环遍历出每一条搜索结果的标题
    for t in list:
        # print("t text:",t.text)
        element = t.find_element(by=By.TAG_NAME, value='a')
        # print("a text:",element.text)
        arr = element.text.split('\n')

        # 以csdn目录的格式输出，把 'p1','p1的标题'，'视频长度' -> '#','p1','p1的标题'
        # arr[0], arr[1], arr[2] = '#', arr[0], arr[1]
        print("# " + arr[0] + ' ' + arr[1])

        item = Item(arr[0], arr[1], arr[2])

        # 计算时长
        # second_sum += item.get_second()
        # itemList.append(item)

    # print("总数量:", len(itemList))

    # 显示时长
    # print("总时长/分钟:", round(second_sum / 60, 2))
    # print("总时长/小时:", round(second_sum / 3600.0, 2))

    browser.close()

    return itemList

#此处输入b站视频地址，需要安装chrome浏览器
url = "https://www.bilibili.com/video/BV1LA411n73X"
get_bilili_page_items(url)
