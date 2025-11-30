from generator import modify_html, convert_to_image
from fetcher import fetchVerse
import os
import json
import time

month = [f'2025-12-{str(i).zfill(2)}' for i in range(17,18)]

_month = 'DECEMBER'

f = open(os.path.join(os.getcwd(),'calendar-data-2025.json'))
dates = json.load(f)
f.close()

print("Praise the Lord!")
missed = []
for date in month:
    verseID = dates['hebron'][date]['verseid']
    print(verseID, date)
    try:
        verseObj = fetchVerse(verseID,date)
        modify_html(verseObj)
        convert_to_image(verseObj,_month)
        print(f"generated {verseObj['book'][0]} {verseObj['reference']}\n\n")
        time.sleep(2)
    except Exception as e:
        print(e)
        print('missed :(')
        missed.append(verseID)

print(missed)
