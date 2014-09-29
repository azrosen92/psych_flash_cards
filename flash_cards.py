import requests, re
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

def titlize(string):
	ignored = ['the', 'in', 'a', 'we', 'at', 'on']
	titlized_list = []
	for word in string.split():
		if word not in ignored:
			titlized_word = word[0].upper() + word[1:].lower()
		else:
			titlized_word = word

		titlized_list.append(titlized_word)
	return string.join(titlized_list)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/term/<term>")
def get_term(term):
	print "The term is", term
	baseURL = "http://psychologydictionary.org/"

	requestURL = baseURL + term
	print "Requesting", requestURL
	r = requests.get(requestURL)

	page_html = r.text
	soup = BeautifulSoup(page_html)

	header = soup.find_all("h1", class_="title")
	print header
	word = header[0].find_all("b", limit=1)
	return titlize(word[0].text)

if __name__ == "__main__":
    app.run(debug=True)