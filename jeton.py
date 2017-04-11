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
print(VIEWSTATE)
print(len(VIEWSTATE))


captcha=url+'/'+soup.find_all('img')[1].get('src')
# print(captcha)
urllib.request.urlretrieve(captcha,"captcha.jpg")   #saving image into filename captcha

#
# username=11521
# password=9213231259
captcha=input('Please Insert Captcha:')

r=s.post(url+"/login.aspx",data={'__LASTFOCUS':'' ,'__EVENTTARGET':'','__EVENTARGUMENT':'',
                                        '__VIEWSTATE':VIEWSTATE,'__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,
                                        '__VIEWSTATEENCRYPTED':'','__EVENTVALIDATION':EVENTVALIDATION,
                                        'txtusername':11521,'txtpassword':9213231259,
                                        'CaptchaControl1':captcha,'btnlogin':'ورود'})

html_doc=r.text
soup = BeautifulSoup(html_doc, 'html.parser')

VIEWSTATE=soup.find(id="__VIEWSTATE").get('value')
VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR").get('value')
EVENTVALIDATION=soup.find(id="__EVENTVALIDATION").get('value')



# message=soup.find(id="LbMsg").get('value')
# print(s.text)
# print(s.headers)
s.headers['Referer'] = 'http://jeton.araku.ac.ir/Reserve.aspx';
# {'Referer': 'http://jeton.araku.ac.ir/Reserve.aspx'}
# print(s.headers)

# print(VIEWSTATE)
# print(VIEWSTATEGENERATOR)
# print(EVENTVALIDATION)


data={
    # 'EditC1': '0',
    # 'EditC2': '0',
    # 'EditC3': '0',
    'EditC4': '0',
    # 'EditC5': '0',
    'EditC6': '0',

    # 'EditN1': '0',
    # 'EditN2': '0',
    # 'EditN3': '0',
    # 'EditN4': '0',
    # 'EditN5': '0',
    # 'EditN6': '10',

    # 'EditS1': '0',
    # 'EditS2': '0',
    # 'EditS3': '0',
    # 'EditS4': '0',
    # 'EditS5': '0',
    # 'EditS6': '0',

    # 'GhazaC1': '0',
    # 'GhazaC2': '0',
    # 'GhazaC3': '0',
    # 'GhazaC4': '0',
    # 'GhazaC5': '0',
    # 'GhazaC6': '0',
    # 'GhazaC7': '0',

    'GhazaN1': '1',
    'GhazaN2': '0',
    'GhazaN3': '1',
    'GhazaN4': '0',
    'GhazaN5': '1',
    'GhazaN6': '1',
    'GhazaN7': '0',

    'GhazaS1': '2',
    'GhazaS2': '0',
    'GhazaS3': '1',
    'GhazaS4': '0',
    'GhazaS5': '2',
    'GhazaS6': '0',
    'GhazaS7': '0',

    'Hid1': '5625',
    'Hid2': '0',
    'Hid3': '6450',
    'Hid4': '0',
    'Hid5': '3950',
    'Hid6': '6450',
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

    'HidN1': '1',
    'HidN2': '0',
    'HidN3': '1',
    'HidN4': '0',
    'HidN5': '1',
    'HidN6': '1',
    'HidN7': '0',

    'HidS1': '3950',
    'HidS2': '0',
    'HidS3': '3950',
    'HidS4': '0',
    'HidS5': '5625',
    'HidS6': '0',
    'HidS7': '0',

    'HidSN1': '2',
    'HidSN2': '0',
    'HidSN3': '1',
    'HidSN4': '0',
    'HidSN5': '2',
    'HidSN6': '0',
    'HidSN7': '0',

    'txtn_numGhazac6':'on',
    'RD_Self':'1',
    'Self':'1',

    'btn_saveKharid':'تائید',

    '__EVENTTARGET':'','__EVENTARGUMENT':'',
    # '__VIEWSTATE':VIEWSTATE,
    '__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,
    '__VIEWSTATEENCRYPTED':'','__EVENTVALIDATION':EVENTVALIDATION,
    }
print(VIEWSTATE)
print(len(VIEWSTATE))
data['__VIEWSTATE']=VIEWSTATE
print(data['__VIEWSTATE'])
print(len(data['__VIEWSTATE']))
#


r=requests.post(urlReserve,data=data,cookies=s.cookies.get_dict('ASP.NET_SessionId'))
#
#
# html_doc=r.text
# soup = BeautifulSoup(html_doc, 'html.parser')
#
# message=soup.find(id="LbMsg").get('value')
#
#
#
# print(message)
#
#
