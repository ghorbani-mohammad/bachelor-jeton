import requests
from bs4 import BeautifulSoup
import urllib.request


url ="http://jeton.araku.ac.ir"
urlReserve=url+"/Reserve.aspx"
urlSelect=url+"/SelectGhaza.aspx?date="
s=requests.session()
r=s.get(url)

html_doc=r.text
soup = BeautifulSoup(html_doc, 'html.parser')

VIEWSTATE=soup.find(id="__VIEWSTATE").get('value')
VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR").get('value')
EVENTVALIDATION=soup.find(id="__EVENTVALIDATION").get('value')


captcha=url+'/'+soup.find_all('img')[1].get('src')

urllib.request.urlretrieve(captcha,"captcha.jpg")   #saving image into filename captcha


captcha=input('Please Insert Captcha:')

r=s.post(url+"/login.aspx",data={'__LASTFOCUS':'' ,'__EVENTTARGET':'','__EVENTARGUMENT':'',
                                        '__VIEWSTATE':VIEWSTATE,'__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,
                                        '__VIEWSTATEENCRYPTED':'','__EVENTVALIDATION':EVENTVALIDATION,
                                        'txtusername':11521,'txtpassword':9213231259,
                                        'CaptchaControl1':captcha,'btnlogin':'ورود'})

html_doc=r.text
soup = BeautifulSoup(html_doc, 'html.parser')

startOfWeek=soup.find(id="D1").text
startOfWeek = startOfWeek.replace("/", "")
startOfWeek=startOfWeek[4:]+startOfWeek[2:4]+startOfWeek[0:2]


def price( dow,kind,week,username,item=1):
    r1=s.get(urlSelect+str(startOfWeek)+"&dow="+str(dow)+"&kind="+str(kind)+"&sel=False&selg=True&week="+str(week)+"&personeli="+str(username))
    print(urlSelect+str(startOfWeek)+"&dow="+str(dow)+"&kind="+str(kind)+"&sel=False&selg=True&week="+str(week)+"&personeli="+str(username))
    soup2 = BeautifulSoup(r1.text, 'html.parser')
    tr=soup2.find_all('tr')[2+item]
    td=tr.find_all('td')
    return  td[3].text

# http://jeton.araku.ac.ir/SelectGhaza.aspx?date=960119&dow=5&kind=0&sel=False&selg=True&week=0&personeli=11521
# print(price(5,0,0,11521))

data={}

for x in range(1,8):

    enable = soup.find(id="txts_numGhazac" + str(x))
    if (enable.get('disabled') == None):
        if (enable.get('checked') != None):
            data['EditS' + str(x)] = soup.find(id="EditS" + str(x)).get('value')
            data['txts_numGhazac' + str(x)] = 'on'
        else:
            data['GhazaS' + str(x)] = '0'
            data['EditS' + str(x)] = 0


    enable = soup.find(id="txtn_numGhazac" + str(x))
    if (enable.get('disabled') == None):
        if (enable.get('checked') != None):
            data['EditN' + str(x)] = soup.find(id="EditN" + str(x)).get('value')
            data['txtn_numGhazac' + str(x)] = 'on'
        else:
            data['GhazaN' + str(x)] = '0'
            data['EditN' + str(x)] = 0


    enable = soup.find(id="txtc_numGhazac" + str(x))
    if (enable.get('disabled') ==None):
        if(enable.get('checked') !=None):
          data['EditC'+str(x)]=soup.find(id="EditC"+str(x)).get('value')
          data['txtc_numGhazac'+str(x)]='on'
        else:
            data['GhazaC' + str(x)] = '0'
            data['EditC' + str(x)] = 0

    value=soup.find(id="GhazaS"+str(x)).get('value')
    if(int(value) !=0):
        data['HidS'+str(x)]=price(x-1,2,0,'11521',int(value))
    else:
        data['HidS' + str(x)] =0;
    data['HidSN'+str(x)]=value

    value = soup.find(id="GhazaN" + str(x)).get('value')
    if (int(value) != 0):
        data['Hid' + str(x)] = price(x-1, 1, 0, '11521', int(value))
    else:
        data['Hid' + str(x)] =0;
    data['HidN' + str(x)] = value

    value = soup.find(id="GhazaC" + str(x)).get('value')
    if (int(value) != 0):
        data['HidC' + str(x)] = price(x-1, 0, 0, '11521', int(value))
    else:
        data['HidC' + str(x)] =0;
    data['HidCN' + str(x)] = value

print(data)
