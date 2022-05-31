import asyncio
from pyppeteer import launch
import sys
import os
from datetime import date
from bs4 import BeautifulSoup



def modify_html(verseObj):
    file = os.path.join(os.getcwd(),'src','index.html')
    html = open(file,'r',encoding='utf-8')
    soup = BeautifulSoup(html.read(),features='lxml')

    date = verseObj['date'].split('-')
    soup.find(id='_date').string = f"{date[2]}-{date[1]}-{date[0]}"

    soup.find(id='eV').string = verseObj['verse'][0]
    soup.find(id='hV').string = verseObj['verse'][1]
    soup.find(id='tV').string = verseObj['verse'][2]

    soup.find(id='eR').string = verseObj['book'][0]
    soup.find(id='hR').string = verseObj['book'][1]
    soup.find(id='tR').string = verseObj['book'][2]

    soup.find(id='nums').string = str(verseObj['reference'])
    html.close()

    html = open(file,'w',encoding='utf-8')
    html.write(soup.prettify())
    html.close()


def convert_to_image(verseObj,_month):

    _HTML = os.path.join(os.getcwd(),'src','index.html')
    file_name = f'{(verseObj["date"]).replace("/","-")}__{verseObj["book"][0]} {verseObj["reference"]}'
    _FOLDER = os.path.join(os.getcwd(),'output',_month)
    _OUTFILE = os.path.join(_FOLDER,file_name+'.png')

    if not os.path.exists(_FOLDER):
        os.makedirs(_FOLDER)
    sourcepath = 'file://' + _HTML

    async def generate_png():
        browser = await launch()
        page = await browser.newPage()
        await page.goto(sourcepath, {'waitUntil' : 'domcontentloaded'})
        await page.evaluateHandle('document.fonts.ready')
        await page.setViewport({ 'width': 1080, 'height': 1920 })
        await page.screenshot({'path': _OUTFILE, 'fullPage': True})
        await browser.close()


    asyncio.get_event_loop().run_until_complete(generate_png())