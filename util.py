#coding=utf-8

def utf8_wrapper(s):
    if isinstance(s, unicode):
        return unicode.encode(s, 'utf-8')
    else:
        return s