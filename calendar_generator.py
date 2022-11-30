import json
from pathlib import Path
from datetime import date, timedelta


def main(db_path):
    days = {}
    start_date = date(2023,1,1)
    end_date = date(2023,12,31)
    delta = end_date - start_date
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        days.update({day.isoformat(): {
            "verseid": ""
        }})
    calendar_obj = {
        "hebron": days
    }
    with open(db_path,'w') as json_file:
        json.dump(calendar_obj, json_file, indent=4)



if __name__ == '__main__':
    year = '2023'
    db_path = Path('calendar-data-2023.json')
    db_path.touch(exist_ok=True)
    main(db_path)