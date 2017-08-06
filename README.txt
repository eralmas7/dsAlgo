Goal
=====
Download problems listed on dsAlgo.com in an easy to read pdf format.

Requirement:
-------------
dsAlgo.com is an excellent site for preparing algorithm and data structures. It has helped many people in getting jobs at Google, Amazon, Microsoft etc.

One things that people find problem with is, Everytime i need to look at the problems on dsAlgo.com, i have to turn on data plan or logon to internet and start reading problems one by one.

With static file, i can open and read from anywhere and can work out without the need of internet. All the problems are at one place.

The only thing i would be missing is the comments around the solution and if any new problem is added onto the site.

With this in mid, we have designed a project that Scrapes [dsAlgo](http://www.dsalgo.com/2013/02/index.php.html) and creates html & PDF for all the problems listed along with syntax highlighting for the code.

Instructions to build and run the application.
---------------------------------------------

##### Pre-requisite for this project:
	- To use the scrapper, install the following:
		`$ sudo apt-get install wkhtmltopdf`
	- Now install BeautifulSoup as:
		`$ pip install beautifulsoup4`
		or via package manager as:
		`$ sudo apt-get install python-bs4`
		or for Python dependencies, you can just install via `requirements.txt` inside the virtual environment as below:
		`$ pip install -r requirements.txt`

##### To build and run the application:
	$ python dsAlgo.py
	
##### Output from the application:
You can find the output as `dsAlgo.html` and `dsAlgo.pdf` in the same directory.

### Disclaimer: This is strictly for educational purpose only.