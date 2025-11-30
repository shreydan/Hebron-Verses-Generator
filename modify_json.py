import json
from datetime import datetime, timedelta

april="""MAT.10.31
PSA.147.14
JOB.11.19
PSA.89.28
ISA.54.14
PSA.98.4
JHN.16.23
MAT.6.33
NEH.8.10
1PE.5.4
JOB.5.19
ISA.45.2
MAT.4.10
JOB.11.18
JER.39.18
PSA.147.14
JER.15.21
PRO.3.6
PSA.32.8
PSA.22.25
1PE.4.14
ISA.48.17
PSA.91.11
GEN.26.24
DAN.10.18
PSA.7.4
PSA.41.13
MIC.4.13
1PE.5.7
MAT.5.12
DEU.15.4
"""
verses = april.splitlines()
with open('./calendar-data-2025.json','r') as f:
    cal = json.load(f)

num_days = 31
start = datetime(2025,7,1)
days = [start,]
for _ in range(num_days-1):
    day = start + timedelta(days=1)
    days.append(day)
    start = day

days = [d.strftime("%Y-%m-%d") for d in days]
print(days)

for day,verse in zip(days,verses):
    cal['hebron'][day] = {'verseid': verse}

with open('./calendar-data-2025.json','w') as f:
    json.dump(cal,f,indent=4)