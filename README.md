# pintuition

Python script to pull pins from a specific [Pinterest board](https://www.pinterest.com/eleanordare/wedding/) and generate a graph based on the frequency of posting.


## Getting Started

1. `git clone https://github.com/eleanordare/pintuition.git`

2. Install dependencies.
  - `pip install bottle`
  - `pip install python-highcharts`
  - `pip install datetime`

3. Accessing the Pinterest API requires an SSL connection. [This tutorial](http://www.socouldanyone.com/2014/01/bottle-with-ssl.html) walks you through how to create a server certificate and create a basic SSL server using Bottle.

4. You can use my Pinterst API access token in **pinterest.py** or [create your own](https://developers.pinterest.com/apps/) by registering an app with them.

5. Change the `boardUrl` variable in **pinterest.py** to whatever board URL you prefer. A future update will define this dynamically in the web app, but for now you can enter it yourself.

6. Run `python routes.py` to start the server, available at [https://localhost:5000/hello](https://localhost:5000/hello).


## Dependencies

- [Pinterest API](https://developers.pinterest.com/)
- [Bottle Python Web Framework](http://bottlepy.org/)
- [Highcharts JS Charts](http://www.highcharts.com/)
- [Python Highcharts Wrapper](https://github.com/kyper-data/python-highcharts)
