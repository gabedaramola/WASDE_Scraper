# import BeautifulSoup
from bs4 import BeautifulSoup

# import requests
import requests

# specify webpage for inspection
r = requests.get('https://www.usda.gov/oce/commodity/wasde/latest.xml')
data = r.text

# return whole page for inspection
# print(data)

soup = BeautifulSoup(data, "xml")

# cell_value1
for ce in soup.find_all("Cell"):
	try:
		print("cell_value1", ce["cell_value1"])		
	except KeyError:
		pass

# cell_value2
for ce in soup.find_all("Cell"):
	try:
		print("cell_value2", ce["cell_value2"])		
	except KeyError:
		pass

# cell_value3
for ce in soup.find_all("Cell"):
	try:
		print("cell_value3", ce["cell_value3"])		
	except KeyError:
		pass

# cell_value4
for ce in soup.find_all("Cell"):
	try:
		print("cell_value4", ce["cell_value4"])		
	except KeyError:
		pass

# cell_value5
for ce in soup.find_all("Cell"):
	try:
		print("cell_value5", ce["cell_value5"])		
	except KeyError:
		pass

# cell_value6
for ce in soup.find_all("Cell"):
	try:
		print("cell_value6", ce["cell_value6"])		
	except KeyError:
		pass
