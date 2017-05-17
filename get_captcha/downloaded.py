from urllib import urlretrieve
import os

captcha_url = 'http://kns.cnki.net/kns/checkcode.aspx?t=%1+Math.random()'
for k in range(30):
    urlretrieve(captcha_url,'../img/test/%d.gif' %k)