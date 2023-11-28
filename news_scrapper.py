from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime
import pytz

def scrapper(q):
    headers = {
        'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }
    
    params = {
    'q': q,
    'gl': 'us',
    }

    html = requests.get('https://www.google.com/search?q=', headers=headers, params=params)
    soup = bs(html.text, 'lxml')
    all_news = soup.select('.BVG0Nb')
    result = {
                'Name': q,
                'titles':[],
                'sources':[],
                'pub_times':[],
                'scrapping_time':[]
             }
    for news in all_news:
        try:
            title = news.select_one('span').text.replace('\n','')
            source = news.find('div', attrs={'class':'BNeawe tAd8D AP7Wnd'}).text.split('\n')[0]
            pub_time = news.find('div', attrs={'class':'BNeawe tAd8D AP7Wnd'}).text.split('\n')[1]
        except:
            pass
        else:
            result['Name'] = q
            result['titles'].append(title)
            result['sources'].append(source)
            result['pub_times'].append(pub_time)
            new_york_tz = pytz.timezone('America/New_York')
            result['scrapping_time'].append(datetime.now(new_york_tz).strftime('%Y-%m-%d %H:%M'))

    if len(result['titles'])!=0:
        print(f'{q}: Scrapped Successfuly')
    else:
        print(f'{q}: No Top News or error in name')

    return(result)

