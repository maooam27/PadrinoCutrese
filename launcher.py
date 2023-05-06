import requests

a = requests.get('https://raw.githubusercontent.com/maooam27/PadrinoCutrese/master/main.py?token=GHSAT0AAAAAACAOVSGOO4N7LIMJK5PVSLFYZCWLFHA')

print(a.text)
