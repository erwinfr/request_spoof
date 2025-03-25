import sys
import random
from datetime import datetime, timedelta
import socket
import struct
import os 
import json
import csv
import ipaddress
import codecs
import requests
import time

""" random_ip = str( ipaddress.IPv4Address( random.randint( 0, 4294967295 ) ) )
open_connect = datetime.now().strftime("%d/%b/%Y:%H:%M:%S +0100")
filler1 = " - - ["
filler2 = "] "
print(random_ip) """

""" input list with user agents strings to be used. Loaded into memory and randomly inserted into the request"""
"""Code to read an input file with the urls to request """
with codecs.open('./seed_urls.txt', 'r' ,"utf-8-sig") as input_file:
    """ input list with user agents strings to be used. Loaded into memory and randomly inserted into the request"""
    user_agent_list = (
        'Mozilla/5.0 (Linux; Android 9) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile DuckDuckGo/5 Safari/537.36',
        'Mozilla/5.0 (Linux; Android 10; Pixel 3a Build/QQ2A.200405.005; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.83 Mobile Safari/537.36 YJApp-ANDROID jp.co.yahoo.android.yjtop/3.70.1',
        'Mozilla/5.0 (Linux; Android 11; Lenovo TB-X306X Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Safari/537.36',
        'Dalvik/2.1.0 (Linux; U; Android 10; K15_Plus Build/QP1A.190711.020)',
        'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/86.0.4240.96 Safari/537.36',
        'Mozilla/5.0 (Linux; Android 8.0.0; moto e5 cruise) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0.1; SM-G610M Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0; MYA-L11 Build/HUAWEIMYA-L11; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 9; SM-N950F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 10; SM-G977B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36'
    )
    """Code to go line by line through the input file, insert random IP as requester and insert user-agent"""
    for line in input_file:
        line2 = line.strip() 
        random_ip2 = str( ipaddress.IPv4Address( random.randint( 0, 4294967295 ) ) )
        user_agent = random.choice(user_agent_list)
        ##modified_line = line.replace(line[:47], "cp4s.cool8.nl "+"httpd: "+random_ip2+" 185.87.187.124"+filler1+open_connect+filler2)
        headers = {'X-Forwarded-For': random_ip2, 'User-Agent': user_agent}
        response = requests.get( line2, headers=headers)
        print(line2)
        print(random_ip2)
        print(headers)
        print(response.status_code)
        requests.Session().close()
        time.sleep(2)
    input_file.close()