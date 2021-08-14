from bs4 import BeautifulSoup
import requests  

class GetTicker():
	def __init__(self, url):
		self.url = url 
		self.headers ={
		    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
		} 
		self.r = requests.get(url, headers=self.headers).content

	def get_tickers(self):
		soup = BeautifulSoup(self.r, 'lxml')
		ticker_list = []
		table_rows = soup.find_all('tr')
		for i in range(1,len(table_rows)) :
			ticker_list.append(table_rows[i].a.text)
		return tuple(ticker_list)