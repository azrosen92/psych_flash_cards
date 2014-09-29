import requests, re, json
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

	result_dict = {}

	# Scrape term from page
	header = soup.find_all("h1", class_="title")
	print header
	word = titlize(header[0].find_all("b", limit=1)[0].text)
	result_dict['word'] = word

	#Scrape definition from page
	entry = soup.find_all("div", class_="entry")[0]
	definition = entry.find_all("p", limit=1)[0].text
	print definition
	result_dict['definition'] = definition

	#Scrape example from page
	example = entry.find_all("div", limit=1)[0].text
	print example
	result_dict['example'] = example
	
	return json.dumps(result_dict)


if __name__ == "__main__":
    app.run(debug=True)