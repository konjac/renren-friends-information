#coding=utf-8
import urllib
import urllib2
import cookielib
import re
import time
import login
import jquery

def open(email, password):

    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    urllib2.install_opener(opener)

    html = urllib2.urlopen('http://m.renren.com').read()
    
    img, verifykey = None, None 
    xn = {}
    xn['email'] = email
    xn['password'] = password
    try:
        img = jquery.query(html, "img")[1].attrib['src'];
        verifykey = jquery.query(html, "input[name=verifykey]")[0].attrib['value']
        print img
        verifycode = raw_input("please visit the above url in your browser, and type the verify code on the page:\n")
        xn['verifycode'] = verifycode
        xn['verifykey'] = verifykey
    except:
        pass

    #print xn
    
    data = urllib.urlencode(xn)
    req = urllib2.Request('http://3g.renren.com/login.do?fx=0&autoLogin=true', data)
    resp = urllib2.urlopen(req)
    return resp.read()
