#!/usr/bin/python3
import random
from random import choice
import requests
from colorama import Back, Style, Fore
import urllib3

#command line argument
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-w", "--wordlist", help="Subdomain list for scanning", required=True)
args = parser.parse_args()

proxies = {'http':'http://127.0.0.1:9999','https':'https://127.0.0.1:9999'} #change this with your proxy address

#disable ssl warnings with urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def alive():
    pos_code = {"200", "204", "301", "302", "308", "401,""403"}
    neg_code = {"400", "404", "500", "502"}
    proto = {'http://', 'https://'}
    useragent= [
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:83.0) Gecko/20100101 Firefox/83.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.320',
        'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0'
    ]


    with open(args.wordlist, "r") as s:
        for sub in s:
            for p in proto:
                output = open('reportScan.txt', 'a')
                u = {
                    'User-Agent': random.choice(useragent)
                }
                comp = p + sub.rstrip()
                req = requests.get(comp, proxies=proxies, verify=False, headers=u, allow_redirects=False)
                resp = str(req.status_code)
                if resp in pos_code:
                    print(Style.BRIGHT + Fore.YELLOW + f"Possible candidate: [{resp}] {comp}".rstrip() + Fore.RESET)
                    # creo file e appendo result
                    output.write("[Possible candidate]: [%s] %s \n" %(str(resp),str(comp)))
                elif resp in neg_code:
                    print(Style.BRIGHT + Fore.RED + f"[Nothing here] [{resp}] {comp}".rstrip() + Fore.RESET)
                    output.write("[Nothing here]: [%s] %s \n" %(str(resp),str(comp)))
                else:
                    print("Error, review the list or the command or different status code in the response")


if __name__ == "__main__":
    alive()
