@[TOC](使用Python网络爬虫获取B站视频选集内容，并转换成csdn标题的形式，方便做笔记（附源码）)
# 效果展示
python爬虫结果
![在这里插入图片描述](https://img-blog.csdnimg.cn/6d716c63035a4aedb978980c07312cbb.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBASmVmZnJleUxlYWw=,size_20,color_FFFFFF,t_70,g_se,x_16)
直接复制到csdn的markdown编辑器就可以用了
![在这里插入图片描述](https://img-blog.csdnimg.cn/d17f245f46da411e8f2f8b0282404b63.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBASmVmZnJleUxlYWw=,size_20,color_FFFFFF,t_70,g_se,x_16)


# 代码



代码源自: [手把手教你使用Python网络爬虫获取B站视频选集内容（附源码）](https://blog.csdn.net/pdcfighting/article/details/120446254).他的代码没什么问题，只是在他已有的基础上做了一点点修改。爬虫使用的浏览器是chrome，但由于chrome自带更新，导致驱动升级跟不上，很容易造成爬虫失败，他的文章没有详细说明具体怎么操作，所以我寻找了解决浏览器更新导致驱动版本不匹配的方法如下：
# 爬虫浏览器chrome安装
这个链接可以下载指定的chrome浏览器版本: [下载指定的浏览器版本](https://chromium.cypress.io/).
设置chrome不自动更新: [如何禁止Chrome浏览器版本自动更新的方法](https://blog.csdn.net/ffffffff8/article/details/104003450).
驱动的下载与配置 [解决：'chromedriver' executable needs to be in PATH问题](https://blog.csdn.net/weixin_41990913/article/details/90936149).


