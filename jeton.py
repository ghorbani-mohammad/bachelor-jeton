import requests
from bs4 import BeautifulSoup
import urllib.request


url ="http://jeton.araku.ac.ir"
urlReserve=url+"/Reserve.aspx"
s=requests.session()
r=s.get(url)

html_doc=r.text
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
r=s.post(url+"/login.aspx",data={'__LASTFOCUS':'' ,'__EVENTTARGET':'','__EVENTARGUMENT':'',
                                        '__VIEWSTATE':VIEWSTATE,'__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,
                                        '__VIEWSTATEENCRYPTED':'','__EVENTVALIDATION':EVENTVALIDATION,
                                        'txtusername':11521,'txtpassword':9213231259,
                                        'CaptchaControl1':captcha,'btnlogin':'ورود'})

# print(r.status_code)
# print(r.content)

# html_doc=s.text
# soup = BeautifulSoup(html_doc, 'html.parser')
#
# etebar=soup.find(id='lbEtebar').text
# print(etebar)
sessionId=s.cookies.get_dict()['ASP.NET_SessionId']
# r=s.get(url+"/SelectGhaza.aspx?date=960126&dow=0&kind=2&sel=False&selg=True&week=1&personeli=11521", cookies={'ASP.NET_SessionId':sessionId})

html_doc=r.text
soup = BeautifulSoup(html_doc, 'html.parser')

VIEWSTATE=soup.find(id="__VIEWSTATE").get('value')
VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR").get('value')
EVENTVALIDATION=soup.find(id="__EVENTVALIDATION").get('value')


r=s.post(urlReserve,cookies={'ASP.NET_SessionId':sessionId},data={
    'EditC1': '0',
    'EditC2': '0',
    'EditC3': '0',
    'EditC4': '0',
    'EditC5': '0',
    'EditC6': '0',

    'EditN1': '0',
    'EditN2': '0',
    'EditN3': '0',
    'EditN4': '0',
    'EditN5': '0',
    'EditN6': '0',

    'EditS1': '0',
    'EditS2': '0',
    'EditS3': '0',
    'EditS4': '0',
    'EditS5': '0',
    'EditS6': '0',

    'GhazaC1': '0',
    'GhazaC2': '0',
    'GhazaC3': '0',
    'GhazaC4': '0',
    'GhazaC5': '0',
    'GhazaC6': '0',
    'GhazaC7': '0',

    'GhazaN1': '0',
    'GhazaN2': '0',
    'GhazaN3': '0',
    'GhazaN4': '0',
    'GhazaN5': '0',
    'GhazaN6': '0',
    'GhazaN7': '0',

    'GhazaS1': '0',
    'GhazaS2': '0',
    'GhazaS3': '0',
    'GhazaS4': '0',
    'GhazaS5': '0',
    'GhazaS6': '0',
    'GhazaS7': '0',

    'Hid1': '0',
    'Hid2': '0',
    'Hid3': '0',
    'Hid4': '0',
    'Hid5': '0',
    'Hid6': '0',
    'Hid7': '0',

    'HidC1': '0',
    'HidC2': '0',
    'HidC3': '0',
    'HidC4': '0',
    'HidC5': '0',
    'HidC6': '0',
    'HidC7': '0',

    'HidCN1': '0',
    'HidCN2': '0',
    'HidCN3': '0',
    'HidCN4': '0',
    'HidCN5': '0',
    'HidCN6': '0',
    'HidCN7': '0',

    'HidN1': '0',
    'HidN2': '0',
    'HidN3': '0',
    'HidN4': '0',
    'HidN5': '0',
    'HidN6': '0',
    'HidN7': '0',

    'HidS1': '0',
    'HidS2': '0',
    'HidS3': '0',
    'HidS4': '0',
    'HidS5': '0',
    'HidS6': '0',
    'HidS7': '0',

    'HidSN1': '0',
    'HidSN2': '0',
    'HidSN3': '0',
    'HidSN4': '0',
    'HidSN5': '0',
    'HidSN6': '0',
    'HidSN7': '0',

    'RD_Self':'1',
    'Selt':'1',

    'btn_saveKharid':'تایید',


    '__EVENTTARGET':'','__EVENTARGUMENT':'',
    '__VIEWSTATE':VIEWSTATE,'__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,
    '__VIEWSTATEENCRYPTED':'','__EVENTVALIDATION':EVENTVALIDATION,



    })


html_doc=r.text
soup = BeautifulSoup(html_doc, 'html.parser')

message=soup.find(id="LbMsg").get('value')



print(message)


