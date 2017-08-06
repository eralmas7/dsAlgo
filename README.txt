# DsAlgoBookDownloader
Scrapes [DsAlgo](http://www.dsalgo.com/2013/02/index.php.html) and creates html & PDF for chosen category along with syntax highlighting for the code.

## Installation
To use the scrapper, install the following:

`$ sudo apt-get install wkhtmltopdf`
Now install BeautifulSoup as:

`$ pip install beautifulsoup4`

or via package manager as:

`$ sudo apt-get install python-bs4`

or for Python dependencies, you can just install via `requirements.txt` inside the virtual environment.

`$ pip install -r requirements.txt`

## Run the dsAlgo_Scrapper

$ python dsAlgo.py

You can find the output as `dsAlgo.html` and `dsAlgo.pdf` in the same directory.

### Disclaimer: This is strictly for educational purpose only.