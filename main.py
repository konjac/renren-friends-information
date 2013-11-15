#coding=utf-8
import urllib
import urllib2
import cookielib
import re
import time
import ConfigParser
import login
import jquery
import util

config = ConfigParser.ConfigParser()
config.read("config.ini")

email = config.get("account", "email")
password = config.get("account", "password")
output_file = config.get("output", "filename")

print email, password, output_file

f = open(output_file, 'w')

login.open(email, password)

html = urllib2.urlopen('http://3g.renren.com/friendlist.do').read()
page_cnt = 0
person_cnt = 0
f.write("[");
while True:
    profiles = map(lambda t : t.attrib['href'], jquery.query(html, "a[class=p]"))
    for p in profiles:
        url = p.replace("profile", "details")
        uid = re.findall(r"id=([0-9]+)", url)[0]
        print uid, person_cnt
        detail_page = urllib2.urlopen(url).read()
        name = jquery.query(detail_page, ".sec b a").text()
        res = jquery.query(detail_page, ".list")
        info = "\n".join(res.listOuterHtml());
        if len(info) == 0:
            info = u"null"
        if person_cnt>0:
            f.write(",");
        f.write("{\n");
        f.write(("\t\"%s\": %d")%("uid", int(uid)))
        f.write((",\n\t\"%s\": \"%s\"")%("Name", util.utf8_wrapper(name)))
        for s in re.findall(ur"[^>]*：[^<]*", info):
            idx = s.find(u"：");
            f.write(util.utf8_wrapper((",\n\t\"%s\": \"%s\"")%(s[0:idx], s[idx+1:])))
        time.sleep(1)
        f.write("\n}")
        f.flush()
        person_cnt = person_cnt + 1

    if html.find("下一页") == -1:
        break
    next_page = jquery.query(html, u"[title=下一页]")[0].attrib['href']
    print next_page
    html = urllib2.urlopen(next_page).read()
    page_cnt = page_cnt + 1
    time.sleep(1)
f.write("]\n")
f.close()