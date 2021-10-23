@[TOC](python爬虫：获取选集内容，并转换成csdn标题的形式，方便做笔记)
# 效果展示
python爬虫结果
![在这里插入图片描述](https://img-blog.csdnimg.cn/e0edd1567369467189d1836a0069fa3e.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBASmVmZnJleUxlYWw=,size_20,color_FFFFFF,t_70,g_se,x_16)

直接复制到csdn的markdown编辑器就可以用了
![在这里插入图片描述](https://img-blog.csdnimg.cn/96ad212b668d4366b71fd473459ad7ac.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBASmVmZnJleUxlYWw=,size_20,color_FFFFFF,t_70,g_se,x_16)


由于审核问题，爬的是哪个学习网站的视频就自己体会了。
# 代码

代码地址：[https://github.com/JeffreyLeal/MyUtils/tree/%E7%88%AC%E8%99%AB%E5%B7%A5%E5%85%B71](https://github.com/JeffreyLeal/MyUtils/tree/%E7%88%AC%E8%99%AB%E5%B7%A5%E5%85%B71)，需要安装selenium包才能运行代码。

代码源自: [这里](https://blog.csdn.net/pdcfighting/article/details/120446254)。他的代码没什么问题，只是在他已有的基础上做了一点点修改。爬虫使用的浏览器是chrome，他的文章没有详细说明具体怎么配置，这个文章讲述了怎么配置驱动的下载与配置 [解决：'chromedriver' executable needs to be in PATH问题](https://blog.csdn.net/weixin_41990913/article/details/90936149).
# 爬虫浏览器chrome安装
解决浏览器更新导致驱动版本不匹配的方法如下：
这个链接可以下载指定的chrome浏览器版本: [下载指定的浏览器版本](https://chromium.cypress.io/).

但由于chrome自带更新，导致驱动升级跟不上，很容易造成爬虫失败：
设置chrome不自动更新: [如何禁止Chrome浏览器版本自动更新的方法](https://blog.csdn.net/ffffffff8/article/details/104003450).


