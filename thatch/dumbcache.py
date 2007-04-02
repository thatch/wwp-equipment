"""Module for caching resources that don't return the proper headers

This is designed to be pretty nice to servers while still allowing
the user of the cache access to parameters that may be helpful when
serving data (last-modified, and last-check).

Optionally allows you to specify a stripper function that will remove
parts of a webpage that you don't care about, such as ads.

Will use gzip compression when possible

"""

__author__ = "Tim Hatch <tim@timhatch.com>"
__revision__ = "$Rev: 433 $"[6:-2]
__date__  = "$Date: 2006-03-17 21:29:34 -0600 (Fri, 17 Mar 2006) $"[7:-2]
__copyright__ = "Copyright (c) 2006 Tim Hatch"
__license__ = "BSD"
__all__ = ["Cacher", "CacheEntry", "NewCacheEntry", "StripError", "DemoStripper"]

_maxage = 24 * 60 * 60 #seconds in one day
_cachedir = ".cache"

import os, urllib, urllib2, httplib, re, time, rfc822, gzip, StringIO
from md5 import md5
from util import rmkdir

defuseragent = "Mozilla/5.0"

class Cacher(object):
    """
    >>> c = Cacher()
    >>> x = c.fetch("http://slashdot.org/")
    >>> len(x.data) > 100
    True
    >>> x.fresh()
    True
    >>> x.invalidate()
    >>> x.fresh()
    False
    >>> x2 = c.fetch("http://slashdot.org/")
    >>> x2.changed()
    True
    >>> x3 = c.fetch("http://slashdot.org/")
    >>> x3.changed()
    False
    >>> c = Cacher(DemoStripper)
    >>> x = c.fetch("http://google.com/")
    >>> "<html>" in x.data
    False
    
    
    """
    def __init__(self, stripper=None, useragent=None):
        self._stripper = stripper
        self.ua = useragent or defuseragent
        if not os.path.isdir(_cachedir):
            os.mkdir(_cachedir)
        
    def cachefn(self, url, params):
        """
        url is the base url for the entity
        
        params can either be a dictionary or a sequence of tuples -- it's
        passed verbatim to urllib.urlencode()
        """
        s = url
        if not params is None:
            s = url + "?" + urllib.urlencode(params)
        return (s, os.path.join(_cachedir, md5(s).hexdigest()))
    
    def fetch(self, url, params=None, cookie=None):
        """
        Requests an entity from the cache, if it exists.

        See the docstring for cachefn() for parameters
        """
        (u, fn) = self.cachefn(url, params)
        prev = None
        if os.path.exists(fn) and os.path.exists(fn + ".props"):
            prev = CacheEntry(fn)
            if prev.fresh():
                return prev
        req = urllib2.Request(u, None, {"Accept-Encoding": "gzip", "User-Agent": self.ua})
        if cookie:
            req.add_header("Cookie", cookie)
        f = urllib2.urlopen(req)
        data = f.read()
        # Handle compressed content before writing to the local cache
        if f.headers.get("Content-Encoding") == "gzip":
            data = gzip.GzipFile(fileobj=StringIO.StringIO(data)).read()
        # Process through a function to get rid of dynamic bits
        if self._stripper is not None:
            data = self._stripper(data)
            
        if prev:
            if data == prev.data:
                # Simply update the last-check time, leaving last-modified alone
                prev.touch()
            else:
                # New data, set last-modified too
                prev.feed(data)
        else:
            # Last-modified and last-check are both now
            prev = NewCacheEntry(fn, data)
        return prev

class TerraserverTileCache(Cacher):
    _baseurl = "http://terraserver-usa.com/tile.ashx"
    def __init__(self):
        pass
    def cachefn(self, url, params):
        return ""
    def gettile(self, t, s, x, y, z):
        pass
        #http://terraserver-usa.com/tile.ashx?t=1&s=14&x=72&y=1162&z=14        
                

class CacheEntry(object):
    _changed = False
    def __init__(self, fn): #FIXME: pass in an md5 instead?
        assert(os.path.exists(fn))
        self._fn = fn
        tf = file(fn + ".props", "rb")
        self.props = rfc822.Message(tf)
        tf.close()
        self.data = file(fn, "rb").read()
        
    def age(self):
        return time.time() - float(self.props['last-check'])
        
    def fresh(self):
        return self.age() < _maxage
        
    def changed(self):
        return self._changed
        
    def feed(self, data):
        fo = file(self._fn, "wb")
        fo.write(data)
        fo.close()
        self.touch(True)
        self.data = data
        
    def touch(self, changed=False):
        now = str(time.time())
        self.props['last-check'] = now
        if changed:
            self.props['last-modified'] = now
            self._changed = True
        self._saveprops()
        
    def _saveprops(self):
        fo = file(self._fn + ".props", "wb")
        fo.write(str(self.props))
        fo.close()
        
    def invalidate(self):
        self.props['last-check'] = "0.0" #Yay 1970!
        self._saveprops()   

class NewCacheEntry(CacheEntry):
    def __init__(self, fn, data):
        self._fn = fn
        self.props = rfc822.Message(StringIO.StringIO())
        self.feed(data)
        

class StripError(Exception):
    pass

r_body = re.compile(r"<body.*?>(.*?)</body", re.I + re.DOTALL)
def DemoStripper(s):
    r"""
    >>> d = "\n".join(["<html>", "<body>", "<p>", "asd</p>", "</body></html>"])
    >>> DemoStripper(d)
    '<p>\nasd</p>'
    >>> DemoStripper('')
    Traceback (most recent call last):
    ...
    StripError: DemoStripper could not find the right info
    >>>
    """
    m = r_body.search(s)
    if not m:
        raise StripError, "DemoStripper could not find the right info"
    return m.group(1).strip()

def _test():
    from doctest import testmod
    testmod()
    
if __name__ == "__main__":
    _test()