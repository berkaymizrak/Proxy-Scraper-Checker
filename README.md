# Proxy Scraper - Automated Non-Stop

## What is Proxy Scraper?

This bot each defined second, crawls updated proxies to a txt file.

* You can call same function in your app and it will before crawling all proxies again, use crawled proxies from file to save time.

* You always have at least 130 fresh proxies in your file. Default 130 value can be overwritten.

* All proxies are testing and the proxies which doesn't work, are saved to another file to not use again.

## Requirements

```
pip install -r requirements.txt
```

## How to Run it

```
python "Proxy Scraper.py"
```

Then answer **3 questions**. You can just press enter to all for **default values.**

```
How often would you like to make proxy control (For default, leave empty - 5 secs.):
```

```
What is your WORKING proxies file name (For default, leave empty - Recorded OK Proxies.txt): 
```

```
What is your ERROR proxies file name (For default, leave empty - Recorded FALSE Proxies.txt): 
```

**It will continuously work with checking performance of current proxies.**

<hr>

![Proxy Scraper Screenshot](https://github.com/berkaymizrak/Proxy-Scraper/blob/master/Functions/proxy_scraper_screen2.png?raw=true)
