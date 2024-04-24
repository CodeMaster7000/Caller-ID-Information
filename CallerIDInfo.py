import pandas as pd 
import requests
from bs4 import BeautifulSoup
	
def getdata(url):
	r=requests.get(url)
	return r.text
  
api = 'YOUR API KEY' # Enter API key here
number = 'XXXXXXXXXX' # Emter cell phone number here
country = 'XX' # Enter country here

htmldata=getdata('http://apilayer.net/api/validate?access_key='+api+'&number='+number+'&country_code='+country+'&format=1')
soup = BeautifulSoup(htmldata, 'html.parser')

print(soup)
