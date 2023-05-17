import requests

a = requests.get('https://github.com/maooam27/PadrinoCutrese/raw/master/app/main.py')

with open("app/main.py", 'w') as f:
    f.writelines(a.text)

