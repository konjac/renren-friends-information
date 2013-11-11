#coding=utf-8
import urllib
import urllib2
import cookielib
import re
import time
import ConfigParser
import login

config = ConfigParser.ConfigParser()
config.read("config.ini")

email = config.get("account", "email")
password = config.get("account", "password")
output_file = config.get("IO", "output")

print email, password, output_file

f = open(output_file, 'w')

login.open(email, password)

html = urllib2.urlopen('http://3g.renren.com/friendlist.do').read()
cnt = 0

while html.find("下一页")<>-1:
    profiles = re.findall('<tr valign="top"><td><a href="(http://3g.renren.com/profile.do\?id=[0-9]*)', html)

    for p in profiles:
        url = p.replace("profile", "details")
        detail_page = urllib2.urlopen(url).read()
        name = re.findall(r'<b><a href="http://3g.renren.com/profile.do\?[\S]*">([\S]*)</a>', detail_page)[0] 
        res = re.findall(r'(<div class="list">[\S ]*</div>)<div class="sec">', detail_page)
        if len(res) == 0:
            info = "null"
        else:
            info = res[0]
        print name
        print info
        f.write(name)
        f.write("\n")
        f.write(info)
        time.sleep(1)
        f.write("\n")
        
    next_page = re.findall(r'"(http://3g.renren.com/friendlist.do\?curpage=[\S]*)"', html)[0]
    html = urllib2.urlopen(next_page).read()
    if cnt==1:
        break
    cnt = cnt + 1
    time.sleep(1)