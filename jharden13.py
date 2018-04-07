# import BeautifulSoup
from bs4 import BeautifulSoup

# import requests
import requests

# specify webpage for inspection
r = requests.get('http://www.nba.com/players/james/harden/201935')
data = r.text

# return whole page for inspection
print(data)