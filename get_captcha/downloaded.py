from urllib import urlretrieve

captcha_url = 'http://kns.cnki.net/kns/checkcode.aspx?t=%1+Math.random()'
for k in range(300):
    urlretrieve(captcha_url,'D:\\zhiwang_captcha\\img\\raw/%d.gif' %k)