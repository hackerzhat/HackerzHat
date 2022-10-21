import requests, sys
import argparse
import urllib3
from colorama import Back, Style, Fore
from urllib.parse import unquote

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http':'http://127.0.0.1:8080', 'https':'127.0.0.1:8080'}  # remove proxies from request.get if not use it

banner='''
###################################################################################
# ██   ██ ███████ ███████     ███████ ██    ██ ███████ ███████ ███████ ██████     #             
#  ██ ██  ██      ██          ██      ██    ██    ███     ███  ██      ██   ██    #    
#   ███   ███████ ███████     █████   ██    ██   ███     ███   █████   ██████     #
#  ██ ██       ██      ██     ██      ██    ██  ███     ███    ██      ██   ██    # 
# ██   ██ ███████ ███████     ██       ██████  ███████ ███████ ███████ ██   ██    #
#                                                                                 #                                                                         
# Version: 1 Development by N3rs                                                  #                                                                                                      
###################################################################################
'''

def fuzz_list(file, xfile):
    injection = '"><b>test</b>'
    print(Style.BRIGHT + Fore.YELLOW + "Send Payload" + Fore.RESET)
    xss  = open(xfile, 'r')
    with open(file, 'r') as url:
        for line in url:
            for x in xss:
                request = line.rstrip() + '/' + x.rstrip()
                req = requests.get(request, proxies=proxies, auth=None, verify=False)
                resp = req.text
                if x in resp:
                    print(Style.BRIGHT + Fore.RED + '[*]Found, payload not sanitized[*]: ' + '%s\n' + Fore.RESET) % request


def fuzz_url(xurl, xfile):
    injection = '"><img src=x onerror=alert(document.domain)>'
    print(Style.BRIGHT + Fore.YELLOW + "Send Payload" + Fore.RESET)
    xss  = open(xfile, 'r')
    for x in xss:
        x = x.rstrip()
        request = xurl + x
        req = requests.get(request, proxies=proxies, auth=None, verify=False)
        resp = req.content.decode('utf-8')
        if x in resp:
            print(Style.BRIGHT + Fore.RED + f'[*]Found, payload not sanitized[*]: {request}' + Fore.RESET)


def main():
    parser = argparse.ArgumentParser()
    #parser.add_argument('--url', '-u', required=True, dest='url', help='Target URL')
    parser.add_argument('--single', '-S', action='store_true', required=False, help='single endpoint fuzz')
    parser.add_argument('--multi', '-M', action='store_true', required=False, help='multi endpoint fuzz')
    parser.add_argument('--file', '-f', required=False, dest='file', help='URL wordlist')
    parser.add_argument('--xfile', '-xf', required=True, dest='xfile', help='XSS wordlist')
    parser.add_argument('--xurl', '-xu', required=False, dest='xurl', help='single endpoint')
    parser.add_argument('--verbose', '-v', help='Print more data', action='store_true')
    args = parser.parse_args()

    print(banner)

    file = args.file
    xfile = args.xfile
    xurl = args.xurl
    if sys.argv[1] == '-S':
        fuzz_url(xurl, xfile)
    else:
        fuzz_list(file, xfile)




if __name__ == "__main__":
    main()