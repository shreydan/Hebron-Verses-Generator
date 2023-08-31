import shlex
import subprocess
import os
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
    print('fetched...generating image...')

def generate_png(src, dest):
    print('running command...')
    command = f'google-chrome --headless=new --disable-gpu --screenshot={dest} --window-size=1085,2025  {src} --start-maximized --hide-scrollbars --run-all-compositor-stages-before-draw --disable-translate --virtual-time-budget=1000'
    command = shlex.split(command)
    subprocess.run(command)


def convert_to_image(verseObj,_month):

    _HTML = os.path.join(os.getcwd(),'src','index.html')
    file_name = f'{(verseObj["date"]).replace("/","-")}__{verseObj["book"][0]}_{verseObj["reference"]}'.replace(' ', '-')
    _FOLDER = os.path.join(os.getcwd(),'output',_month)
    _OUTFILE = os.path.join(_FOLDER,file_name+'.png')

    if not os.path.exists(_FOLDER):
        os.makedirs(_FOLDER)
    sourcepath = 'file://' + _HTML

    
    generate_png(sourcepath, _OUTFILE)
