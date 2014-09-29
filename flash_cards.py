import requests, re
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/term/<term>")
def get_term(term):
	baseURL = "http://psychologydictionary.org/"

	requestURL = baseURL + term
	r = requests.get(requestURL)

	page_html = r.text
	soup = BeautifulSoup(page_html)

	word = soup.find_all("h1", class_="title").find_all('b')
	print word 
	return word

if __name__ == "__main__":
    app.run()