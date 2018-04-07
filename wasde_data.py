# import BeautifulSoup
from bs4 import BeautifulSoup

# import requests
import requests

# specify webpage for inspection
r = requests.get('https://www.usda.gov/oce/commodity/wasde/latest.xml')
data = r.text

# return whole page for inspection
print(data)