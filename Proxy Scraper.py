# -*- coding: utf-8 -*-
# Proxy Scraper - Automated Non-Stop
# Berkay MIZRAK
# www.BerkayMizrak.com
# www.DaktiNetwork.com

# Keep up to date your 200 proxies always.

version = '2.2'
program = "Proxy Checker v%s" % version
code = 'proxy_scraper'

print('\n\t%s' % (program))
print('\n\t\twww.BerkayMizrak.com')
print('\n\t\t\twww.DaktiNetwork.com')


try:
    import time

    from Functions import Connect
    from Functions import Progress
except Exception as e:
    print()
    print(e)
    while True:
        input('\n! ! ERROR --> A module is not installed...')


while True:
    try:
        reload = input('\nHow often would you like to make proxy control (For default, leave empty - 5 secs.): ')
        if not reload:
            reload = 5
            break
        reload = int(reload)
        if reload < 0:
            raise Exception
        break
    except:
        print('\n--> Please enter only positive number for second.')

print()
print('--> Reload time selected %s sec.' % reload)

"""
ok_file = input('\nWhat is your WORKING proxies file name (For default, leave empty - Recorded OK Proxies.txt): ')
if not ok_file:
    ok_file = "Recorded OK Proxies.txt"

error_file = input('\nWhat is your ERROR proxies file name (For default, leave empty - Recorded FALSE Proxies.txt): ')
if not error_file:
    error_file = "Recorded FALSE Proxies.txt"
"""

print()

count_loop = 0

frequency_of_check_run = 20000
while True:
    error_point = 0
    try:
        error_point = 1
        if count_loop % frequency_of_check_run == 0:
            # Check if program has permission to run from developer by API
            Connect.check_run(code, program, 30, sound_error=True)  # <-- Remove this line in your app or you can create yours.
            API_KEY = Connect.connect_api(code='proxy_scraper_proxy_orbit_api_key', program=program, )

        error_point = 2
        print('-' * 40)
        print()

        error_point = 3
        first_time = time.time()

        error_point = 4
        # count_loop, proxy_decide, record_ip_type = Connect.get_proxy(
        #     selenium=False,
        #     get_random=False,
        #     allow_print=True,
        #     count_loop=count_loop,
        #     error_file=error_file,
        #     ok_file=ok_file,
        #     run_test=True,
        #     no_proxy=False,
        #     for_https=True
        # )

        count_loop, proxy_decide, curl = Connect.get_proxy_orbit(
            selenium=False,
            get_random=False,
            allow_print=True,
            count_loop=count_loop,
            # error_file=error_file,
            # ok_file=ok_file,
            number_of_save_proxies=10,
            number_of_min_saved_proxies=5,
            run_test=True,
            no_proxy=False,
            for_https=True,
            API_KEY=API_KEY,
        )
        # OR OTHER USAGE:
        # proxy_decide = Connect.get_proxy(selenium=False, get_random=True, error_file=error_file, ok_file=ok_file, run_test=True)

        # You can use get_proxy with whether count_loop or get_random.
        # count_loop helps you to run it in while with using count_loop+=1 and you can receive proxies 1 by 1 in lines of proxy file.
        # if get_random set True, you get proxy randomly from proxy file without looking count_loop.


        # Now you can use 'proxy_decide' in your requests or in selenium app.
        """
        response = requests.get(
            url,
            headers={},   # Define, if needed (User-Agent, Accept, Referer etc.)
            stream=True,
            proxies=proxy_decide,
            timeout=5,
        )
        """

        error_point = 5
        print('Time of fetching: %s' % Progress.time_definition(time.time() - first_time))
        print()

        Progress.count_down(reload)
        print()

    except Exception as e:
        message = 'An error occurred while running app.\n' \
                  'error_point: %s' % (error_point)
        Progress.exit_app(e=e, message=message, exit_all=False)
        time.sleep(3)
        continue
