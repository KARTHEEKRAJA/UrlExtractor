from urllib.request import urlopen

page = urlopen("https://www.Google.com")

source_code = page.read()

print(source_code)