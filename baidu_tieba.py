import re  
import urllib.request
  
def getHtml(url):  
    page = urllib.request.urlopen(url)  
    html = page.read()
    html = html.decode('utf-8')
    return html  
  
def getImg(html):  
    reg = r'src="(.+?\.jpg)" pic_ext'  
    imgre = re.compile(reg)  
    imglist = imgre.findall(html)  
    x = 0  
    for imgurl in imglist:  
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)  
        x = x + 1          
     
html = getHtml("http://tieba.baidu.com/p/2460150866")  
getImg(html)  
