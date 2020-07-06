# Proxy Scraper & Checker - Automated Non-Stop

## What is Proxy Scraper & Checker?

This bot each defined second, crawls updated proxies to a txt file.

* You can call same function in your app and it will before crawling all proxies again, use crawled proxies from file to save time.

* You always have at least 130 fresh proxies in your file. Default 130 value can be overwritten.

* All proxies are testing and the proxies which doesn't work, are saved to another file to not use again.

## Requirements

```
pip install -r requirements.txt
```

## How to Run it

### Running next to your app

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

### Running in your app

```
from Functions import Connect
import requests
from selenium import webdriver

count_loop = 0
while True:
    count_loop += 1
    
    # Here we get our fresh proxy
    count_loop, proxy_decide = Connect.get_proxy(
        count_loop,
        selenium=False,
        run_test=False,
    )
    
    # Your function in requests
    response = requests.get(
        url,
        headers=headers,
        stream=True,
        proxies=proxy_decide,  # <-- HERE
        timeout=5,
    )

    # Your function in Selenium
    options = webdriver.ChromeOptions()
    options.add_argument('user-agent={%s}' % user_agent)
    options.add_argument(proxy_decide)  # <-- HERE
    browser = webdriver.Chrome(options=options)

    # do...
```

<hr>

![Proxy Scraper Screenshot](https://github.com/berkaymizrak/Proxy-Scraper/blob/master/Functions/proxy_scraper_screen2.png?raw=true)
