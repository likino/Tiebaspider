# -*- coding:utf-8 -*-
#------------------------
# 程序：百度贴吧爬虫
# 版本：1.0
# 作者：lee
# 日期：2015-03-27
# 语言：Python 2.7
# 功能：下载对应页码内的所有页面并存储为html文件
#------------------------

import string, urllib2

#定义百度函数
def baidu_tieba(url,begin_page,end_page):
	for i in range(begin_page,end_page+1):
		sName = string.zfill(i,5) + '.html' #自动填充成六位文件名
		print 'Download ' + str(i) + ' page, and save ' + sName + '......'
		f = open(sName,'w+')
		m = urllib2.urlopen(url + str(i)).read()
		f.write(m)
		f.close()
		
#-------这里输入参数--------



bdurl = str(raw_input('tieba dizhi except pn=:\n'))
begin_page = int(raw_input('beginpage?:\n'))
end_page = int(raw_input(u'endpage?:\n'))

baidu_tieba(bdurl,begin_page,end_page)