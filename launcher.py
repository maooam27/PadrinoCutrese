import requests

a = requests.get('https://raw.githubusercontent.com/maooam27/PadrinoCutrese/master/app/main.py?token=GHSAT0AAAAAACCYTSTF7STQ5VCLDTGAZ3P4ZDE6VAA')

with open("app/main.py", 'w') as f:
    f.writelines(a.text)

