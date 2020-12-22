import requests

from bs4 import BeautifulSoup
episode= open('episode.txt','r')
latest=episode.read()
print(int(latest))
episode.close()

res = requests.get('https://www.primevideo.com/detail/0PURFQY578DB8NNPQJG4L52E4W/ref=atv_dp_season_select_s3');

soup = BeautifulSoup(res.text, "lxml");

ep = soup.find_all("span",attrs={"dir": "auto"});

url = f'https://api.telegram.org/bot1184739317:AAFcjgnch0_kgNO4xOLfiyuCtHYufaWpY3I/sendMessage';
data = {'chat_id': 830370648, 'text': f'Season 3 episode {int(latest)+1} released'};

if(len(ep)==int(latest)+1):
         requests.post(url, data).json();
         episode1= open('episode.txt','w')
         episode1.write(str(int(latest)+1))
         episode1.close()
