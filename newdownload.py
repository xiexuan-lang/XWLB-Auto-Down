# write by xiexuan
# date 2022.2
# support sdyz.huangyinhao.top. and wordpress.xiexuanicu.com and xiexuan.icu    all right serverd

import requests
import os
import datetime
import toml
from bs4 import BeautifulSoup
curretpath = os.path.dirname(__file__)
toml1 = toml.load(curretpath + '/newspath.toml')
def get_time():
	time = datetime.datetime.now()
	if toml1['TODAYS'] :
		day = time.day
	else :
		day = time.day -1
	return '/'+ str(time.year)+'/'+str('{:0>2}'.format(time.month))+'/'+str('{:0>2}'.format(day))+'/'
url = 'https://tv.cctv.com/lm/xwlb/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
for link in soup.find_all('a'):
	if 'https://tv.cctv.com'+get_time() in str(link.get('href')):
		realurl = str(link.get('href'))
		break

os.system('you-get -o '+str(toml1['NEWS_LOCAL_PATH'])+" "+str(realurl))
