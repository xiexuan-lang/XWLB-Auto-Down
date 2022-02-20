# write by xiexuan（谢轩）
# date 2022.2
# support sdyz.huangyinhao.top. and wordpress.xiexuanicu.com and xiexuan.icu    all right serverd
# 用来测试央视的url，怕他突然改变而出问题
import requests
from bs4 import BeautifulSoup
url = 'https://tv.cctv.com/lm/xwlb/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
for link in soup.find_all('a'):
	realurl = str(link.get('href'))
	print(realurl)