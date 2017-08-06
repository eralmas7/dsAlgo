#!/usr/bin/python

import requests
from os import system
from sys import exit
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup

BASE_URL = 'http://www.dsalgo.com/2013/02/index.php.html'
articles = []

def save_articles_as_html_and_pdf(fileName):
    print("All links scraped, extracting articles")
    # Formatting the html for articles
    all_articles = (
        '<!DOCTYPE html>'
        '<html><head>'
        '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />'
        '<link rel="stylesheet" href="style.min.css" type="text/css" media="all" />'
        '<script src="https://cdn.rawgit.com/google/code-prettify/master/loader/run_prettify.js"></script>'
        '</head><body>'
    )

    for x in range(len(articles)):
		all_articles += '<hr id=\"' + str(x+1) +'\">' + articles[x].decode("utf-8")

    all_articles += '''</body></html>'''
    html_file_name = '{0}.html'.format(fileName)
    with open(html_file_name, 'w') as html_file:
        html_file.write(all_articles.encode("utf-8"))

    pdf_file_name = '{0}.pdf'.format(fileName)
    print("Generating PDF " + pdf_file_name)
    html_to_pdf_command = 'wkhtmltopdf ' + html_file_name + ' ' + pdf_file_name
    system(html_to_pdf_command)


def scrape_category(category_url):
    try:
        print "Using URL now " + category_url
        soup = BeautifulSoup(requests.get(category_url).text, 'html.parser')
    except ConnectionError:
        print("Couldn't connect to Internet! Please check your connection & Try again.")
        exit(1)

    # Selecting links which are in the category page
    links = [a.attrs.get('href') for a in soup.select('ul li a')]
    links = [link for link in links if "preface" or "index.php.html"  not in link]

    print("Found: " + str(len(links)) + " links")
    i = 1

    # Traverse each link to find article and save it.
    for link in links:
        try:
            link = link.strip()
            print("Scraping link no: " + str(i) + " Link: " + link)
            i += 1
            download(link)
        except ConnectionError:
            print("Will download again from " + str(link))
            download(link)

def download(link):
    result = requests.get(link).text
    result = result.replace('\\n', '\n')

    link_soup = BeautifulSoup(result, 'html.parser')
    mydiv = link_soup.find("div", {"class": "entry-content"})
    if (not mydiv is None):
        page = mydiv.encode('UTF-8')
        articles.append(page)

if __name__ == '__main__':
    articles = []
    scrape_category(BASE_URL)
    save_articles_as_html_and_pdf()