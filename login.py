#coding=utf-8
import urllib
import urllib2
import cookielib
import re
import time
def open(email, password):

    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    urllib2.install_opener(opener)

    html = urllib2.urlopen('http://m.renren.com').read()
    img = re.findall(r'<img src="([\S]*)"', html)[0]
    verifykey = re.findall(r'name="verifykey" value="([\S]*)"', html)[0]
    
    print img
    verifycode = raw_input("please visit the above url in your browser, and type the verify code on the page:\n")

    xn = {}
    xn['email'] = email
    xn['password'] = password
    xn['verifycode'] = verifycode
    xn['verifykey'] = verifykey
    #print xn
    
    data = urllib.urlencode(xn)
    req = urllib2.Request('http://3g.renren.com/login.do?fx=0&autoLogin=true', data)
    resp = urllib2.urlopen(req)
    return resp.read()
