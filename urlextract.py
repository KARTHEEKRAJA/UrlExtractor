from urllib.request import urlopen

page = urlopen("https://www.Google.com")

print(page.headers)