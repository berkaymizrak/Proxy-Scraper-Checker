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
```

If you set run_test True, program checks each time whether you have enough number of proxies (default 130). If it is not enough, it fetches new ones and save it to the file. 

To escape this time losing, use run_test False in your app and run my app (without modification if you didn't understand) next to your app at the same time. It will keep proxy file up to date.
```
# Here we get our fresh proxy
count_loop, proxy_decide = Connect.get_proxy(
    selenium=False,
    get_random=True
    run_test=False,
    )
```

Use it in requests:
```  
# Your function in requests
response = requests.get(
    url,
    headers=headers,
    stream=True,
    proxies=proxy_decide,  # <-- HERE
    timeout=5,
    )
```

Use it in Selenium:
```
# Your function in Selenium
options = webdriver.ChromeOptions()
options.add_argument('user-agent={%s}' % user_agent)
options.add_argument(proxy_decide)  # <-- HERE
browser = webdriver.Chrome(options=options)

# do...
```

<hr>

![Proxy Scraper Screenshot](https://github.com/berkaymizrak/Proxy-Scraper/blob/master/Functions/proxy_scraper_screen2.png?raw=true)
