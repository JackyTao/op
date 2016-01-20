# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import json


# Pattern for each single page!!
p = {
    'type': 'list',
    'name': 'movies',
    'selector': '.sk_maincol li',
    'sub': [
        # sub of the item if type is dict by default
        # else sub of every single item if type is list
        {'selector': '.order', 'name': 'order'},
        {'selector': '.skey a', 'name': 'name'},
        {'selector': '.skey a', 'name': 'link', 'key': 'href'},
        {'selector': '.stat', 'name': 'stat'},
    ],
}


def parseSoup(soup, ptn):
    if not ptn:
        return
    items = soup.select(ptn.get('selector'))

    if 'sub' in ptn:
        if ptn.get('type') == 'list':
            return [{
                ptn_sub.get('name'): parseSoup(item, ptn_sub)
                for ptn_sub in ptn['sub']
            } for item in items]
        else:
            return {
                ptn_sub.get('name'): parseSoup(items[0], ptn_sub)
                for ptn_sub in ptn['sub']
            }
    else:
        if ptn.get('type') == 'list':
            return [_get_value(item, ptn) for item in items]
        else:
            return _get_value(items[0], ptn)


def _get_value(soup, ptn):
    if ptn.get('key') is not None:
        return soup[ptn['key']]
    else:
        return soup.text


# 
def parseContent(content):
    soup = BeautifulSoup(content)
    movies = soup.select('.sk_maincol')[0].select('li')
    for movie in movies:
        print movie.select('.order')[0].text
        print movie.select('.skey')[0].select('a')[0]['href']
        print movie.select('.stat')[0].string
    return


if __name__ == '__main__':
    c = urllib2.urlopen('http://www.soku.com/newtop/movie.html').read()
    soup = BeautifulSoup(c)
    json.dump(parseSoup(soup, p), open('movies.json', 'w'))
    print 'aaa'
