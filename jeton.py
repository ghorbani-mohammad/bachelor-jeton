import requests
from bs4 import BeautifulSoup
import urllib.request


url ="http://jeton.araku.ac.ir"
r=requests.session()
s=r.get(url)
html_doc=s.text

# print(r.status_code)
# print(r.text)
# print(r.content)


soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
# print(soup.find_all('input'))
# print('\n')
VIEWSTATE=soup.find(id="__VIEWSTATE").get('value')
VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR").get('value')
EVENTVALIDATION=soup.find(id="__EVENTVALIDATION").get('value')

# print(r.cookies['ASP.NET_SessionId'])
# print(r.cookies.get_dict())
# print(r.content)



captcha=url+'/'+soup.find_all('img')[1].get('src')
# print(captcha)
urllib.request.urlretrieve(captcha,"captcha.jpg")   #saving image into filename captcha

#
# username=11521
# password=9213231259
captcha=input('Please Insert Captcha:')
#
# print(captcha)
#
s=r.post(url+"/login.aspx",data={'__LASTFOCUS':'' ,'__EVENTTARGET':'','__EVENTARGUMENT':'',
                                        '__VIEWSTATE':VIEWSTATE,'__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,
                                        '__VIEWSTATEENCRYPTED':'','__EVENTVALIDATION':EVENTVALIDATION,
                                        'txtusername':11521,'txtpassword':9213231259,
                                        'CaptchaControl1':captcha,'btnlogin':'ورود'})

# print(r.status_code)
# print(r.content)

# html_doc=r.text
# soup = BeautifulSoup(html_doc, 'html.parser')

# etebar=soup.find(id='lbEtebar').text
# print(etebar)


print(r.cookies)
print(r.headers)