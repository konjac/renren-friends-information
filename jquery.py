#coding=utf-8
from pyquery import PyQuery as PQ


PQ.fn.listOuterHtml = lambda: this.map(lambda i, el: PQ(this).outerHtml())

def query(html, str):
    return PQ(html).find(str)