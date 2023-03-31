from generator import modify_html, convert_to_image
from fetcher import fetchVerse
import os
import json

month = [f'2023-04-{str(i).zfill(2)}' for i in range(1,31)]
_month = 'APRIL'

f = open(os.path.join(os.getcwd(),'calendar-data-2023.json'))
dates = json.load(f)
f.close()

print("Praise the Lord!")

for date in month:
    verseID = dates['hebron'][date]['verseid']
    print(verseID, date)
    verseObj = fetchVerse(verseID,date)
    modify_html(verseObj)
    convert_to_image(verseObj,_month)

    print(f"generated {verseObj['book'][0]} {verseObj['reference']}\n\n")
