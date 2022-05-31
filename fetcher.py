import requests
from bs4 import BeautifulSoup
import re
from config import API_KEY


api_key = API_KEY
language = {
    'english': 'de4e12af7f28f599-01',
    'hindi' : '705aad6832c6e4d2-02',
    'hindi2': '1e8ab327edbce67f-01',
    'telugu': '5b835ce16a1703ff-01'
}


headers = {'api-key': api_key}



def fetchVerse(reference,date):

    verseObj = {
        'verse': [],
        'book': [],
        'reference': '',
        'date': date
    }
    
    for lang in ['english','hindi2','telugu']:

        url = f"https://api.scripture.api.bible/v1/bibles/{language[lang]}/verses/{reference}"

        try:
            raw = requests.get(url=url, headers=headers)
        except requests.exceptions.RequestException as e: 
            raise SystemExit(e)

        verse = re.sub('^[0-9]+','',
                        BeautifulSoup(
                            ((raw.json())['data']['content']).replace('</span>',' </span>'), 
                            features='lxml').get_text())
        ref = re.split('([0-9]+:[0-9]+)',(raw.json())['data']['reference'])


        verseObj['verse'].append(verse)
        verseObj['book'].append(ref[0].strip())
        
    verseObj['reference'] = ref[1]

    return verseObj
    

